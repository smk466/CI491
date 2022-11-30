from dataclasses import dataclass
       
# Person objects will contain name, email, position, and the link it was from (more will probably be implemented like phone numbers) 
@dataclass
class Person:
    name: str
    email: str
    phone: str
    position: str
    link: str

# LinkContent objects will contain link and content both in string
@dataclass
class LinkContent:
    link: str
    content: str

@dataclass
class LinkScraped:
    link: str
    personList: list[Person]