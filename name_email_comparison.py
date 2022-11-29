from difflib import SequenceMatcher
from web_scrape_classes import Person
import jellyfish

nameList: list = ["Chris Bryant", "Michael Jordan", "Michael Jackson", "Kobe Bryant"]
emailList: list = ["C.Bryant@gmail.com","Kobe.B@gmail.com","Mich.Jackson@gmail.com","Mich.Jordan@gmail.com"]

nameList2: list = ["Khalid Salem", "Mutasem Salem"]
emailList2: list = ["kjs426@drexel.edu", "ms4268@drexel.edu"]


def compareLists(nameList: list[str], emailList: list[str], link: str) -> tuple[list[tuple], list[Person]]:
    matchList: list = []
    finalPersonList: list[Person]
    for name in nameList:
        threshold: float = .30
        emailMatched: str = ''
        for email in emailList[:]:
            temp = jellyfish.jaro_winkler_similarity(name, email.split("@")[0])
            if temp > threshold:
                threshold = temp
                emailMatched = email
                #emailList.remove(emailMatched)
        match = (name, emailMatched)
        matchList.append(match)
    # print(matchList)
    finalList: list = iterate_each_tuple(matchList)
    finalPersonList = [Person(personTuple[0], personTuple[1], "WIP", "WIP", link) for personTuple in finalList]
    return finalList, finalPersonList

def iterate_each_tuple(matchList: list) -> list[tuple]:
    email: str
    emailsMatched, emailsNotMatched = get_emails_that_are_matched(matchList)
    returnList: list[tuple] = []
    emailsChecked: list = []
    for emailTuple in emailsMatched:
        email = emailTuple[1]
        if email in emailsChecked:
            continue
        returnList.append(determine_most_likely_match(emailsMatched, email))
        emailsChecked.append(email)
    returnList.extend(emailsNotMatched)
    return returnList

# def iterate_each_tuple(matchList: list) -> list[tuple]:
#     email: str
#     emailsMatched: list = get_emails_that_are_matched(matchList)
#     returnList: list[tuple] = []
#     emailsChecked: list = []
#     for emailTuple in emailsMatched:
#         email = emailTuple[1]
#         #print(f"Email in tuple: {email}")
#         if email in emailsChecked:
#             #emailsMatched.pop(emailsMatched.index(emailTuple))
#             continue   
#         returnList.append(determine_most_likely_match(emailsMatched, email))
#         emailsChecked.append(email)
#         #emailsMatched.pop(emailsMatched.index(emailTuple))
#     return returnList

"""
1. Get all tuples that both names and emails are matched (Done)
2. Get each duplicated emails that are matched with different names (Done)
3. Determine each similarity and get the highest ratio by using SequenceMatcher (Done)
4. Return the tuple with the highest ratio (Done)
"""
    
def get_name_email_similarity_ratio(name: str, email: str) -> float:
    return jellyfish.jaro_winkler_similarity(name, email.split("@")[0])
    
def get_emails_that_are_matched(matchList: list) -> list:
    emailsMatched: list = []
    emailsNotMatched: list = []
    for item in matchList:
        email = item[1]
        if (email == ""):
            emailsNotMatched.append(item)
            continue
        emailsMatched.append(item)
    return emailsMatched, emailsNotMatched

def determine_most_likely_match(emailsMatched: list[tuple], email: str) -> tuple:
    mostLikelyMatch: list = [""]
    highestRatio: float = 0.0
    for matchTuple in emailsMatched:
        if matchTuple[1] != email:
            continue
        if get_name_email_similarity_ratio(matchTuple[0], matchTuple[1]) > highestRatio:
            #print(f"mostLikelyMatch: {mostLikelyMatch}")
            mostLikelyMatch[0] = matchTuple
            highestRatio = get_name_email_similarity_ratio(matchTuple[0], matchTuple[1])
            #emailsMatched.pop(emailsMatched.index(matchTuple))
            #print(f"Highest ratio: {highestRatio}")
    return mostLikelyMatch[0]

compareLists(nameList, emailList)

# print(similar("Apple", "Bapple"))

# print(compareLists(["Ben Adams  Associate"], ["chiang@purdue.edu"]))
# print(get_name_email_similarity_ratio("Ben Adams  Associate", "benjamin.adams@canterbury.ac.nz"))