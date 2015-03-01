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
