# Descrição da arquitetura proposta

![Arquitetura](https://i.imgur.com/HkgXFPw.png)

A arquitetura descrita segue o padrão de aplicações *serverless*, ou seja, os servidores são abstraídos no gerenciamento da aplicação, e gerenciados pelo próprio provedor cloud utilizado.

Ao se conectar no domínio da aplicação web, o usuário estará buscando os arquivos estáticos de um *Bucket* no serviço de armazenamento **S3**. Para otimizar a entrega deste conteúdo, em vez de solicitar os arquivos diretamente do S3, a aplicação utilizará os serviços do **CloudFront**, uma rede de entrega de conteúdo (CDN) distribuída por todo o mundo, otimizando assim o tempo de resposta para o conteúdo da aplicação.

A aplicação pode ocasionalmente solicitar a leitura ou escrita de dados em uma base de dados. Para fazer este acesso, é utilizado o serviço **AWS Lambda**, que permite a execução de código sem a necessidade de provisionamento por parte dos usuários. Este padrão reduz os custos com hospedagem e manutenção de servidores, visto que o utilizador é cobrado apenas pelo tempo durante o qual seu código executa.

Para criar as rotas para acessar às funções Lambda, é utilizado o serviço de **API Gateway**. O Gateway também está atrás do CloudFront, o que garante uma entrega otimizada das chamadas da API e permite que seja feito cache das respostas da API.

A base de dados NoSQL é gerenciada através do serviço **DynamoDB**, que facilita a escalabilidade e resiliência da base, permitindo utilizar um padrão de múltiplas zonas de disponibilidade sem se preocupar em realizar a sincronização entre os dados. 

O código Lambda e o banco DynamoDB estão isolados em uma rede privada (VPC), o que aumenta a segurança da aplicação visto que o Lambda só pode ser acessado pelo API Gateway, e o banco de dados só pode ser acessado pelo Lambda. Desta forma, os serviços não estão conectados à internet e não podem acessar ou serem acessados por serviços externos à rede privada. 