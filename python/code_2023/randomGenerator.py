import random as r
import string

def main():
    """acts as an orchestrator for the entire program"""

    lowercaseList = list(string.ascii_lowercase)
    uppercaseList = list(string.ascii_uppercase)
    bothCaseList = list(string.ascii_uppercase) + list(string.ascii_lowercase)

    dataTypeLettersUpper, dataTypeLettersLower, dataTypeLettersBoth = getStringType() # error on this line

    generationList = addParametersToList(dataTypeLettersUpper, dataTypeLettersLower, dataTypeLettersBoth, uppercaseList, lowercaseList, bothCaseList)

    getStringLength(generationList)


def getStringType():
    """gets the data type, str, int, str + int.."""

    dataTypeLetters = input("Include Letters?")
    if dataTypeLetters == "yes" or dataTypeLetters == "y":
        dataTypeLetters = input("Upper, Lower, or Both?")
    elif dataTypeLetters == "no" or dataTypeLetters == "n":

        if dataTypeLetters == "upper":
            dataTypeLettersUpper = True

        elif dataTypeLetters == "Lower":
            dataTypeLettersLower = True

        elif dataTypeLetters == "both":
            dataTypeLettersBoth = True

        return dataTypeLettersUpper, dataTypeLettersLower, dataTypeLettersBoth

    # dataTypeNumbers = input("Include Numbers?")
    # if dataTypeNumbers == "yes" or dataTypeNumbers == "y":
    #     dataTypeNumbers == True

    # dataTypeSpecial = input("Include Special Characters?")
    # if dataTypeSpecial == "yes" or dataTypeSpecial == "y":
    #     dataTypeSpecial == True


def addParametersToList(dataTypeLettersUpper, dataTypeLettersLower, dataTypeLettersBoth, uppercaseList, lowercaseList, bothCaseList):
    """Adds the True parameters to a list the random generator can grab from"""

    if dataTypeLettersUpper:
        generationList = generationList.append(uppercaseList)

    elif dataTypeLettersLower:
        generationList = generationList.append(lowercaseList)

    elif dataTypeLettersBoth:
        generationList = generationList.append(bothCaseList)

    return generationList


def getStringLength(generationList):
    """gets the amount of characters to be generated"""

    generatedString = r.choice(generationList)
    print(generatedString)


def generateString():
    """generates the random string sequence"""


def outputFunction():
    """outputs the final sequence"""

if __name__ == "__main__":
    main()