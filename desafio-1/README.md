## Executar a aplicação localmente
**Requisitos necessários: Docker**

```sh
$ docker build -t desafio-1:latest .
$ docker run -d -p 80:5000 desafio-1:latest
```

## Deploy
[Clique aqui para acessar a documentação](resolucao.md).

## Testar a aplicação

Cadastrar um usuário

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{
  "username": "gus",
  "password": "123456"
}' http://localhost:5000/users
```

Login
```sh
$ curl -X POST -H "Content-Type: application/json" -d '{
  "username": "gus",
  "password": "123456"
}' http://localhost:5000/login
```

Listar personagens
```sh
$ curl -H "Authorization: Bearer <Token JWT aqui>" http://localhost:5000/characters
```

Buscar personagem por ID
```sh
$ curl -H "Authorization: Bearer <Token JWT aqui>" http://localhost:5000/characters/1
```

Buscar personagem por nome
```sh
$ curl -H "Authorization: Bearer <Token JWT aqui>" http://localhost:5000/characters/ara
```

Cadastrar personagem
```sh
$ curl -X POST -H "Authorization: Bearer <Token JWT aqui>" -H "Content-Type: application/json" -d '{
  "race": "Hobbit",
  "age": "589",
  "name": "Gollum"
}' http://localhost:5000/characters
```

Editar personagem
```sh
$ curl -X PUT -H "Authorization: Bearer <Token JWT aqui>" -H "Content-Type: application/json" -d '{
  "race": "Hobbit",
  "age": "589",
  "name": "Gollum"
}' http://localhost:5000/characters/1
```

Excluir personagem
```sh
$ curl -X DELETE -H "Authorization: Bearer <Token JWT aqui>" http://localhost:5000/characters/1
```

## Collection do Postman
[![Executar no Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/91a89b865e6c65b7242f#?env%5BDesafio%201%5D=W3sia2V5IjoiYXBpX3VybCIsInZhbHVlIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJhcGlfdXNlcm5hbWUiLCJ2YWx1ZSI6Imd1cyIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiYXBpX3Bhc3N3b3JkIiwidmFsdWUiOiIxMjM0NTYiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InRva2VuIiwidmFsdWUiOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKcWRHa2lPaUptWWpZeE1qRTBaQzFrTURWaUxUUmpNREl0T1dGaVlTMWlaR0U1TmpRMVlXUXpZaklpTENKbGVIQWlPakUxTmpZM05EQTVPVFlzSW1aeVpYTm9JanBtWVd4elpTd2lhV0YwSWpveE5UWTJOelF3TURrMkxDSjBlWEJsSWpvaVlXTmpaWE56SWl3aWJtSm1Jam94TlRZMk56UXdNRGsyTENKcFpHVnVkR2wwZVNJNkltZDFjeUo5LkQzYTFRT09SalF2cVJzeS1pS0ZGeG5MTi1FOHRmemZWVFduY1JlMUZXZ28iLCJlbmFibGVkIjp0cnVlfV0=)

## Referências
- Docker + Flask: https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
- Provisionamento c/ Terraform: https://www.youtube.com/watch?v=lrAycU7_XnQ
- Organização do projeto Terraform: https://www.terraform-best-practices.com/examples/terraform/small-size-infrastructure
- Variáveis Terraform: https://learn.hashicorp.com/terraform/getting-started/variables.html
- Integrando Ansible com Terraform: https://getintodevops.com/blog/using-ansible-with-terraform
- Instalação do Docker no Ansible: https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-install-and-set-up-docker-on-ubuntu-18-04
- Organização do projeto Ansible: https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html
- Autenticação JWT e CRUD com SQLite no Flask: https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb