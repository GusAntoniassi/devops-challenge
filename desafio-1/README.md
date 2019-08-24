## Executar a aplicação localmente
**Requisitos necessários: Docker**

```sh
$ docker build -t desafio-1:latest .
$ docker run -d -p 80:5000 desafio-1:latest
```

## Deploy
**Requisitos necessários: Terraform e Ansible**

Para subir a aplicação na AWS, será necessário ter um arquivo com credenciais da AWS. O diretório padrão para ele é em `~/.aws/credentials`, mas é possível alterar este diretório conforme explicado abaixo. Para maiores informações, consulte a [documentação da AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

Caso seja necessário alterar configurações como o caminho da chave pública, do arquivo de credenciais ou o perfil da AWS, faça uma cópia do arquivo `terraform.tfvars.dist`, renomeando-o para `terraform.tfvars` e alterando as variáveis conforme a necessidade.

Depois de fazer as configurações necessárias, provisione a infraestrutura da aplicação com o seguinte comando:

```sh
$ cd .provision/terraform
$ terraform init
$ terraform plan
$ terraform apply
```

Após executar o deploy com sucesso, o Terraform irá retornar o endereço da aplicação na AWS.

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
- Organização do projeto Ansible: https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html