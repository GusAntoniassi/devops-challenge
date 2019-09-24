resource "aws_alb" "desafio_2_alb" {
  name = "desafio-2-alb"
  internal = false
  load_balancer_type = "application"
  security_groups = [
    "${aws_security_group.allow_http.id}", 
    "${aws_security_group.allow_ssh.id}"
  ]

  subnets = [
    "${aws_subnet.frontend_a.id}",
    "${aws_subnet.frontend_b.id}"
  ]

  tags = {
    Name = "Desafio 2 - ALB"
  }
}

resource "aws_alb_listener" "desafio_2_alb_listener" {
  load_balancer_arn = "${aws_alb.desafio_2_alb.arn}"
  port = "80"
  protocol = "HTTP"

  default_action {
    target_group_arn = "${aws_alb_target_group.desafio_2_alb_target_group.arn}"
    type = "forward"
  }
}

resource "aws_alb_target_group" "desafio_2_alb_target_group" {
  name = "desafio-2-tg"
  port = "9999"
  protocol = "HTTP"
  vpc_id = "${aws_vpc.desafio_2_vpc.id}"
  tags = {
    Name = "Desafio 2 - Target Group"
  }

  health_check {
    healthy_threshold = 3
    unhealthy_threshold = 10
    timeout = 5
    interval = 10
    path = "/"
    port = "80"
  }
}

resource "aws_alb_listener_rule" "desafio_2_alb_listener_rule" {
  depends_on = ["aws_alb_target_group.desafio_2_alb_target_group"]
  listener_arn = "${aws_alb_listener.desafio_2_alb_listener.arn}"
  
  action {
    type = "forward"
    target_group_arn = "${aws_alb_target_group.desafio_2_alb_target_group.id}"
  }

  condition {
    field = "path-pattern"
    values = [
      "/*" # Apenas para teste, como não vamos ter um domínio registrado para a aplicação
    ]
  }
}

# @TODO: Usar autoscaling attachment
resource "aws_alb_target_group_attachment" "desafio_2_tg_attachment" {
  target_group_arn = "${aws_alb_target_group.desafio_2_alb_target_group.arn}"
  target_id = "${aws_instance.desafio_2_web.id}"
  port = 80
}