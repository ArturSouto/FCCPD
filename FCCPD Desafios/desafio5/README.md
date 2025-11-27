Na pasta gateway o app.py irá servir como uma central que vai receber requisições do app.py(que esta na pasta order) e no app.py(que esta na pasta user)

Na pasta order o app.py vai fornecer informações de pedidos organizadas, pegando informações que está na app.py(que está na pasta user)

na pasta user o app.py vai fornecer uma lista de usuários

Todos os Dockerfile vão preparar o ambiente da aplicação

Todos os requirements.txt, ao rodar, instalar tudo que for necessário para a aplicação

`docker-compose up`     

Irá mostrar tudo que aparece no app.py do gateway http://localhost:8080/

Irá mostrar tudo que aparece no app.py do user http://localhost:8080/users

Irá mostrar tudo que aparece no app.py do orders http://localhost:8080/orders