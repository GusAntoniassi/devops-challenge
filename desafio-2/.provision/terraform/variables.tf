variable "server_instance_type" {
  default     = "t2.micro"
  description = "Tipo da instância"
}

variable "ami" {
  default     = "ami-064a0193585662d74"
  description = "AMI do Sistema Operacional"
}

variable "aws_region" {
  default     = "us-east-1"
  description = "Região AWS"
}

variable "aws_credentials_file" {
  default     = "~/.aws/credentials"
  description = "Arquivo de credenciais do AWS CLI"
}

variable "public_key" {
  default     = "~/.ssh/id_rsa.pub"
  description = "Chave pública da máquina para conectar via SSH"
}

variable "aws_credentials_profile" {
  default     = "default"
  description = "Perfil das credenciais definido no arquivo de credenciais. Info: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html"
}
