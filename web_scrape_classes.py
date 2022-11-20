class LinkContent:
    def __init__(self, link: str, content: str) -> None:
        self.__link: str = link
        self.__content: str = content
        
    def __str__(self):
        return f"Link: {self.__link}\n\n{self.__content}"
        
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