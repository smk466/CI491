from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def determine_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio() > 0.5

def main():
    name = 'christopher lee'
    email = 'christopherlee@gmail.com'
    print(f'Is it similar: {determine_similarity(name, email)}')
    print(f'Similarity ratio: {similar(name, email)}')

if __name__ == '__main__':
    main()