from dataclasses import dataclass, field
       
# Person objects will contain name, email, position, and the link it was from (more will probably be implemented like phone numbers) 
@dataclass
class Person:
    name: str
    email: str
    phone: str
    specialty: str
    link: str

# LinkContent objects will contain link and content both in string
@dataclass
class LinkContent:
    link: str
    content: str
    personList: list[Person] = field(default_factory=list)

@dataclass
class LinkScraped:
    link: str
    personList: list[Person]