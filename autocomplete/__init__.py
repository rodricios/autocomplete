"""autocomplete - or How to "suggest" the completion of an unfinished word
using a simple conditional probability model.

written by Rodrigo Palacios
rodrigopala91@gmail.com

find me on GitHub or twitter:
http://github.com/rodricios
http://twitter.com/rodricios
- Copyright 2015

Notes:

There are two works that have greatly inspired this and my last Python modules.

The first work is by Peter Norvig, a Director of Research @ Google (according
to his wiki page):

How to Write a Spelling Corrector:
http://norvig.com/spell-correct.html

I also suggest watching his lecture The Unreasonable Effectiveness of Data:
https://www.youtube.com/watch?v=yvDCzhbjYWs

The second is by Rob Renaud who states (in his project's README) that he also
felt inspired and challenged by Peter Norvig's lecture.

rrenaud's Gibberish-Detector:
https://github.com/rrenaud/Gibberish-Detector

Finally, the implied challenge issued by Norvig is to try to come up with a
simple solution to some problem using lots of data. He [probabilistically]
solved the spell-checker problem by using text he found within his computer (not
pulled from the internet). This data is contained within big.txt (6mb). I borrow
this corpus, as did Renaud; you will likely see a lot of similarities between
mine, Renaud's, and Norvig's Python projects. That's the point. Please feel
free to send me any questions and comments to my email: rodrigopala91@gmail.com

Cheers,
Rodrigo
"""

from bottle import route, run, debug

from autocomplete import models

from .autocomplete import predict

def run_server(port_num=8080):
    """little demo server for demo'ing sake"""
    models.load_models()

    debug(True)

    @route('/<first_word>/<second_word>')
    def index(first_word, second_word):
        return dict(predict(first_word, second_word))

    run(host='localhost', port=port_num)


def load():
    """load the classic Norvig big.txt corpus"""
    print("training!")

    models.load_models()

    print("done training!")

    return True

