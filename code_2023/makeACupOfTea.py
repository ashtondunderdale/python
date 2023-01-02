def makeCupOfTea():
    """makes a cup of tea"""

    water = getWater()
    teabag = getTeabag()
    milk = getMilk()
    sugar = getSugar()
    cup = getCup()
    spoon = getSpoon()
    kettle = getKettle()

    boilingWater = boilWater(water, kettle)
    cupOfWater = pourWater(boilingWater, cup)
    cupWithTea = addTeabag(cupOfWater, teabag)
    cupWithSqueezedTea = squeezeTeabag(teabag, cupWithTea, spoon)
    cupOfTeaWithRemovedTeabag = removeTeabag(cupWithSqueezedTea, spoon, teabag)
    cupOfTeaAndMilk = addMilk(milk, cupOfTeaWithRemovedTeabag)
    cupOfTeaAndMilkAndSugar = addSugar(sugar, cupOfTeaAndMilk, spoon)
    cupOfTea = stirTea(spoon, cupOfTeaAndMilkAndSugar)

    drinkTea(cupOfTea)


def getWater(tap):
    """gets water"""

    return "water"

def getTeabag(teabagJar):
    """gets a tea bag"""

    return "tea bag"

def getMilk(Fridge):
    """gets milk"""

    return "milk"

def getSugar(sugarJar):
    """gets sugar"""

    return "sugar"

def getCup(Cupboard):
    """gets a cup"""

    return "cup"

def getSpoon(Drawer):
    """gets a spoon"""

    return "spoon"

def getKettle(Counter):
    """gets kettle"""

    return "kettle"



def boilWater(water):
    """boils water"""

    return "boiling water"

def pourWater(boilingWater, cup):
    """pours the boiling water"""

    return "cup of boiling water"

def addTeabag(cupOfWater, teabag):
    """adds a teabag to the cup"""

    return "cup with teabag"


def squeezeTeabag(teabag, cupWithTea, spoon):
    """soaks the teabag in the water"""

    return "cup of tea soaked water"

def removeTeabag(cupWithSqueezedTea, spoon, teabag):
    """remove teabag from the cup"""

    return "cup of tea soaked water without teabag"

def addMilk(milk, cupOfTeaWithRemovedTeabag):
    """adds milk to the tea"""

    return "cup of tea and milk"

def addSugar(sugar, cupOfTeaAndMilk, spoon):
    """adds sugar to thge tea""" 

    return "cup of tea, milk, and sugar"

def stirTea(spoon, cupOfTeaAndMilkAndSugar):
    """stirrs the milk and tea"""

    return "cup of tea"


def drinkTea(cupOfTea):
    """drinks the tea"""

    print("*slurp*")


makeCupOfTea()