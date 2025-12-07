# Projeto de FCCPD

# Desafio 1
Temos:

Um servidor Flask rodando na porta 8080

Um cliente em Python que envia requisições ao servidor a cada 3 segundos

Ambos os serviços rodando na mesma rede Docker, comunicando-se pelo nome do serviço (server)

## O que foi feito

Criado um servidor Flask que responde "Servidor ativo! Comunicação OK!"

Cliente Python usando requests para fazer requisições periódicas ao servidor

Containers conectados pela rede interna criada pelo docker-compose

Cliente acessa o servidor usando o hostname do serviço 

Logs do cliente mostram cada requisição e resposta

## Estrutura do desafio
```
desafio1/
  docker-compose.yml
  server/
    Dockerfile
    app.py
  client/
    Dockerfile
    client.py
```
## Como executar

Dentro da pasta do desafio:

```
docker-compose up
```

## Após subir:

O cliente começará automaticamente a fazer requisições ao servidor a cada 3 segundos.

Deve retornar:

Servidor ativo! Comunicação OK!



# Desafio 2
Esse desafio mostra como dados armazenados em um banco PostgreSQL permanecem intactos mesmo após remover o container.
Foi criado um banco com volume persistente e um serviço em Python/Flask que consulta os dados.

## O que foi feito

Criado um container PostgreSQL que executa automaticamente um script carros.sql.

As informações são salvas em um volume Docker chamado pgdata.

Um segundo container (reader) conecta-se ao banco e retorna a lista de carros cadastrados via API.

O container do banco foi removido e iniciado novamente para comprovar que os dados continuam salvos graças ao volume.

## Estrutura do desafio
```
desafio2/
  docker-compose.yml
  carros.sql
  reader/
    Dockerfile
    reader.py
```

## Como executar

Entre na pasta do desafio:
```
cd desafio2
```

Suba os containers:
```
docker-compose up
```

O serviço reader subirá automaticamente e você poderá acessar os dados no localhost:

http://localhost:5000/carros


Ele exibirá a lista de carros cadastrados no banco de dados

# Desafio 3 

## O que a aplicação faz

Sempre que a rota principal é acessada:

Um contador no Redis é incrementado.

A API se conecta ao MySQL e executa um SELECT 'Funcionando'.

A resposta retorna:


O resultado do banco ("Funcionando")


O total de visitas armazenado no Redis

Exemplo de resposta

Funcionando
Visitas registradas no Redis: 4

Estrutura do desafio
```
desafio3/
  docker-compose.yml
  web/
    Dockerfile
    app.py
    requirements.txt
```

## Como executar

Dentro da pasta do desafio:

```
docker-compose up
```


Quando tudo estiver rodando, acesse:

http://localhost:8080/


Cada refresh aumenta o contador armazenado no Redis.


# Desafio 4
Neste desafio foram criados dois microsserviços independentes, que se comunicam entre si através de requisições HTTP, funcionando na mesma rede Docker:

service_usuarios (user) vai fornecer dados de usuários

service_relatorios (consumer) vai consomir o serviço de usuários e monta frases já formatadas

O objetivo é demonstrar comunicação entre microsserviços simples usando Flask e Docker Compose.

## Visão geral
1. service_usuarios

Expondo a rota: /users

Retorna uma lista JSON com usuários contendo:
```
id
name
activeSince
```
(O activeSince é para mostrar quando o usuário ficou ativo no sistema)

2. service_relatorios

Faz uma requisição HTTP ao serviço de usuários:
http://user:5001/users

Processa os dados recebidos

Retorna frases formatadas com o nome e a data de atividade de cada usuário

Cada serviço possui seu próprio Dockerfile e suas próprias dependências.

## Estrutura do desafio
```
desafio_microsservicos/
  docker-compose.yml
  user/
    Dockerfile
    app.py
    requirements.txt
  consumer/
    Dockerfile
    app.py
    requirements.txt
```
## Como executar

Dentro da pasta do desafio:
```
docker-compose up
```

Isso fará:

Subir o microsserviço user (Flask na porta interna 5001, exposta como 5001)

Subir o microsserviço consumer (Flask na porta interna 5002, exposta como 5002)

Criar a rede interna automática para permitir comunicação entre eles

Testando os serviços
1. Microsserviço de usuários

No navegador:

curl http://localhost:5001/users


Resposta esperada:
```
[
  {"id": 1, "name": "Alice", "activeSince": "2022-01-10"},
  {"id": 2, "name": "Bruno", "activeSince": "2023-03-15"},
  {"id": 3, "name": "Carlos", "activeSince": "2024-05-01"},
  {"id": 4, "name": "Daniela", "activeSince": "2021-11-22"},
  {"id": 5, "name": "Eduardo", "activeSince": "2020-07-08"},
  {"id": 6, "name": "Fernanda", "activeSince": "2023-09-19"},
  {"id": 7, "name": "Gabriel", "activeSince": "2022-06-30"}
]
```
2. Microsserviço consumidor
curl http://localhost:5002/combined


Exemplo de resposta:
```
Usuario Alice     desde 2022-01-10
Usuario Bruno     desde 2023-03-15
Usuario Carlos    desde 2024-05-01
Usuario Daniela   desde 2021-11-22
...
```

# Desafio 5
Neste desafio foi criada uma arquitetura com três serviços que trabalham juntos por meio de uma comunicação HTTP dentro do Docker:

Um microsserviço de usuários

Um microsserviço de pedidos

Um API Gateway, que centraliza o acesso aos dois serviços

O objetivo é demonstrar como um único ponto de entrada pode organizar e unificar chamadas para múltiplos microsserviços internos.

## Visão geral dos serviços
service_usuarios

Rota: GET /users

Retorna uma lista de usuários em formato JSON.

service_pedidos

Rota: GET /orders

Retorna uma lista de pedidos em formato JSON, contendo ID do pedido, usuário associado e total.

gateway

Rota: GET /users
Encaminha a requisição para user-service

Rota: GET /orders
Encaminha a requisição para order-service

Rota: GET /
Apenas retorna uma mensagem indicando que o gateway está funcionando.

Do ponto de vista do cliente, somente o gateway é acessado.

## Estrutura do desafio
``` 
desafio_gateway/
  docker-compose.yml
  gateway/
    Dockerfile
    app.py
    requirements.txt
  user/
    Dockerfile
    app.py
    requirements.txt
  order/
    Dockerfile
    app.py
    requirements.txt
```
## Como executar

Dentro da pasta do desafio:
```
docker-compose up
```

O Docker Compose irá:

Subir o microsserviço user-service

Subir o microsserviço order-service

Subir o API Gateway

Criar automaticamente a rede interna para permitir comunicação via DNS interno

## Testando o sistema pelo Gateway

Todas as chamadas devem ser feitas para o gateway na porta 8080 do host.

### Listar usuários:
http://localhost:8080/users

### Listar pedidos:
http://localhost:8080/orders

## Para mostrar que o gateway está funcionando:
http://localhost:8080/


As respostas vêm do gateway, que por sua vez consulta os outros microsserviços.
