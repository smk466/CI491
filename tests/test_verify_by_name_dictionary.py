import unittest
from find_names_and_emails import verify_by_name_dictionary

class TestVerifyByNameDictionary(unittest.TestCase):

    def test_normal_names(self):
        verifiedNames = verify_by_name_dictionary("daniel wlinna")
        self.assertTrue(verifiedNames)

    def test_individual_names_first(self):
        verifiedNames = verify_by_name_dictionary("daniel")
        self.assertTrue(verifiedNames)

    def test_individual_names_middle(self):
        verifiedNames = verify_by_name_dictionary("wlinna")
        self.assertTrue(verifiedNames)

    def test_individual_names_last(self):
        verifiedNames = verify_by_name_dictionary("jrhanliu")
        self.assertTrue(verifiedNames)

    def test_individual_names_last_combined(self):
        verifiedNames = verify_by_name_dictionary("jrhanliuassociate")
        self.assertFalse(verifiedNames)

    def test_names_without_spaces(self):
        verifiedNames = verify_by_name_dictionary("daniel wlinna jrhanliuassociate")
        self.assertFalse(verifiedNames)

