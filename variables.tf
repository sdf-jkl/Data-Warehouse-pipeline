variable "aws_keys_file" {
  type        = string
  description = "Path to the JSON file containing AWS access and secret keys"
  default     = "keys.json"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "us-east-1"
}

variable "bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "terraform-demo-terra-bucket"
}