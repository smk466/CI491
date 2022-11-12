from difflib import SequenceMatcher

nameList: list = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList: list = ["C.Bryant@gmail.com","Kobe.Br@gmail.com","Mich.Jackson@gmail.com","Mich.Jordan@gmail.com"]

nameList2: list = ["Khalid Salem", "Mutasem Salem"]
emailList2: list = ["kjs426@drexel.ed", "ms4268@drexel.edu"]


def compareLists(nameList: list[str], emailList: list[str]) -> list[str]:
    list = []
    for i in nameList:
        x = .30
        email = ''
        for j in emailList:
            temp = SequenceMatcher(lambda x: x == " ", i, j.split("@")[0]).ratio()
            if temp > x:
                x = temp
                email = j   
        match = (i, email) 
        list.append(match)   

    return list        



#compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))