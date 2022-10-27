from difflib import SequenceMatcher

nameList = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList = ["C.Bryant@gmail.com","Kobeeeeee.B@gmail.com","Mich.Jackson@gmail.com","Mich.J@gmail.com"]


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def compareLists(nameList, emailList):
    for i in nameList:
        x = 0
        email = ''
        for j in emailList:
            temp = SequenceMatcher(None, i, j).ratio()
            if temp > x:
                x = temp
                email = j
        print(i,"---",email,"---",x)
        emailList.remove(email)        

compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))