from difflib import SequenceMatcher
import jellyfish

nameList: list = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList: list = ["C.Bryant@gmail.com","Kobe.B@gmail.com","Mich.Jackson@gmail.com","Mich.Jordan@gmail.com"]

nameList2: list = ["Khalid Salem", "Mutasem Salem"]
emailList2: list = ["kjs426@drexel.edu", "ms4268@drexel.edu"]


def compareLists(nameList: list[str], emailList: list[str]) -> list[str]:
    list = []
    for i in nameList:
        x = 0.60
        email = ''
        for j in emailList:
            # temp = SequenceMatcher(lambda x: x == " ", i, j.split("@")[0]).ratio()
            temp = jellyfish.jaro_winkler_similarity(i, j.split("@")[0])
            if temp > x:
                x = temp
                email = j   
        match = (i, email) 
        # print(match, temp)
        list.append(match)   

    return list        



compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))