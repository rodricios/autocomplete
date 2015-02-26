import os
from unittest import TestCase



class TestLoadWordsModel(TestCase):
    def test_load_models(self):
        import autocomplete

        is_loaded = autocomplete.load()
        self.assertTrue(is_loaded)


    def test_WORDS_MODEL_not_loaded(self):
        from collections import Counter

        from autocomplete import models

        self.assertFalse(len(models.WORDS_MODEL.keys()) > 0)

    def test_WORD_PAIRS_MODEL_not_loaded(self):
        from autocomplete import models

        self.assertFalse(len(models.WORD_TUPLES_MODEL.keys()) > 0)


"""
class TestGetXPathFrequencyDistribution(TestCase):
    def test_is_tuple(self):
        url = 'http://en.wikipedia.org/wiki/Google'
        sent_xpath_pairs = get_sentence_xpath_tuples(url)

        xpaths = [x for (_, x) in sent_xpath_pairs]
        max_path = get_xpath_frequencydistribution(xpaths)[0]
        self.assertTrue(isinstance(max_path, tuple))


class TestExtractArticleText(TestCase):
    def test_is_string(self):
        url = 'http://en.wikipedia.org/wiki/Google'
        text = extract(url)
        self.assertTrue(isinstance(text, basestring))


class TestRegexSplitVariousEndingsInHTML(TestCase):
    def setUp(self):
        self.file = open(RE_SPLIT_VARIOUS_ENDINGS_FILENAME, 'r')

    def tearDown(self):
        self.file.close()

    def test_splits_regex(self):
        sent_xpath_pairs = get_sentence_xpath_tuples(self.file)
        num_of_splits = len(sent_xpath_pairs)
        self.assertEqual(num_of_splits, 9, "\nrequired number of splits: 9\n" +
                         "actual number of splits:   " + str(num_of_splits))


class TestRegexSplitDotEndingsInHTML(TestCase):
    def setUp(self):
        self.file = open(RE_SPLIT_DOT_ENDINGS_FILENAME, 'r')

    def tearDown(self):
        self.file.close()

    def test_splits_regex(self):
        sent_xpath_pairs = get_sentence_xpath_tuples(self.file)
        num_of_splits = len(sent_xpath_pairs)
        self.assertEqual(num_of_splits, 9, "\nrequired number of splits: 9\n" +
                         "actual number of splits:   " + str(num_of_splits))
"""
