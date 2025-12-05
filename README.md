# Projeto de FCCPD

## Desafio 1
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



## Desafio 2
carros.sql->Vai criar uma tabela se não existir e vai inserir os carros

docker-compose.yml->Vai criar e configurar o SQL, vai definir as opções para o ambiente virtual e vai permitir analisar informações após rodar

Para rodar:

Acesse a pasta onde estão os arquivos e utilize o comando abaixo:

`docker-compose up -d`

esse comando irá ler o docker-compose.yml e vai criar container e configurá-lo.

Para executar utilize o comando abaixo:

`docker exec -it desafio2_db psql -U admin -d desafio2`

Desse jeito já vai funcionar e, para completar, faça uma consulta para mostrar os carros. Segue a consulta abaixo:

`select * from carros;`


## Desafio 3 

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


## Desafio 4
Na parte do consumer tem o arquivo app.py que vai buscar do app.py (que está na pasta user) a lista de usuários e vai mostrar formatado

Dockerfile vai preparar o ambiente da aplicação

Na parte do user o app.py vai basicamente fornecer uma lista de usuários (de forma desorganizada) 

Dockerfile vai preparar o ambiente da aplicação

Ambos tem requirements.txt e, ao rodar, instalar tudo que for necessário para a aplicação

Para rodar basta usar o comando abaixo:

`docker compose up --build`

Tudo que esta no app.py da pasta consumer vai aparecer em http://localhost:5002/combined (aqui vai mostrar formatado a lista de usuários)

Tudo que esta no app.py da pasta user vai aparecer em http://localhost:5001/users

## Desafio 5
Na pasta gateway o app.py irá servir como uma central que vai receber requisições do app.py(que esta na pasta order) e no app.py(que esta na pasta user)

Na pasta order o app.py vai fornecer informações de pedidos organizadas, pegando informações que está na app.py(que está na pasta user)

na pasta user o app.py vai fornecer uma lista de usuários

Todos os Dockerfile vão preparar o ambiente da aplicação

Todos os requirements.txt, ao rodar, instalar tudo que for necessário para a aplicação

`docker-compose up`     

Irá mostrar tudo que aparece no app.py do gateway http://localhost:8080/

Irá mostrar tudo que aparece no app.py do user http://localhost:8080/users

Irá mostrar tudo que aparece no app.py do orders http://localhost:8080/orders
