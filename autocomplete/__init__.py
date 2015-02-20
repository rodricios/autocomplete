import os

from bottle import route, run, request

import models

import autocomplete

"""load the classic Norvig big.txt corpus"""
"""
print("training!")

if not models.load_models():
    #print(os.listdir(os.curdir))
    with open(os.path.join(os.path.dirname(__file__), 'big.txt'),'rb') as f:
        print(os.listdir(os.curdir))
        models.train_models(str(f.read()))

print("done training!")
"""

def run_server(port_num=8080):
    if not models.load_models():
        #print(os.listdir(os.curdir))
        with open(os.path.join(os.path.dirname(__file__), 'big.txt'),'rb') as f:
            print(os.path.join(os.path.dirname(__file__), 'big.txt'))
            models.train_models(str(f.read()))

    @route('/<wordA>/<wordB>')
    def index(wordA, wordB):
        return  dict(autocomplete.predict(wordA, wordB))

    run(host='localhost', port=port_num)


if __name__ == "__main__":
    """load the classic Norvig big.txt corpus"""
    print("training!")

    if not models.load_models():
        #print(os.listdir(os.curdir))
        with open(os.path.join(os.path.dirname(__file__), 'big.txt'),'rb') as f:
            print(os.path.join(os.path.dirname(__file__), 'big.txt'))
            models.train_models(str(f.read()))

    print("done training!")
