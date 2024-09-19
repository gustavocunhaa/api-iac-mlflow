provider "aws" {
  alias = "east"
  profile = "default"
  region = var.region
  
  default_tags {
    tags = var.tags
  }
}
