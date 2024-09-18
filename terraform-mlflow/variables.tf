variable "region" {
  default     = "us-east-1"
}

variable "instance_type" {
  default     = "t2.micro"
}

variable "key_name" {
  default     = "mlflow-key"
}

variable "bucket_name" {
  default     = "a3data-mlflow-storage"
}

variable "tags" {
    default = {
        projeto    = "aprovador_emprestismos",
        componente = "machine_learning"
    }
}
