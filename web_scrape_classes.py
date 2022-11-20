# LinkContent objects will contain link and content both in string
class LinkContent:
    def __init__(self, link: str, content: str) -> None:
        self.__link: str = link
        self.__content: str = content
        
    def __str__(self):
        return f"Link: {self.__link}\n\n{self.__content}\n\n"
        
    def display(self) -> None:
        print(f'Link: {self.__link}\n\n{self.__content}\n\n')

    @property        
    def link(self) -> str:
        return self.__link
    
    @property
    def content(self) -> str:
        return self.__content
    
    @link.setter
    def link(self, newLink: str) -> None:
        self.__link = newLink
    
    @content.setter
    def content(self, newContent: str) -> None:
        self.__content = newContent
       
# Person objects will contain name, email, position, and the link it was from (more will probably be implemented like phone numbers) 
class Person:
    def __init__(self, name: str, email: str, position: str, link: str) -> None:
        self.__name: str = name
        self.__email: str = email
        self.__position: str = position
        self.__link: str = link
        
    def __str__(self):
        return f"Person (name: {self.__name}, email: {self.__email}, position: {self.__position}, from link: {self.__link})"
        
    def display(self) -> None:
        print(f'Name: {self.__name}\nEmail: {self.__email}\nPosition: {self.__position}\nLink: {self.__link}\n\n')
        
    @property        
    def name(self) -> str:
        return self.__name
    
    @property        
    def email(self) -> str:
        return self.__email
    
    @property        
    def position(self) -> str:
        return self.__position

    @property        
    def link(self) -> str:
        return self.__link
    
    @name.setter
    def name(self, newName: str) -> None:
        self.__name = newName
        
    @email.setter
    def email(self, newName: str) -> None:
        self.__email = newName
        
    @position.setter
    def position(self, newPosition: str) -> None:
        self.__position = newPosition
    
    @link.setter
    def link(self, newLink: str) -> None:
        self.__link = newLink