from dataclasses import dataclass

# LinkContent objects will contain link and content both in string
@dataclass
class LinkContent:
    link: str
    content: str
       
# Person objects will contain name, email, position, and the link it was from (more will probably be implemented like phone numbers) 
@dataclass
class Person:
    name: str
    email: str
    phone: str
    position: str
    link: str