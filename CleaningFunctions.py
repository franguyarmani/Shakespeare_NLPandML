
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