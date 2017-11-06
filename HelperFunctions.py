from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.tag import pos_tag
import CleaningFunctions as c


def cleaner(rawText):
    noBrackets = c.remove_directions_brackets(rawText)
    noDirections = c.remove_directions_space(noBrackets)
    noNames = c.remove_abrv_names(noDirections)
    tokenized = WordPunctTokenizer().tokenize(noNames)
    noCaps = c.remove_all_caps(tokenized)
    noPunct = c.remove_punctandnums(noCaps)
    lemmatized = lemmatizer(noPunct)
    return lemmatized

def lemmatizer (List):
    LemList = []
    for word in List:
        LemList.append(WordNetLemmatizer().lemmatize(word))
    return LemList

def remove_nouns(List):
    nounFree = []
    for word in List:
        lst = pos_tag(word)
        tup = lst[0]
        pos = tup[1]
        if pos != 'NNP':
            nounFree.append(word)
    return nounFree
            


