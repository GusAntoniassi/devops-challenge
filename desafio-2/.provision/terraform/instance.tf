provider "aws" {
  region                  = "${var.aws_region}"
  shared_credentials_file = "${var.aws_credentials_file}"
  profile                 = "${var.aws_credentials_profile}"
}

resource "aws_key_pair" "public_key" {
  key_name   = "public_key"
  public_key = "${file("${var.public_key}")}"
}

resource "aws_security_group" "allow_ssh" {
  name = "allow_ssh"
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
    Name = "Desafio 1 - SSH"
  }
}

resource "aws_security_group" "allow_http" {
  name = "allow_http"
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
    Name = "Desafio 1 - HTTP"
  }

}

resource "aws_instance" "desafio_2_web" {
  ami           = "${var.ami}"
  instance_type = "${var.server_instance_type}"

  tags = {
    Name = "Desafio 2 - Web"
    Type = "webserver"
  }

  security_groups = [
    "${aws_security_group.allow_ssh.name}",
    "${aws_security_group.allow_http.name}"
  ]
  associate_public_ip_address = true

  key_name = "${aws_key_pair.public_key.key_name}"

  # provisioner "local-exec" {
  #   command = "sleep 120; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i '${aws_instance.desafio_2_web.public_ip},' ../ansible/master.yml"
  # }
}
