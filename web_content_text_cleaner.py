"""
TODO
This will clean the texts before searching names with spacy as spacy can't fully recognize
the texts directly from the extracted web contents

This script will run after web_content_retrieve.py and before find_names_and_emails.py

Plan to do:
1. Remove new lines in each link content
2. Remove any special characters in content text
3. Try to eliminate any combined texts
"""