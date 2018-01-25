import os
import json
from flask import Flask, request
from app.libraries import Listogram, Stochastic, Markov

# Initialize application
app = Flask(__name__, static_folder=None)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/markov-sentense")
def listogram():
    m = Markov("one fish two fish red fish blue fish".split())

    return m.generate_a_sentence()


@app.route("/person")
def person_route():
    person = {"name": "Eliel", 'age': 23}
    json_person = json.dumps(person)
    return (json_person, 200, None)
