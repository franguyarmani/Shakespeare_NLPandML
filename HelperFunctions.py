from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.tag import pos_tag
import CleaningFunctions as c

def make_wordBank(listOfTexts):
    wordBank = []
    for text in listOfTexts:
        clean = h.cleaner(text)
        lemmatized = h.lemmatizer(clean)
        noPropNouns = h.remove_Pnouns(lemmatized)
        wordBank.extend(noPropNouns)
    return wordBank


def cleaner(rawText):
    noBrackets = c.remove_directions_brackets(rawText)
    noDirections = c.remove_directions_space(noBrackets)
    noNames = c.remove_abrv_names(noDirections)
    tokenized = WordPunctTokenizer().tokenize(noNames)
    noCaps = c.remove_all_caps(tokenized)
    cleanList = c.remove_punctandnums(noCaps)
    return cleanList

def lemmatizer (List):
    lemList = []
    for word in List:
        lemList.append(WordNetLemmatizer().lemmatize(word))
    return lemList

def remove_Pnouns(List):
    nounFree = []
    for word in List:
        lst = pos_tag(word)
        tup = lst[0]
        pos = tup[1]
        if pos != 'NNP':
            nounFree.append(word)
    return nounFree
            


