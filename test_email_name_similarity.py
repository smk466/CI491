from difflib import SequenceMatcher
from names_dataset import NameDataset, NameWrapper

nd = NameDataset()
nameDictionary = {}

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def determine_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio() > 0.5

def sort_dataset_names_to_dictionary():
    alphabetKeysList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nameFromDatasetList = nd.get_top_names(gender = 'Male', country_alpha2='US').get('US').get('M') + nd.get_top_names(gender = 'Female', country_alpha2='US').get('US').get('F')
    #print(nameFromDatasetList)
    for letter in alphabetKeysList:
        currentLetterList = []
        for name in nameFromDatasetList:
            #print(name[:1])
            if name[:1] == letter:
                currentLetterList.append(name)
                nameFromDatasetList.remove(name)
                #print(len(nameFromDatasetList))
        if len(currentLetterList) > 0:
            nameDictionary[letter] = sorted(currentLetterList)

def main():
    name = 'christopher lee'
    email = 'christopherlee@gmail.com'
    sort_dataset_names_to_dictionary()
    #print(f'Is it similar: {determine_similarity(name, email)}')
    #print(f'Similarity ratio: {similar(name, email)}')
    #print(nd.get_top_names(country_alpha2='US').get('US').get('M'))
    print(nameDictionary)

if __name__ == '__main__':
    main()