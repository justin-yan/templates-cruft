# Infra

This is a collection of terraform declarations that help define and provision relevant cloud infrastructure.

Generally, the requisite commands are implemented in the Justfile, but deployment is simply done by directly executing the terraform commands.

## Deployment

- `terraform init`
- `terraform plan -refresh-only`
- `terraform apply -refresh-only`
- `terraform plan`
- `terraform apply`
    - Make sure the changes are non-destructive!

