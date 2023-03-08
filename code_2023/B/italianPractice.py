import random

# oldItalian = ["io sono", "tu sei", "lui / lei e", "noi siamo", "voi siete", "loro sono",
#                 "io ho", "tu hai", "lui / lei ha", "noi abbiamo", "voi avete", "loro hanno",
#                 "io voglio", "tu voui", "lui / lei vuole", "noi vogliamo", "voi volete", "loro vogliono",]

# OldEnlish = ["i am", "you are", "he / she is", "we are", "you all are", "they are",
#                  "i have", "you have", "he / she has", "we have", "you all have", "they have",
#                  "i want", "you want", "he / she wants", "we want", "you all want", "they want",]

englishList = [
                 "i do", "you do", "he / she does", "we do", "you all do", "they do",
                 "i say", "you say", "he / she says", "we say", "you all say", "they say"]

italianList = [
                "io faccio", "tu fai", "lui / lei fa", "noi facciamo", "voi fate", "loro fanno",
                "io dico", "tu dici", "lui / lei dice", "noi diciamo", "voi dite", "loro dicono"]

while True:
    randomIndex = random.randint(0, len(englishList) - 1)
    print("English |", englishList[randomIndex])
    input()
    print("Italian |", italianList[randomIndex], "\n\n")
