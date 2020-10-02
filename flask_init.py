from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import constants

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = constants.KAMANIM_SQLITE_DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
