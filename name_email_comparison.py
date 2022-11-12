from difflib import SequenceMatcher

nameList: list = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList: list = ["C.Bryant@gmail.com","Kobe.Br@gmail.com","Mich.Jackson@gmail.com","Mich.Jordan@gmail.com"]

nameList2: list = ["Khalid Salem", "Mutasem Salem"]
emailList2: list = ["kjs426@drexel.ed", "ms4268@drexel.edu"]


def compareLists(nameList: list[str], emailList: list[str]) -> list[str]:
    matchList: list = []
    for name in nameList:
        threshold = .30
        emailMatched = ''
        for email in emailList[:]:
            temp = SequenceMatcher(lambda threshold: threshold == " ", name, email.split("@")[0]).ratio()
            if temp > threshold:
                threshold = temp
                emailMatched = email
                #emailList.remove(emailMatched)
        match = (name, emailMatched)
        matchList.append(match)
    finalList: list = determine_most_likely_match(matchList)
    return finalList        

def determine_most_likely_match(matchList: list) -> list[tuple]:
    email: str
    emailsMatched: list = get_emails_that_are_matched(matchList)
    returnList: list = []
    emailsChecked: list = []
    for emailTuple in emailsMatched:
        email = emailTuple[1]
        print(f"Email in tuple: {email}")
        if email in emailsChecked:
            continue   
        mostLikelyMatch: list = [""]
        highestRatio: float = 0.0
        for matchTuple in emailsMatched:
            if matchTuple[1] != email:
                continue
            if get_name_email_similarity_ratio(matchTuple[0], matchTuple[1]) > highestRatio:
                print(f"mostLikelyMatch: {mostLikelyMatch}")
                mostLikelyMatch[0] = matchTuple
                highestRatio = get_name_email_similarity_ratio(matchTuple[0], matchTuple[1])
                print(f"Highest ratio: {highestRatio}")
        emailsChecked.append(email)
        returnList.append(mostLikelyMatch[0])

    """
    1. Get all tuples that both names and emails are matched (Done)
    2. Get each duplicated emails that are matched with different names (Done)
    3. Determine each similarity and get the highest ratio by using SequenceMatcher (Done)
    4. Return the tuple with the highest ratio (Done)
    """

    return returnList
    
def get_name_email_similarity_ratio(name: str, email: str) -> float:
    return SequenceMatcher(None, name, email.split("@")[0]).ratio()
    
def get_emails_that_are_matched(matchList: list) -> list:
    emailsMatched: list = []
    for item in matchList:
        email = item[1]
        if (email == ""):
            continue
        emailsMatched.append(item)
    return emailsMatched

#compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))