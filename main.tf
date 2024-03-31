terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = var.region
  access_key = jsondecode(file(var.aws_keys_file))["access_key"]
  secret_key = jsondecode(file(var.aws_keys_file))["secret_key"]
}

# Create a bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucket-meow-meow-meow"

  tags = {
    Name        = var.bucket_name
    Environment = "Dev"
  }
}