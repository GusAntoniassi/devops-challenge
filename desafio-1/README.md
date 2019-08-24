## Executar a aplicação
**Requisitos necessários: Docker**

```sh
$ docker build -t desafio-1:latest .
$ docker run -d -p 80:5000 desafio-1:latest
```

## Deploy
**Requisitos necessários: Terraform**

Caso seja necessário alterar configurações como o caminho da chave pública, do arquivo de credenciais ou o perfil da AWS, faça uma cópia do arquivo `terraform.tfvars.dist`, renomeando-o para `terraform.tfvars` e alterando as variáveis conforme a necessidade.

Depois de fazer as configurações necessárias, provisione a infraestrutura da aplicação com o seguinte comando:

```sh
$ terraform init
$ terraform plan
$ terraform apply
```

Depois de provisionar o servidor, copie o código fonte da aplicação utilizando o seguinte comando:
```sh
$ rsync -r --filter=':- .gitignore' . ubuntu@<endereço do ec2>:/home/ubuntu/app
```

Depois conecte-se nele via SSH usando o usuário `ubuntu` e o nome de domínio fornecido pelo Terraform. Dentro do servidor, [instale o Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository) e [execute a aplicação](#executar-a-aplicacao) na porta 80.

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
