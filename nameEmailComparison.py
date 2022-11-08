from difflib import SequenceMatcher

nameList = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList = ["C.Bryant@gmail.com","Kobe.Br@gmail.com","Mich.Jackson@gmail.com","Mich.Jordan@gmail.com"]

nameList2 = ["Khalid Salem", "Mutasem Salem"]
emailList2 = ["kjs426@drexel.ed", "ms4268@drexel.edu"]


def compareLists(nameList, emailList):
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



compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))