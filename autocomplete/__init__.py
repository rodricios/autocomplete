import os

import bottle

from bottle import route, run, request, template, view

import autocomplete

from autocomplete import predict, predict_currword

"""load the classic Norvig big.txt corpus"""

def run_server(port_num=8080):

    autocomplete.models.load_models()
    bottle.debug(True)

    @route('/<wordA>/<wordB>')
    def index(wordA, wordB):
        return  dict(autocomplete.predict(wordA, wordB))

    @route('/bigcorpus')
    @view('bigcorpus')
    def bigcorpus():
        return {'suggestions':autocomplete.models.WORDS_MODEL}

    run(host='localhost', port=port_num)


def load():
    """load the classic Norvig big.txt corpus"""
    print("training!")

    autocomplete.models.load_models()

    print("done training!")

    return True
