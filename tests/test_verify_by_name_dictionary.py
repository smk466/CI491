import unittest
from find_names_and_emails import verify_by_name_dictionary

class TestVerifyByNameDictionary(unittest.TestCase):

    def test_normal_names(self):
        name = "daniel wlinna"
        verifiedNamesList = verify_by_name_dictionary(name)
        self.assertTrue(name in verifiedNamesList)

    def test_individual_names_first(self):
        name = "daniel"
        verifiedNamesList = verify_by_name_dictionary(name)
        self.assertTrue(name in verifiedNamesList)

    def test_individual_names_middle(self):
        name = "wlinna"
        verifiedNamesList = verify_by_name_dictionary(name)
        self.assertTrue(name in verifiedNamesList)

    def test_individual_names_last(self):
        name = "jrhanliu"
        verifiedNamesList = verify_by_name_dictionary(name)
        self.assertTrue(name in verifiedNamesList)

    def test_individual_names_last_combined(self):
        name = "jrhanliuassociate"
        verifiedNamesList = verify_by_name_dictionary(name)
        self.assertFalse(name in verifiedNamesList)

    def test_names_without_spaces(self):
        name = "daniel wlinna jrhanliuassociate"
        verifiedNamesList = verify_by_name_dictionary(name)
        self.assertFalse(name in verifiedNamesList)

