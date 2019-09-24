provider "aws" {
  region                  = "${var.aws_region}"
  shared_credentials_file = "${var.aws_credentials_file}"
  profile                 = "${var.aws_credentials_profile}"
}

resource "aws_key_pair" "public_key" {
  key_name   = "public_key"
  public_key = "${file("${var.public_key}")}"
}

resource "aws_instance" "desafio_2_db" {
  ami           = "${var.ami}"
  instance_type = "${var.server_instance_type}"
  subnet_id     = "${aws_subnet.backend.id}"

  tags = {
    Name = "Desafio 2 - DB"
    Type = "dbserver"
  }

  security_groups = [
    "${aws_security_group.allow_ssh.id}",
    "${aws_security_group.allow_mysql.id}"
  ]
  associate_public_ip_address = true

  key_name = "${aws_key_pair.public_key.key_name}"

  provisioner "local-exec" {
    command = <<EOT
      sleep 120; \
      cd ../ansible && \
      AWS_PROFILE='${var.aws_credentials_profile}' \
      ansible-playbook \
        --vault-password-file .vault_pass \
        -u ubuntu \
        -i inventory/ec2.py \
        dbservers.yml
EOT
  }
}

resource "aws_instance" "desafio_2_web" {
  ami           = "${var.ami}"
  instance_type = "${var.server_instance_type}"
  subnet_id     = "${aws_subnet.frontend_a.id}"

  tags = {
    Name = "Desafio 2 - Web"
    Type = "webserver"
  }

  security_groups = [
    "${aws_security_group.allow_ssh.id}",
    "${aws_security_group.allow_http.id}"
  ]
  associate_public_ip_address = true

  key_name = "${aws_key_pair.public_key.key_name}"

  provisioner "local-exec" {
    command = <<EOT
      sleep 120; \
      cd ../ansible && \
      AWS_PROFILE='${var.aws_credentials_profile}' \
      ansible-playbook \
        --vault-password-file .vault_pass \
        -u ubuntu \
        -i inventory/ec2.py \
        --extra-vars "db_address=${aws_instance.desafio_2_db.private_dns}" \
        webservers.yml
EOT
  }
}
