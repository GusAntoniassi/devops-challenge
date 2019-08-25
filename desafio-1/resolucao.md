# Deploy
**Requisitos necessários: Terraform e Ansible (>=2.7)**

Para subir a aplicação na AWS, será necessário ter um arquivo com credenciais da AWS. O diretório padrão para ele é em `~/.aws/credentials`, mas é possível alterar este diretório conforme explicado abaixo. Para maiores informações, consulte a [documentação da AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

Também será necessário ter um par de chaves SSH criado. O caminho padrão da chave pública é `~/.ssh/id_rsa.pub`, porém também é possível alterar este diretório conforme explicado abaixo. O par de chaves pode ser gerado executando o comando `ssh-keygen`.

Caso seja necessário alterar configurações como o caminho da chave pública, do arquivo de credenciais ou o perfil da AWS, faça uma cópia do arquivo `terraform.tfvars.dist`, renomeando-o para `terraform.tfvars` e alterando as variáveis conforme a necessidade.

Depois de fazer as configurações necessárias, provisione a infraestrutura da aplicação com o seguinte comando:

```sh
$ cd .provision/terraform
$ terraform init
$ terraform plan
$ terraform apply
```

Após executar o deploy com sucesso, o Terraform irá retornar o endereço da aplicação na AWS.
