## Executar a aplicação
**Requisitos necessários: Docker**

```sh
$ docker build -t desafio-1:latest .
$ docker run -d -p 80:5000 desafio-1:latest
```

## Deploy
**Requisitos necessários: Terraform e Ansible**

Caso seja necessário alterar configurações como o caminho da chave pública, do arquivo de credenciais ou o perfil da AWS, faça uma cópia do arquivo `terraform.tfvars.dist`, renomeando-o para `terraform.tfvars` e alterando as variáveis conforme a necessidade.

Depois de fazer as configurações necessárias, provisione a infraestrutura da aplicação com o seguinte comando:

```sh
$ terraform init
$ terraform plan
$ terraform apply
```

### Testar a aplicação
Teste GET
```sh
$ curl http://localhost:5000/characters
```
Teste POST
```sh
$ curl -X POST -H "Content-Type: application/json" -d '{
  "Race": "Hobbit",
  "age": "589",
  "name": "Gollum"
}' http://localhost:5000/characters
```

## Referências
- Docker + Flask: https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
- Provisionamento c/ Terraform: https://www.youtube.com/watch?v=lrAycU7_XnQ
- Organização do projeto Terraform: https://www.terraform-best-practices.com/examples/terraform/small-size-infrastructure
- Variáveis Terraform: https://learn.hashicorp.com/terraform/getting-started/variables.html
- Integrando Ansible com Terraform: https://getintodevops.com/blog/using-ansible-with-terraform
- Instalação do Docker no Ansible: https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-install-and-set-up-docker-on-ubuntu-18-04
