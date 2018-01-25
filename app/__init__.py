import json
from flask import Flask, render_template, request
from app.libraries import Listogram, Stochastic, Markov, RandomWords

# Initialize application
app = Flask(__name__, static_folder=None)


@app.route("/")
def hello():
    num_words = int(request.args.get('words'))
    rnd_wrds = RandomWords(num_words)

    return render_template("index.html", sentence=str(rnd_wrds))


# /generate-sentence?words=5
@app.route("/generate-sentence")
def generate_sentence():
    num_words = int(request.args.get('words'))

    rnd_wrds = RandomWords(num_words)

    return str(rnd_wrds)


@app.route("/markov-sentense")
def listogram():
    m = Markov("one fish two fish red fish blue fish".split())

    return m.generate_a_sentence()


@app.route("/person")
def person_route():
    person = {"name": "Eliel", 'age': 23}
    json_person = json.dumps(person)
    return (json_person, 200, None)
