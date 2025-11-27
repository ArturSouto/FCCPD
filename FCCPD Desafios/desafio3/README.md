O app.py utiliza flask (parte web solicitada), MySQL (para a parte de database) e Redis (para a parte do cache);

Dockerfile vai preparar o ambiente da aplicação

O requirements.txt vai, ao rodar, instalar tudo que for necessário para a aplicação



Ao usar o comando abaixo dentro da pasta, vai rodar a aplicação:

`docker-compose up -d`

esse comando irá ler o docker-compose.yml e vai criar container e configurá-lo.

Vai mostrar funcionando em localhost, basta acessar http://localhost:8080/
