terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.61.0"
    }
  }
}

provider "google" {
  project = "{{cookiecutter.gcp_project_name}}"
  region  = "us-west1"
  zone    = "us-west1-c"
}

provider "google-beta" {
  project = "{{cookiecutter.gcp_project_name}}"
  region  = "us-west1"
  zone    = "us-west1-c"
}

resource "google_artifact_registry_repository" "images" {
  provider = google-beta

  location = "us-west1"
  repository_id = "images"
  description = "Docker Repository for Base Images"
  format = "DOCKER"
  mode = "STANDARD_REPOSITORY"
}

resource "google_service_account" "github-actions-cicd" {
  account_id   = "github-actions-cicd"
  display_name = "github-actions-cicd"
  project      = "iomorphic"
}

data "google_iam_policy" "images_policy" {
  binding {
    role = "roles/artifactregistry.reader"
    members = [
      "domain:{{cookiecutter.gcp_org_domain}}",
    ]
  }

  binding {
    role = "roles/artifactregistry.createOnPushWriter"
    members = [
      google_service_account.github-actions-cicd.member,
    ]
  }
}

resource "google_artifact_registry_repository_iam_policy" "images_policy" {
  provider = google-beta

  project = google_artifact_registry_repository.images.project
  location = google_artifact_registry_repository.images.location
  repository = google_artifact_registry_repository.images.name
  policy_data = data.google_iam_policy.images_policy.policy_data
}
