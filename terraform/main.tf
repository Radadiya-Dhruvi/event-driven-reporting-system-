provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "input_bucket" {
  bucket = "event-input-demo-terraform"
}

resource "aws_dynamodb_table" "table" {
  name         = "ProcessedData"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}
