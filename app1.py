import json
from difflib import get_close_matches
data = json.load(open('data.json'))
def translate(wrd):
    wrd = wrd.lower()
    if wrd in data:
        return data[wrd]
    elif len(get_close_matches(wrd, data.keys())) > 0:
        yn = input('Did yo mean %s instead ? Press Y for yes and N for No: ' % get_close_matches(wrd, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(wrd, data.keys())[0]]
        elif yn == 'N':
            return "Word Not Exists"
        else:
            return 'Wrong Entry'

    else:
        return 'No Such word is present in Dictionary'


word = input('Enter word: ')
value = translate(word)
if type(value) == list:
    for item in value:
        print(item)
else:
    print(value)