
import bottle
from bottle import route, run, debug
import autocomplete
from autocomplete import models, predict
models.load_models()
#autocomplete.load()
#autocomplete.run_server()


app = bottle.default_app()

@route('/')
def hello_world():
    #autocomplete.load()
    #autocomplete.run_server()
    return "Hello, world! Simple test to make sure if Docker is running fine"

@route('/<first_word>/<last_word>')
def hello_ml(first_word, last_word):
     return dict(predict(first_word,last_word))

if __name__ == "__main__":
    autocomplete.load()
    run(host="0.0.0.0", port=8000, debug=True, reloader=True)

