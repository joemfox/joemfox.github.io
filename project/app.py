# -*- coding: utf-8 -*-
import os
import yaml
from flask import Flask
# from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
# pages = FlatPages(app)
freezer = Freezer(app)

projects = yaml.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/projects.yaml')))
