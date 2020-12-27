from flask import Flask
from flask_app.config import Configuration
# from .posts.blueprint import posts


app = Flask(__name__)

app.config.from_object(Configuration)
# app.register_blueprint(posts, url_prefix='/blog')


