output "public-dns" {
  description = "DNS público da aplicação"
  value = "${aws_instance.desafio_1.public_dns}"
}
