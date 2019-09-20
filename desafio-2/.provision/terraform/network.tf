
######################################################
# Internet Gateway e tabelas de roteamento
######################################################
resource "aws_internet_gateway" "desafio_2_igw" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"

    tags = {
        Name = "Desafio 2 - Internet Gateway"
    }
}

resource "aws_route_table" "desafio_2_rt" {
    vpc_id = "${aws_vpc.desafio_2_vpc.id}"

    route {
        cidr_block = "0.0.0.0/0"

        gateway_id = "${aws_internet_gateway.desafio_2_igw.id}"
    }

    tags = {
        Name = "Desafio 2 - Acesso Internet Route Table"
    }
}

resource "aws_route_table_association" "desafio_2_rta_frontend" {
    route_table_id = "${aws_route_table.desafio_2_rt.id}"
    subnet_id = "${aws_subnet.frontend.id}"
}

resource "aws_route_table_association" "desafio_2_rta_backend" {
    route_table_id = "${aws_route_table.desafio_2_rt.id}"
    subnet_id = "${aws_subnet.backend.id}"
}

######################################################
# Security Groups 
######################################################
resource "aws_security_group" "allow_ssh" {
  name = "allow_ssh"
  vpc_id = "${aws_vpc.desafio_2_vpc.id}"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Desafio 2 - SSH"
  }
}

resource "aws_security_group" "allow_http" {
  name = "allow_http"
  vpc_id = "${aws_vpc.desafio_2_vpc.id}"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Desafio 2 - HTTP"
  }

}
resource "aws_security_group" "allow_mysql" {
  name = "allow_mysql"
  vpc_id = "${aws_vpc.desafio_2_vpc.id}"

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Desafio 2 - HTTP"
  }

}