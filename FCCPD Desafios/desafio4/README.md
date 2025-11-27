Na parte do consumer tem o arquivo app.py que vai buscar do app.py (que está na pasta user) a lista de usuários e vai mostrar formatado

Dockerfile vai preparar o ambiente da aplicação

Na parte do user o app.py vai basicamente fornecer uma lista de usuários (de forma desorganizada) 

Dockerfile vai preparar o ambiente da aplicação

Ambos tem requirements.txt e, ao rodar, instalar tudo que for necessário para a aplicação



Tudo que esta no app.py da pasta consumer vai aparecer em `http://localhost:5002/combined` (aqui vai mostrar formatado a lista de usuários)

Tudo que esta no app.py da pasta user vai aparecer em `http://localhost:5001/users`