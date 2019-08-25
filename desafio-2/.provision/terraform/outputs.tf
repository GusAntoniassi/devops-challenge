output "public-dns" {
  description = "DNS público da aplicação"
  value = "${aws_instance.desafio_2_web.public_dns}"
}
