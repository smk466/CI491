import unittest

import spacy
from spacy.language import Language
from spacy.tokens import Doc, Span

from find_names_and_emails import is_the_name_in_name_dictionary

class TestVerifyByNameDictionary(unittest.TestCase):

    def test_normal_names(self):
        name: Span = "daniel wlinna"
        english_nlp: Language = spacy.load('en_core_web_sm')
        spacy_parser: Doc = english_nlp("daniel wlinna")
        self.assertTrue(is_the_name_in_name_dictionary(spacy_parser[0]))

    def test_individual_names_first(self):
        name = "daniel"
        english_nlp: Language = spacy.load('en_core_web_sm')
        spacy_parser: Doc = english_nlp("daniel")
        self.assertTrue(is_the_name_in_name_dictionary(spacy_parser[0]))

    def test_individual_names_middle(self):
        name = "wlinna"
        spacy_parser: Doc = self.english_nlp(name)
        self.assertFalse(is_the_name_in_name_dictionary(spacy_parser.ents[0]))

    def test_individual_names_last(self):
        name = "jrhanliu"
        spacy_parser: Doc = self.english_nlp(name)
        self.assertFalse(is_the_name_in_name_dictionary(spacy_parser.ents[0]))

    def test_individual_names_last_combined(self):
        name = "jrhanliuassociate"
        spacy_parser: Doc = self.english_nlp(name)
        self.assertFalse(is_the_name_in_name_dictionary(spacy_parser.ents[0]))

    def test_names_without_spaces(self):
        name = "daniel wlinna jrhanliuassociate"
        spacy_parser: Doc = self.english_nlp(name)
        self.assertFalse(is_the_name_in_name_dictionary(spacy_parser.ents[0]))


