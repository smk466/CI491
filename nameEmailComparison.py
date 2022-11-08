from difflib import SequenceMatcher

nameList = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList = ["C.Bryant@gmail.com","Kobe.Br@gmail.com","Mich.Jackson@gmail.com","Mich.J@gmail.com"]


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def compareLists(nameList, emailList):
    for i in nameList:
        x = 0
        email = ''
        for j in emailList:
            temp = SequenceMatcher(lambda x: x == " ", i, j.split("@")[0]).ratio()
            if temp > x:
                x = temp
                email = j   
        print(i,"---",email,"---",x)        

compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))