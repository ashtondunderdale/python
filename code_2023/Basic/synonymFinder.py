from PyDictionary import PyDictionary # does not work
dictionary=PyDictionary()

word = input("Enter a word: ")
synonyms = dictionary.synonym(word)
if synonyms is None:
    print("Sorry, no synonyms found for the word")
else:
    print("Synonyms for the word '{}':".format(word))
    for i, syn in enumerate(synonyms[:3], start=1):
        print(i, syn)