## Executar a aplicação localmente
**Requisitos necessários: Docker**

```sh
$ docker build -t desafio-1:latest .
$ docker run -d -p 80:5000 desafio-1:latest
```

## Deploy
[Clique aqui](resolucao.md).

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