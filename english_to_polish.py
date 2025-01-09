##
# The user enters a word in English from the keyboard. The program displays the translation 
# of the word or information that the translation is unavailable.
##

translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

i = input('Enter an english word: ')

if i in translations:
    print(f'The translation of {i} is {translations[i]}')
else:
    print('Translation for this word is unavailable at the moment.')