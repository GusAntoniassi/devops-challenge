
######################################################
# VPCs
######################################################
resource "aws_vpc" "desafio_2_vpc" {
  cidr_block           = "192.168.0.0/16"
  enable_dns_support   = "true" # Habilita um nome de domínio interno
  enable_dns_hostnames = "true" # Habilita um hostname interno
  instance_tenancy     = "default"

  tags = {
    Name = "Desafio 2 - VPC"
  }
}

######################################################
# Sub-networks
######################################################
resource "aws_subnet" "frontend" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"
    cidr_block = "192.168.0.0/24"
    map_public_ip_on_launch = true # Torna a subnet pública
    
    tags = {
        Name = "Desafio 2 - Frontend"
    }
}

resource "aws_subnet" "backend" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"
    cidr_block = "192.168.1.0/24"
    map_public_ip_on_launch = true

    tags = {
        Name = "Desafio 2 - Backend"
    }
}