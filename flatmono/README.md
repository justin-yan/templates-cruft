# Flatmono

This collection of cruft templates is intended to help bootstrap a flatmono implementation.

A few technology choices are made up front:

- Github & Github Actions as the VCSHOST + CICD engine
- `just` as the CMDRUNNER
- `cruft` as the TEMPLATER
- vanilla `docker` and GCP Artifact Registry for container image management
- `terraform` for IAC


## Getting Started

1. Set up your github organization and repo as needed.
1. `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/root'`
2. Run `just setup` from the root directory.
4. Within the `infra` folder, run `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/artireg`
    - This example uses GCP, which requires you to have a GCP org, artifact registry activated, gcloud installed and authenticated, and terraform installed locally.  Feel free to substitute with an alternative registry, as we don't rely on any GAR-specific features.
5. Within the `artireg` folder, run:
    - `just init`
    - `terraform apply`
