terraform {
  required_version = ">= 0.13"
  required_providers {
    aws = "~> 4.30"
  }
}

terraform {
  backend "s3" {
    bucket         = "terraform-state"
    key            = "lambda-function-service"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-central-1"

  assume_role {
    role_arn = var.environment_aws_arn
  }
}

