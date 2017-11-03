import string
def remove_all_caps(dirtyList):
    cleanList = []
    for word in dirtyList:
        if len(word) < 2 or not word.isupper():
            cleanList.append(word)
    return cleanList

def remove_punctandnums(dirtyList):
    cleanList = []
    for word in dirtyList:
        if word not in string.punctuation:
            cleanList.append(word)
    return cleanList

def remove_directions_brackets(rawText):
    cleanString = rawText
    while cleanString.find('[') != -1:
        start = cleanString.find('[')
        end = cleanString.find(']')
        front = cleanString[:start-1]
        back = cleanString[end+1:]
        cleanString = front+back
    return cleanString