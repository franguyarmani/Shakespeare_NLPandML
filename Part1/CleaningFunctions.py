import string
import re


#---------------Raw Text Cleaners---------------
def remove_directions_brackets(rawText): #Safe to use on all plays
    cleanString = rawText
    while cleanString.find('[') != -1:
        start = cleanString.find('[')
        end = cleanString.find(']')
        cleanString = splice(start, end, cleanString)
    return cleanString

def remove_directions_space(rawText): #tested for as you like it, Caesar, 
    #use a regular expresison to find space before direction and return after
    cleanString = rawText
    dir1 = re.compile('\S {8}.+\n| {20}.+\n')
    match = dir1.search(cleanString)
    directions = []
    while match != None:
        start = match.start()
        end = match.end()
        directions.append(cleanString[start:end])
        cleanString = splice(start, end, cleanString)
        match = dir1.search(cleanString)
    return cleanString

def remove_abrv_names(rawText): #Safe to run on Hamlet, King Lear, MacBeth, Much Ado, Othello,
    cleanString = rawText
    test = re.compile('\n *[A-Z][a-z]{2}\.|\n *[A-Z][a-z]{3}\.|\n *[A-Z][a-z]{4}\.')
    match = test.search(cleanString)
    cuts = []
    while match != None:
        start = match.start()
        end = match.end()
        cuts.append(cleanString[start:end])
        cleanString = splice(start, end, cleanString)
        match = test.search(cleanString)
    return cleanString

#--------------List Cleaners--------------
def remove_all_caps(dirtyList):
    cleanList = []
    for word in dirtyList:
        if (len(word) < 2 or not word.isupper()):
            cleanList.append(word)
    return cleanList

def remove_punctandnums(dirtyList):
    cleanList = []
    for word in dirtyList:
        if word not in string.punctuation and not word.isdigit() :
            cleanList.append(word)
    return cleanList







#++++++++++Helper Funcitons++++++++++++
def splice(index1, index2, String):
    front = String[:(index1-1)]
    back = String[(index2+1):]
    newString = front+back
    return newString
