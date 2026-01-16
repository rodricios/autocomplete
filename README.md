*Autocomplete* or: How I learned to stop spelling and love our AI overlords
===

## Note from the author

If you're a user of `autocomplete` or any other one of my projects ([eatiht](https://github.com/rodricios/eatiht), [libextract](https://github.com/datalib/libextract)), I humbly ask that you check out my new project **[wxpath](https://github.com/rodricios/wxpath)**: a declarative web crawler and scraper that extends the [XPath](https://en.wikipedia.org/wiki/XPath) DSL to navigate and scrape web pages. 

**wxpath** is a natural progression of my work of web data extraction and I am very excited to share it with you.

## Autocomplete

Autocomplete is a simple tool that implements a [conditional probability](http://en.wikipedia.org/wiki/Conditional_probability) model to achieve a [spell checker](http://en.wikipedia.org/wiki/Spell_checker). 

For those short on time, the [ELI5](#explain-like-im-5) section is devoid of nomenclature but lengthy; the [tl;dr](#tldr) section describes the implementation using the appropriate terms - basic principles of conditional probability, generalized [Markov chain](http://en.wikipedia.org/wiki/Markov_chain) - but is short, concise, and includes references for further reading. 

## Skip to:

* [How to's](#how-to-install)
* [New: Spell Correction](#spell-correction)
* [tl;dr?](#tldr)
* [Motivation](#motivation)
* [Explanation](#explanation)

---

## How to install:

    pip install autocomplete

## How to use:

```python
import autocomplete

# load pickled python Counter objects representing our predictive models
# I use Peter Norvigs big.txt (http://norvig.com/big.txt) to create the predictive models
autocomplete.load()

# imagine writing "the b"
autocomplete.predict('the','b')

[('blood', 204),
 ('battle', 185),
 ('bone', 175),
 ('best', 149),
 ('body', 149),
 ...]

# now you type an "o"

autocomplete.predict('the','bo')

[('bone', 175),
 ('body', 149),
 ('bones', 122),
 ('boy', 46),
 ('bottom', 32),
 ('box', 24),
 ...]
```

### Spell Correction

Now say you are in the process of typing "body" (with a preceding "the")

```python

autocomplete.predict('the','bo')

[('bone', 175),
 ('body', 149),
 ('bones', 122),
 ('boy', 46),
 ('bottom', 32),
 ('box', 24),
 ...]

```

And then you make the fatal error of typing an "f" instead of a "d"

```python

autocomplete.predict('the','bof')

[('body', 149),
 ('bottom', 32),
 ('borzois', 16),
 ('bottle', 13),
 ('bodies', 13),
 ('border', 12)
 ...]

```

Relax! Autocomplete has you covered. Using a simple ["fat-finger"](http://en.wikipedia.org/wiki/Fat-finger_error) error model,
you can rest assured that you won't be making [six-hundred billion dollar mistakes](http://www.bbc.com/news/business-29454265) at your Japanese investment firm.


If you have your own language model in the form described in [ELI5](#explain-like-im-5), then use the *models* submodule to call the training method:

```python
from autocomplete import models

models.train_models('some giant string of text')

```

Want to run it as a server (bottlepy required)?

```python
import autocomplete

autocomplete.run_server()

#output
Bottle v0.12.8 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.

```

Now head over to http://localhost:8080/the/bo

```
http://localhost:8080/the/bo
#output
{"body": 149, "box": 24, "bottom": 32, "boy": 46, "borzois": 16, "bodies": 13, "bottle": 13, "bones": 122, "book": 14, "bone": 175}

http://localhost:8080/the/bos
#output
{"boscombe": 11, "boston": 7, "boss": 1, "bosom": 5, "bosses": 4}
```

### Obligatory tests
```
python setup.py test
```


---

## [tl;dr](https://github.com/rodricios/autocomplete/blob/master/autocomplete/models.py)

The following code excerpt is my interpretation of a series of lessons/concepts expressed in a number of different books.

The unifying concept can be said to be [conditional probability](http://en.wikipedia.org/wiki/Conditional_probability):

    P(A , B) = P(B | A) * P(A)

Which can read as saying:

    The probability of A and B occuring is equal to the probability of B occuring, given that A has occured

More on this below.


```python

    # "preperation" step
    # for every word in corpus, normalize ('The' -> 'the'), insert to list
    WORDS = helpers.re_split(corpus)

    # first model -> P(word)
    # Counter constructor will take a list of elements and create a frequency distribution (histogram)
    WORDS_MODEL = collections.Counter(WORDS)

    # another preperation step
    # [a,b,c,d] -> [[a,b], [b,c], [c,d]]
    WORD_TUPLES = list(helpers.chunks(WORDS, 2))

    # second model -> P(next word | prev. word)
    # I interpret "..| prev. word)" as saying "dictionary key
    # leading to seperate and smaller (than WORDS_MODEL) freq. dist.
    WORD_TUPLES_MODEL = {first:collections.Counter() for first, second in WORD_TUPLES}

    for prev_word, next_word in WORD_TUPLES:
        # this is called the "conditioning" step where we assert
        # that the probability space of all possible "next_word"'s
        # is "conditioned" under the event that "prev_word" has occurred
        WORD_TUPLES_MODEL[prev_word].update([next_word])

```


The further develop this idea:

Assume you have a large collection of English-understandable text merged into a single string.

Start by transforming that string into a list of words (AKA *ngrams of word-legth*), and also (but not required) normalize each word ('The' -> 'the').

Once you have a normalized list of words, you can start building a frequency distribution measuring the frequency of each word.

...

At this point you can start "predict" the "final state" of a word-in-progress. But consider the case where a user types in some query box:

    "The th"

And he intends to write:

    "The third"

With the above predictive model, you'll be suggesting something like:

    [
        ('the', 80030),
        ('they', 3938),
        ('there', 2972),
        ...
    ]

This explains one specific type of predictive model, which can be written as P(word), and you've just seen the pitfalls of using **just** this model.

Now for the next word, ask yourself, what's the probability that I'm going to type the word "apple" given that I wrote "tasty"?

In machine learning and AI books, you'll be presented *Conditional Probability* with the following equation:

    P(word A and word B) = P(word B | word A) * P(word A)

That equation addresses the problem that I mentioned.

We've handled P(wordA) already.

To handle P(word B | word A), which reads *probability of word A given word B*, I take a *literal* interpretation of the word "given", in that context, to mean the following:

*"word A" is the key pointing to a probability distribution representing all the words that follow "word A"*

Once we can represent this second model, we can also apply the *filtering* step - given that we know more letters in the second word, we can zone in on more precise suggestions.

### Resources

Textbooks, and locations therein, where the concepts have been expressed:

I. [Intro to Statistical Natural Language Processing](http://ics.upjs.sk/~pero/web/documents/pillar/Manning_Schuetze_StatisticalNLP.pdf) - Manning, Schütze, 1999

    a. frequency distribution showing the most common words and frequencies in *Tom Sawyer*, pg. 21

    b. conditional probability definition expressed in page 42 - section 2.1.2

    c. the intuition for *frequency* distributions found in pg. 153 (provided in the context of finding [*Collocations*](http://en.wikipedia.org/wiki/Collocation))

II. [Probabilistic Graphical Models](http://mitpress.mit.edu/books/probabilistic-graphical-models) - Kohler, Friedman, 2009

    a. conditional probability definition found on pg. 18 (hilariously and coincidentally found in section 2.1.2.1)

III. [Artificial Intelligence - A Modern Approach](http://aima.cs.berkeley.edu) - Russell, Norvig, 3rd. ed. 2010

    a. conditional probability concept explained in pg. 485

    b. the "language" (I take to mean "intuition" for asserting things in the probabilistic sense) pg. 486

    c. the notion of "conditioning" found in pg. 492-494

## Motivation

Similar to the motivation behind [eatiht](https://github.com/rodricios/eatiht#motivation), I found that it took far too long to find a palpable theory-to-application example of simple predictive models. I hope you find this project to be useful in your own exploration of predictive models!