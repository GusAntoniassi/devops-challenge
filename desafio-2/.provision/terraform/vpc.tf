data "aws_availability_zones" "available_azs" {
  state = "available"
}

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
resource "aws_subnet" "backend" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"
    cidr_block = "192.168.0.0/25" # Com o CIDR /24 estava dando erro de conflito de IPs entre as subnets
    map_public_ip_on_launch = true

    tags = {
        Name = "Desafio 2 - Backend"
    }
}

resource "aws_subnet" "frontend_a" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"
    cidr_block = "192.168.1.0/25"
    map_public_ip_on_launch = true # Torna a subnet pública
    availability_zone = "${data.aws_availability_zones.available_azs.names[0]}"
    
    tags = {
        Name = "Desafio 2 - Frontend A"
    }
}

resource "aws_subnet" "frontend_b" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"
    cidr_block = "192.168.2.0/25"
    map_public_ip_on_launch = true # Torna a subnet pública
    availability_zone = "${data.aws_availability_zones.available_azs.names[1]}"
    
    tags = {
        Name = "Desafio 2 - Frontend B"
    }
}