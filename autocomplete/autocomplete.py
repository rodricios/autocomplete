"""autocomplete - or How to "suggest" the completion of an unfinished word
using a simple conditional probability model.

written by Rodrigo Palacios
rodrigopala91@gmail.com

find me on GitHub or twitter:
http://github.com/rodricios
http://twitter.com/rodricios
- Copyright 2015

Notes:

There are two works that have greatly inspired this Python module.

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

import re
import collections


WORDS = []

WORD_TUPLES = []

WORDS_MODEL = {}

WORD_TUPLES_MODEL = {}

#http://norvig.com/spell-correct.html
def re_split(text): return re.findall('[a-z]+', text.lower())

def norm_rsplit(text,n): return text.lower().rsplit(' ', n)[-n:]

#http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
#https://github.com/rrenaud/Gibberish-Detector/blob/master/gib_detect_train.py#L16
def chunks(l, n):
    for i in range(0, len(l) - n + 1):
        yield l[i:i+n]

#This step is where we transform "raw" data
# into some sort of probabilistic model(s)
def train(corpus):
    """takes in a preferably long string, split that string -> list,
    we \"chunk\" (partition) -> list -> list of 2-elem list,
    create dictionary, where each key = first elem;
        each value = Counter([second elems])
    """

    # word is in WORDS
    global WORDS
    WORDS = re_split(corpus)

    global WORDS_MODEL
    WORDS_MODEL = collections.Counter(WORDS)

    # wordA, wordB are in WORDS
    global WORD_TUPLES
    WORD_TUPLES = list(chunks(WORDS, 2))

    #P(wordA|wordB)
    global WORD_TUPLES_MODEL
    WORD_TUPLES_MODEL = {first:collections.Counter() for first, second in WORD_TUPLES}

    for tup in WORD_TUPLES:
        try:
            WORD_TUPLES_MODEL[tup[0]].update([tup[1]])
        except:
            pass

    #save for next use. pickle format: (key=model name, value=model)
    pickle.dump({'words_model': words_model,
                'word_tuples_model': WORD_TUPLES_MODEL},
                open('./models_compressed.pkl', 'wb'))

def quick_train():
    """try to load models"""
    try:
        models = pickle.load(open('./models_compressed.pkl','rb'))

        global WORDS_MODEL
        WORDS_MODEL = models['words_model']

        global WORD_TUPLES_MODEL
        WORD_TUPLES_MODEL = models['word_tuples_model']

        return true
    except IOError, KeyError:
        return False


def predict_currword(word,top_n=10):
    """given a word, return top n suggestions based off frequency of words
    prefixed by said input word"""
    try:
        return [(k,v) for k,v in WORDS_MODEL.most_common() if k.startswith(word)]
    except KeyError:
        return word


def predict_currword_given_lastword(word_1, word_2,top_n=10):
    """given a word, return top n suggestions determined by the frequency of
    words prefixed by the input GIVEN the occurence of the last word"""
    return collections.Counter( { w:c for w, c in WORD_TUPLES_MODEL[word_1.lower()].items()
                    if w.startswith(word_2.lower())} ).most_common(top_n)


def predict(text,top_n = 10):
    """given some text, we [r]split last two words (if possible) and call
    predict_currword or predict_currword_given_lastword to retrive most n
    probable suggestions.
    """
    text = norm_rsplit(text,2)

    if len(text) > 1:
        return predict_currword_given_lastword(*text,top_n=top_n)
    else:
        return predict_currword(text[0],top_n)


if __name__ == "__main__":
    """load the classic Norvig big.txt corpus"""
    if not quick_train():
        train('./big.txt')
