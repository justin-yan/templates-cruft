# Flatmono

This collection of cruft templates is intended to help bootstrap a flatmono implementation.  There are a few other technology choices that have been made:

- Github & Github Actions as the VCSHOST + CICD engine
- `just` as the CMDRUNNER
- `cruft` as the TEMPLATER
- vanilla `docker` and GCP Artifact Registry for container image management
- `terraform` for IAC


## Getting Started

1. Initialize an empty repository in GitHub.
2. `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/root`
3. Within the `infra` folder, run `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/artireg-terraform`
    - This example uses GCP, which requires you to have a GCP org, artifact registry activated, gcloud installed and authenticated, and terraform installed locally.  Feel free to substitute with an alternative registry, as we don't rely on any GAR-specific features.
4. Within the `artireg` folder, run:
    - `just init`
    - `terraform apply`
