import argparse
import io
import os
import tarfile
import urllib.request
import urllib.request
from email.message import EmailMessage
from pathlib import Path
from zipfile import ZipInfo

from wheel.wheelfile import WheelFile

#######
### Define mapping of archive name to pypi platform tag
#######
PLATFORMS = {
}
SUMMARY = ""
LICENSE = ""
REPO_URL = ""
#######
### End mapping section
#######


def make_message(headers, payload=None):
    msg = EmailMessage()
    for name, value in headers.items():
        if isinstance(value, list):
            for value_part in value:
                msg[name] = value_part
        else:
            msg[name] = value
    if payload:
        msg.set_payload(payload)
    return msg


def write_wheel_file(filename, contents):
    with WheelFile(filename, 'w') as wheel:
        for member_info, member_source in contents.items():
            wheel.writestr(member_info, bytes(member_source))
    return filename


def convert_archive_to_wheel(
        name: str,
        pypi_version: str,
        archive: bytes,
        platform_tag: str
):
    package_name = f'py{name}'
    contents = {}

    # Extract the command binary
    datadir = f'{package_name}-{pypi_version}.data'
    with tarfile.open(mode="r:gz", fileobj=io.BytesIO(archive)) as tar:
        for entry in tar:
            if entry.isreg():
                if entry.name.split('/')[-1] == f"{name}":
                    contents[f'{datadir}/scripts/{name}'] = tar.extractfile(entry).read()

    # Create distinfo
    tag = f'py3-none-{platform_tag}'
    metadata = {'Summary': SUMMARY,
                'Description-Content-Type': 'text/markdown',
                'License': LICENSE,
                'Requires-Python': '~=3.5',
                'Project-URL': f'Repository, {REPO_URL}',
                }
    with open('README.md') as f:
        description = f.read()
    dist_info = f'{package_name}-{pypi_version}.dist-info'
    contents[f'{dist_info}/METADATA'] = make_message({
            'Metadata-Version': '2.1',
            'Name': package_name,
            'Version': pypi_version,
            **metadata,
        }, description)
    contents[f'{dist_info}/WHEEL'] = make_message({
            'Wheel-Version': '1.0',
            'Generator': f'{package_name} build_wheels.py',
            'Root-Is-Purelib': 'false',
            'Tag': tag,
        })

    wheel_name = f'{package_name}-{pypi_version}-{tag}.whl'
    outdir = "dist"
    Path(outdir).mkdir(exist_ok=True)
    return write_wheel_file(os.path.join(outdir, wheel_name), contents)


def build_wheel(name: str, base_url: str, version: str, pypi_version: str, target: str, platform_tag: str):
    ######
    ### Begin: Custom URL formatting
    ######
    full_url = f"{base_url}/download/{version}/{name}-{version}-{target}.tar.gz"
    ######
    ### End: Custom URL formatting
    ######

    with urllib.request.urlopen(full_url) as response:
        archive = response.read()

    convert_archive_to_wheel(name, pypi_version, archive, platform_tag)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--version')
    parser.add_argument('--pypi_version')
    parser.add_argument('--url')
    args = parser.parse_args()
    for download_target, pypi_platform_tag in PLATFORMS.items():
        build_wheel(args.name, args.url, args.version, args.pypi_version, download_target, pypi_platform_tag)
