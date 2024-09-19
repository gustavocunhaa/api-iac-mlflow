resource "aws_instance" "mlflow_instance" {
  ami                    = "ami-0e86e20dae9224db8"
  instance_type          = var.instance_type
  key_name               = var.key_name
  subnet_id              = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.mlflow_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install python3-pip
              sudo pip3 install pipenv --break-system-packages
              sudo pip3 install virtualenv --break-system-packages
              
              # Criar diretório para MLflow
              mkdir /home/ubuntu/mlflow
              cd mlflow

              # Criando ambiente virtual e preparando para o mlflow
              sudo pipenv install mlflow
              sudo pipenv install awscli
              sudo pipenv install boto3
              sudo pipenv shell

              # Iniciar o servidor MLflow
              mlflow server -h 0.0.0.0 --default-artifact-root s3://${aws_s3_bucket.mlflow_bucket.bucket}/mlflow
              EOF
}

output "mlflow_public_ip" {
  value = aws_instance.mlflow_instance.public_ip
}

output "mlflow_url" {
  value = "http://${aws_instance.mlflow_instance.public_ip}:5000"
}