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