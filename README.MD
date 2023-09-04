pip install SQLAlchemy 			    #ORM BASE para a lib Flask-SQLAlchemy
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