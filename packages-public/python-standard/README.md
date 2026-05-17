Public Python Package
=====================

This is a basic template for publishing a public python package to PyPI using Github as your forge and CICD provider.


## Github Setup

- Use trusted publishing with PyPI.  Create a pending publisher with your org name, project name, and `register.yaml` as the workflow.
- Project assumes trunk-based development targeting `main`, so set the branch protection rules.
	- Require a pull request before merge.
	- Require `pr` status check to pass before merge.
- Lock Github Actions down: restrict reusable actions, require a SHA, require approvals for external contributors.
