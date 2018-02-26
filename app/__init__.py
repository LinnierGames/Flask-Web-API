from flask import Flask, render_template, request, redirect
from app.libraries import Listogram, Stochastic, Markov, RandomWords, OrderedMarkovChain
import twitter
import random

# Initialize application
app = Flask(__name__, static_folder=None)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<int:order>")
def set_markov_order(order):
    with app.open_resource('book.txt') as f:
        corpus = f.read()

    nth_markov = OrderedMarkovChain(corpus, order)

    return redirect('/')


list_random = []


@app.route("/random-sentence")
def generate_sentence():
    num_words = int(random.randint(0, 50))
    rnd_wrds = RandomWords(num_words)
    list_random.insert(0, rnd_wrds)

    return render_template("table.html", title="Random Sentences", data=list_random)


list_markov = []


corpus = "one fish two fish red fish blue fish"


nth_markov = OrderedMarkovChain(corpus, 1)


@app.route("/markov-chain")
def markov():
    corpus = request.args.get("corpus")
    m = None
    if corpus is not None:
        m = Markov(corpus.split())
    else:
        m = Markov("one fish two fish red fish blue fish".split())
    sentence = m.generate_a_sentence()
    list_markov.insert(0, sentence)

    return render_template("table.html", title="Markov Chain", data=list_markov)


@app.route('/tweet', methods=['POST'])
def tweet():
    status = nth_markov.generate_a_sentence()

    print(twitter.tweet(status).text)

    return redirect('/')


# @app.route("/person")
# def person_route():
#     person = {"name": "Eliel", 'age': 23}
#     json_person = json.dumps(person)
#     return (json_person, 200, None)
