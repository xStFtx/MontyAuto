provider "aws" {
  region = "us-west-2"
}

resource "aws_ecs_cluster" "automation" {
  name = "automation-cluster"
}

resource "aws_lb" "app" {
  name               = "automation-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb.id]
  subnets            = aws_subnet.public.*.id
} 