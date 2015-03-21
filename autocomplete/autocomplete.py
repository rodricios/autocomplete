from collections import Counter

from . import models

from . import helpers

#the so called "Hidden" step, thus allowing this module to be
#a "Hidden Markov Model"... Whatever that means...
NEARBY_KEYS = {
    'a': 'qwsz',
    'b': 'vghn',
    'c': 'xdfv',
    'd': 'erfcxs',
    'e': 'rdsw',
    'f': 'rtgvcd',
    'g': 'tyhbvf',
    'h': 'yujnbg',
    'j': 'uikmnh',
    'k': 'iolmj',
    'l': 'opk',
    'm': 'njk',
    'n': 'bhjm',
    'o': 'iklp',
    'p': 'ol',
    'q': 'wa',
    'r': 'edft',
    's': 'wedxza',
    't': 'rfgy',
    'u': 'yhji',
    'v': 'cfgb',
    'w': 'qase',
    'x': 'zsdc',
    'y': 'tghu',
    'z': 'asx'
    }


def this_word(word, top_n=10):
    """given an incomplete word, return top n suggestions based off
    frequency of words prefixed by said input word"""
    try:
        return [(k, v) for k, v in models.WORDS_MODEL.most_common()
                if k.startswith(word)][:top_n]
    except KeyError:
        raise Exception("Please load predictive models. Run:\
                        \n\tautocomplete.load()")


predict_currword = this_word


def this_word_given_last(first_word, second_word, top_n=10):
    """given a word, return top n suggestions determined by the frequency of
    words prefixed by the input GIVEN the occurence of the last word"""

    #Hidden step
    possible_second_words = [second_word[:-1]+char
                             for char in NEARBY_KEYS[second_word[-1]]
                             if len(second_word) > 2]

    possible_second_words.append(second_word)

    probable_words = {w:c for w, c in
                      models.WORD_TUPLES_MODEL[first_word.lower()].items()
                      for sec_word in possible_second_words
                      if w.startswith(sec_word)}

    return Counter(probable_words).most_common(top_n)


predict_currword_given_lastword = this_word_given_last


def predict(first_word, second_word, top_n=10):
    """given the last word and the current word to complete, we call
    predict_currword or predict_currword_given_lastword to retrive most n
    probable suggestions.
    """

    try:
        if first_word and second_word:
            return predict_currword_given_lastword(first_word,
                                                   second_word,
                                                   top_n=top_n)
        else:
            return predict_currword(first_word, top_n)
    except KeyError:
        raise Exception("Please load predictive models. Run:\
                        \n\tautocomplete.load()")


def split_predict(text, top_n=10):
    """takes in string and will right split accordingly.
    Optionally, you can provide keyword argument "top_n" for
    choosing the number of suggestions to return (default is 10)"""
    text = helpers.norm_rsplit(text, 2)
    return predict(*text, top_n=top_n)
