from flask import Flask
from flask_migrate import Migrate
from python_p4_flask_sqlalchemy import create_app, db  # Replace 'python_p4_flask_sqlalchemy' with your actual package name

app = create_app()
migrate = Migrate(app, db)

