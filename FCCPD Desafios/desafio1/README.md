Servidor
app.py->cria uma aplicação, define a rota e a porta do servidor para o cliente se hospedar
Dockerfile->São as dependências necessárias para a parte do servidor e a executa

Cliente
client.py-> Faz requisições para o servidor, fica tentando acessar o servidor e vai mostrar uma mensagem caso consiga ou caso não consiga fazer a conexão
Dockerfile->Irão instalar as dependências e irá executar o client.py