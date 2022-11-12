import unittest
from find_names_and_emails import identify_email

class TestIdentifyEmail(unittest.TestCase):
    
    def test_with_regular_email_one(self) -> None:
        email: str = "alam@purdue.edu"
        self.assertTrue(identify_email(email))
        
    def test_with_regular_email_two(self) -> None:
        email: str = "allebach@ecn.purdue.edu"
        self.assertTrue(identify_email(email))
        
    def test_with_regular_email_three(self) -> None:
        email: str = "chair-computer-engineering@sjsu.edu"
        self.assertTrue(identify_email(email))
        
    def test_with_combined_text(self) -> None:
        email: str = "chair rod fatoohi chair-computer-engineering@sjsu.edu"
        self.assertTrue(identify_email(email))
        
        
        
        