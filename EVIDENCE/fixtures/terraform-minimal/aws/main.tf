terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 6.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

variable "environment" {
  type    = string
  default = "omega-alpha"
}

resource "aws_instance" "web" {
  ami           = "ami-example-placeholder"
  instance_type = "t3.small"

  tags = {
    Name        = "omega-x-${var.environment}-web"
    Environment = var.environment
  }
}

resource "aws_db_instance" "app" {
  identifier          = "omega-x-${var.environment}-db"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  storage_type        = "gp3"
  skip_final_snapshot = true
  username            = "example"
}
