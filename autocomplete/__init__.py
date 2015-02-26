import os

import bottle

from bottle import route, run, request, template, view

import autocomplete

from autocomplete import models

"""load the classic Norvig big.txt corpus"""

def run_server(port_num=8080):

    models.load_models()
    bottle.TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__),'views'))
    bottle.debug(True)

    @route('/<wordA>/<wordB>')
    def index(wordA, wordB):
        return  dict(autocomplete.predict(wordA, wordB))

    @route('/bigcorpus')
    @view('bigcorpus')
    def bigcorpus():
        return {'suggestions':models.WORDS_MODEL}

    run(host='localhost', port=port_num)


if __name__ == "__main__":
    """load the classic Norvig big.txt corpus"""
    print("training!")

    models.load_models()

    print("done training!")
