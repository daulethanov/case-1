from service import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

#SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@database:5432/db2'

#SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@database:5432/dbname'
