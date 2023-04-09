# {{cookiecutter.project_name}}

- `cruft create https://github.com/justin-yan/templates-cruft --directory=flatmono-just-gha` was the command used to generate this project.

We follow the following conventions:

- Flatmono repo structure
    - The different asset types are hardcoded since [cookiecutter is missing support](https://github.com/cookiecutter/cookiecutter/issues/474).
- [just](https://just.systems/) as the Command Runner
- Github Actions as the CICD platform.
- Cruft as the Templater.
