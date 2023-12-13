pybin
=====

The pybin template was inspired by how [Maturin packages rust binaries](https://www.maturin.rs/bindings#bin).  The key observation is that in the wheel format, the [distribution-1.0.data/scripts/ directory is copied to bin](https://packaging.python.org/en/latest/specifications/binary-distribution-format/#installing-a-wheel-distribution-1-0-py32-none-any-whl), which means we can leverage this to seamlessly copy binaries into a user's PATH.

The core of the logic lies in the `build_wheels.py` script, which essentially constructs a wheel file-by-file, containing little more than a binary and some metadata.  A packager just needs to provide the download URLs for the binaries, and to map them to a python packaging wheel tag to ensure the correct platform-specific distribution.
