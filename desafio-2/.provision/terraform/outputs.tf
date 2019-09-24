output "public-dns-web" {
  description = "DNS público da aplicação Wordpress"
  value = "${aws_instance.desafio_2_web.public_dns}"
}
output "public-dns-db" {
  description = "DNS público da aplicação DB"
  value = "${aws_instance.desafio_2_db.public_dns}"
}

output "public-dns-lb" {
  description = "DNS público do Load Balancer"
  value = "${aws_alb.desafio_2_alb.dns_name}"
}