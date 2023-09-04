# Projeto Concessionária MVC 
  
  
**Indice**
[TOCM]
  
- [Projeto Concessionária MVC](#projeto-concessionária-mvc )
  - [Primeiros passos:](#primeiros-passos )
  - [Comandos](#comandos )
  
## Primeiros passos:
  
Para utilização desse projeto é necessario ter o [python instalado](https://www.python.org/ ) após a instalação do python seguir os passos da [instalação do FLASK e da maquina virtual](https://flask.palletsprojects.com/en/2.3.x/installation/
) que é basicamente escolher um local para salvar o projeto e executar os comando 1 e 2 na parte [Comandos](##Comandos )
## Comandos
  
  
1. python3 -m venv .venv    
Comando cria uma pasta .venv que tem um executavel para sua maquina virtual
obs.: as vezes o python não consegue encontrar o pacote na maquina virtual é so sair da maquina virtual e instalar a biblioteca diretamente na sua maquina 
2. .venv\Scripts\activate
Esse comando dentro da pasta do seu projeto permite você executar um CMD da sua maquina virtual onde você vai instalar as bibliotecas.
obs.: as vezes o python não consegue encontrar o pacote na maquina virtual é so sair da maquina virtual e instalar a biblioteca diretamente na sua maquina 
3. pip install Flask
Instalar o Flask na maquina virtual
4. pip install SQLAlchemy 	
ORM BASE para a lib Flask-SQLAlchemy 
  
  
pip install -U Flask-SQLAlchemy 	#ORM Usado para facilitar a conexão com o banco de dados assim como tbm proteger de SQL INJECTIOn
  
  
pip install mysqlclient 		    #Usado Para Conexão SQL
  
  
pip install Flask-Migrate 		    #Usado Para MIgração
  
  
  
flask db init                       # Inicializar a pasta migração
  
  
flask db migrate -m 'comments'      # Cria migração para o BD
  
  
flask db upgrade                    # Subi a migração para o BD
  
  
flask run #Rodar o APP
  
  
Tutoriais
https://www.youtube.com/watch?v=rqv8u31NZo8&list=PLAmj9NJfPKQZXEoa_4J4um_YB7VXK736J&index=1
https://plainenglish.io/blog/flask-crud-application-using-mvc-architecture#the-project-structure
  
Documentações
  
  
Flask
https://flask.palletsprojects.com/en/2.3.x/installation/
https://flask.palletsprojects.com/en/2.3.x/quickstart/
k
  
Flask Migrate
https://flask-migrate.readthedocs.io/en/latest/index.html
SqlAlchemy
  
  
https://docs.sqlalchemy.org/en/20/intro.html#installation
https://docs.sqlalchemy.org/en/20/core/types.html
  
  
Flask SqlAlchemy
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
  
  
Jinja2 ## Linguagem operacional front end framework python nativo do flask
https://jinja.palletsprojects.com/en/2.10.x/
  
  
StackOverFlow
https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip
  