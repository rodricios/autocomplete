# Autocomplete Tutorial

*This work is dedicated to my siblings*

## Motivation

Similar to the motivation behind [eatiht](https://github.com/rodricios/eatiht#motivation), I found that it took far too long to find a palpable theory-to-application example of what amounts to more than a 500 pages of words across 3 books, each spanning a large index of, in certain cases, *counter-intuitive* nomenclature; read the [light criticisms](http://www.reddit.com/r/MachineLearning/comments/2fxi6v/ama_michael_i_jordan/ckep3z6) made by Michael I. Jordan on the matter (he was recently named [#2 machine learning expert "we need to know" on dataconomy.com](http://dataconomy.com/10-machine-learning-experts-you-need-to-know/)).

You can find similar thoughts being expressed [**in an article from 2008 (updated 2009)**](http://brenocon.com/blog/2008/12/statistics-vs-machine-learning-fight/) by [Brennan O'Connor](http://brenocon.com)

---

## Explain like I'm 5[*](#note-1)

*Warning! This explanation is literally intended for young kids - I'm actually trying to see if these concepts can be explained to an audience unaware of the nomenclature used within the statistical [nlp](http://en.wikipedia.org/wiki/Natural_language_processing) and other machine learning fields. For example, my 7, 9, 11, 14 y.o. siblings, and basically anyone else who's ever read a story to a child - they would be a part of the target audience.

If you've found this readable and informative, please consider putting on the goofiest face and reading this to your kids, if you have any :) If you do, please send me your thoughts on the experience.

I'm only interested in lowering the barrier to entry. I should have included this note since the beginning (sorry to those who undoubtedly left with a bad taste in their mouth).

You can contact me at rodrigopala91@gmail.com

Thanks for reading,

Rodrigo

## ELI5

No. I'm explaining this like you're 5. I know you're not *5* , *you guys... Chris, stop jumping on your sister's back*!

Ok, so I'm saying, *imagine I'm 5!*

Oh, that was easy now huh? Let's just forget the *I'm 5* part.

Imagine a giant collection of books.

For example, all the Harry Potter and Hunger Games novels put together.

What if I asked you to go through all the pages and all the words in those pages?

Now I'm not asking you *four* to actually *read* the books. You know, just go through, beginning to end, and notice each word.

For every new word you see, write it down, and put a "1" next to it, and everytime you see a word *again*, add "1" more to the previous number.

So basically I'm asking y'all to keep count of how many times a word comes up.

Got it? If yes, cool! If not, find a sibling, friend, or adult near you and ask them to help you out :)

...

Say you start with *Harry Potter and the Sorcerer's Stone*:

    Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much...

And imagine that you're on the 5th word. This or something close to this is what you're going for:

    Mr.     -> 1
    and     -> 1
    Mrs.    -> 1
    Dursley -> 1
    of      -> 1


Or if you're a *wannabe-Harry-Potter* fan, ah I'm just kidding!

If you started with *the-book-that-must-not-be-named* - I know you guys won't get it, but persons my age will :)

Alright! So you started with *The Hunger Games*:

    When I wake up, the other side of the bed is cold...

By the sixth word you have:

    When  -> 1
    I     -> 1
    wake  -> 1
    up    -> 1
    the   -> 1

You have a long day ahead of you...

...

*1,105,285 words later*

Now that you're done tallying up all those words, why not order all these words by the *number of times you've seen them*?

See you next week!

...

Back so soon? You should have gotten something like this:

    psst*, remember, the format is:
     word -> # of times the word appears

    'the' -> 80030
    'of'  -> 40025
    'and' -> 38313
    'to'  -> 28766
    'in'  -> 22050
    'a'   -> 21155
    'that'-> 12512
    'he'  -> 12401
    'was' -> 11410
    'it'  -> 10681
    ... there's a lot more words you've tallied up...


Those were the most common words.

Now on the *less-frequent* end, you'll find your words appearing not as often...

    ... 29137 words later.
    'przazdziecka' -> 1
    'disclosure'   -> 1
    'galvanism'    -> 1
    'repertoire'   -> 1
    'bravado'      -> 1
    'gal'          -> 1
    'ideological'  -> 1
    'guaiacol'     -> 1
    'expands'      -> 1
    'revolvers'    -> 1

Yeah Chris? Oh, 'what does *lez freekend*' mean? Um, so it means something like: *you probably won't hear or read that word very often.*

Now what if I asked you to help me find this word I'm looking for? And I know this word starts with the letters: 'th'.

I'm pretty sure you guys can do this much faster!

...

*5 minutes later!*

...

Not bad! You only had to go through 29157 unique words after all!


    'the'  -> 80030
    'that' -> 12512
    'this' -> 4063
    'they' -> 3938
    'there'-> 2972
    'their'-> 2955
    'them' -> 2241
    'then' -> 1558
    'these'-> 1231
    'than' -> 1206
    ... 229 words more...


239 words, still kind of lot though huh? And you know your big brother, he's too lazy to do this work *by hand* (*cough* program it up  *cough*) ;)

So the word I'm looking for is on the tip of my tongue. I think the next letter is "i".

*1 minute later*

    'this'     -> 4063
    'think'    -> 557
    'things'   -> 321
    'thing'    -> 303
    'third'    -> 239
    'thin'     -> 166
    'thinking' -> 137
    'thirty'   -> 123
    'thick'    -> 77
    'thirds'   -> 43
    ... 36 words more...


*I scan through the first 10 words.* Oh, I just remembered that the next letter is 'r'.

*You start taking out even more words.*

*10 seconds later.*

    'third'      -> 239
    'thirty'     -> 123
    'thirds'     -> 43
    'thirteen'   -> 32
    'thirst'     -> 13
    'thirteenth' -> 11
    'thirdly'    -> 8
    'thirsty'    -> 5
    'thirtieth'  -> 3
    'thirties'   -> 2

Aha, 'thirdly' was the word I was looking for! What, you never heard of the word "thirdly" before?

Now you might be saying to yourself, "*that's pretty cool!*", and you're right!

And you know what's cooler? *Making everyone's life a tiny bit easier* is! :)

But how can you do that with just *words*?

Aren't words boring and dull?

It's like all we do is talk, write, and think with *words*. I mean, how lame, I can't even describe to you this *autocomplete* thing-slash-idea-thing without having to write it out with *words*!

Ugh! I hate words!

*Whoah, wait a minute! That was not cool of me! Let's relax for a minute.*

Let's try to give an imaginary hug to the word-factory in our brains. That part of our brain works so hard, even when we don't ask it to. How nice of our brain to do that. Not!

What I'm trying to say is that sometimes it's not very nice for our brains to distract us, especially when we have homework or other, real-world problems like adult-homework.

...

So how about this:

As a mental exercise, let's just try to think about *what* the next sentence coming out of our own mouths *will be*[\*](#note-2).

Now if you're thinking about what will be coming out of my mouth, or out of your mouth, or your mouth, or your mouth, or your mouth, you're doing it wrong! (to readers who aren't one of my 4 younger siblings, that's how many I have).

Try your best to think about *what* the next sentence coming out of *your own* mouth will be.

...

Did you decide on your sentence? Good!

Now what if I asked you to give me two **good** reasons explaining *why* and *how* you chose the sentence you chose?

Wait, I can't even do that! Let's make it easier on ourselves. Let's try to only answer *why* and *how* we chose just the first word.

Still pretty hard huh?

If you thought it was pretty darn hard to give a *good and honest* reason as to why it is you chose the word you chose, it's alright. :)

But like all couch-scientists, let's just make a guess! My guess is: our brain is a **probabilistic machine**.

If you feel like you don't *get* what the word "probabilisitic" or "probability" means, sure you do! Just use the word "probably" in one of your sentences, but try to make some sense.

Ok, so what do I mean? Well, let's just consider the English language. Like most other things, the English language has rules.

The kind of rules that can be simplified down to:

1) "***something*** *action* ***something***".

2) Replace ***something***'s and ***action*** with words that make sense to you.

Fair enough, right?

Now imagine that your brain essentially has those rules "branded" or "recorded" into itself. Ok, so now I'm starting to not make much sense huh?

How about this? How many times have you heard,

"**Do** your **bed**!"

"**Brush** your **teeth**!"

"**Let's** get **food**!"

While each one of you guys may have not heard those *exact* sentences, what I'm trying to say makes sense right? *That you probably heard certain sentences more often than others?*

...

Now, imagine you could put "pause" right after the first word that comes out of your mouth.

Let's just say that first word is "the".

Now in the case that you stuttered for reasons outside your conscientious control (for example: "thhh thhe the"). No big deal, you meant to say "the", so let's *flatten* it to just that!

With that *word* said, what words do you *think* you might have said after it?

You might tell me, "*any word I want!*

Of course you could have! I bet you spent a millisecond thinking about whether or not the next word you were going to say was going to be: *guaiacol*.

I *know* because I thought about using that word too!

I can remember the first time I heard (or read) *guaiacol* like it was yesterday. I read it in some funky article on the internet. I found the word in a list of words that don't appear too often in the English language.

After I read it, I was able to fit *guaiacol* nicely into that part of my brain where I... uhh.. was... able... uhh...

Oh, you *know*, that place in my brain where I get to choose whether I want to say *the apple*, *the automobile*, *the austronaut*, etc.

...

Ok, so clearly I'm no brainician, and that may or may not be the way our brain works.

But even though that idea might be wrong, the idea itself sounds like a pretty darn good way of suggesting the next word or words somebody is trying to *type*.

What if you had a way to count the number of times you've heard "apple" said after the word "the"?

Ask yourself the same question, but now with the word "automobile" instead of "apple".

What if you had the time to think about every possible word that you've ever heard spoken after the word "the"? I'd say it might have looked something like this:

    Words you might have heard following the word "the" and the number of times you might have heard it

    'same'     -> 996
    'french'   -> 688
    'first'    -> 652
    'old'      -> 591
    'emperor'  -> 581
    'other'    -> 528
    'whole'    -> 500
    'united'   -> 466
    'room'     -> 376
    'most'     -> 373

    ... 9331 more words...

Not impressed with your brain yet? Let's continue this little thought experiment further.

Imagine that you just said "the", and you could put pause after the first *letter* of the next word out of your mouth: "h".

Real quick, think of the shortest amount of time you can think of. Think of the shortest *second* you can think of. Now shorter than that too.

At this point, you can't even call that length of time a *second*. But in that length of time, your brain may have just done this:

    Every word you've ever heard coming after the word "the":

    'house'   -> 284
    'head'    -> 117
    'hands'   -> 101
    'hand'    -> 97
    'horses'  -> 71
    'hill'    -> 64
    'highest' -> 64
    'high'    -> 57
    'history' -> 56
    'heart'   -> 55

And that brain you got did this realllllyyyyyy fast. Faster than Google, Bing, Yahoo and any other company can ever hope to beat. And your brain did this without even asking for your permission. I think our brains are trying to control us you guys, oh no!

...

Thanks for reading this far folks. Please go to the [afterword](#afterword) for some of the resources I've found useful in both building the intuition, and writing this article.

Also, if it's not too much to ask, consider following me or tweeting this to your friends and/or family, any support is appreciated :)

- [@rodricios](https://twitter.com/rodricios)

## If you're not 5

The basic idea is this:

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

---

## Afterword

notes: \*I have to give a shout out to [Sam Harris](https://twitter.com/SamHarrisOrg) for being, AFAIK, the first person or one of the firsts, in [wonderfully putting into words](https://www.youtube.com/watch?v=pCofmZlC72g#t=1144) what I've borrowed and slightly adapted for this writing. [I highly recommend his work](http://www.samharris.org/)

Another shoutout to [Peter Norvig](http://norvig.com) for inspiring me and probably many others with our own little "toy" programs. His *Occam's Razor* approach to problem solving will likely cause some confusion as it may appear that my work is an almost full on copy-paste of his [*How to Write a Spell Checker*](http://norvig.com/spell-correct.html)!

But I swear it's not! I actually I think I may have out-Norvig'ed Peter Norvig when it comes to describing [conditional probability](http://en.wikipedia.org/wiki/Conditional_probability): P(wordA & wordB) = P(wordB | wordA)\*P(wordA)

And another one to Rob Renaud's [Gibberish Detector](https://github.com/rrenaud/Gibberish-Detector). I, out of pure chance, ran into his project some time after running into Norvig's article. I can't describe *how much it helped* to intuitively understand what the heavy hitters of "AI" consider to be introductory material; this was greatly needed b/c at the time, I felt overwhelmed by my own desire to really understand this area, and everything else going on.

I do have a second article about this exact thing, only expressed differently (audience is non-programming), and it may or may not be posted soon! ~~Oh and the code too, that is if someone hasn't gotten to translating the above article to code before I can get to uploading the project :P I'm trying to get the kinks out of here and the code so it's simple, duh!~~

I dedicate this work to my sisters, Cat, Melissa and Christine, and my favorite brother, Christian :)

#### note 1

[go back](#explain-like-im-5)

*To avoid confusion, I wrote this section in the form of a letter to my younger siblings*

#### note 2

*I'm borrowing, what I consider, [one of the most beautiful thought experiments I've ever heard trying to describe one's self](https://www.youtube.com/watch?v=pCofmZlC72g#t=1144). I'm a big fan of Sam Harris's work. Highly recommend!
