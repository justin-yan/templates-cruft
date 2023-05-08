import nox

@nox.session(python=['3.8', '3.9', '3.10', '3.11'])
def cross_verify(session):
    session.install("ruff")
    session.install("pytest")
    session.install("mypy")
    session.install("hypothesis")
    session.run("ruff", "check", "src", "tests")
    session.run("mypy", "--explicit-package-bases", "-p", "{{cookiecutter.package_name}}")
    session.run("mypy", "--allow-untyped-defs", "tests")
    session.run("pytest", "tests")
