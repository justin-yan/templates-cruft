# Flatmono

This collection of cruft templates is intended to help bootstrap a flatmono implementation.

A few technology choices are made up front:

- Github & Github Actions as the VCSHOST + CICD engine
- `just` as the CMDRUNNER
- `cruft` as the TEMPLATER
- vanilla `docker` and GCP Artifact Registry for container image management
- `terraform` for IAC


## Getting Started

1. Set up your github organization as needed.
2. `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/root'`
3. init a git repo and push to your organization as desired.
4. Run `just setup` from repo root.

### Images

1. `cd images`
2. `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/image'`

### Infra

1. `cd infra`
2. `cruft create https://github.com/justin-yan/templates-cruft --directory='flatmono/infra'`
