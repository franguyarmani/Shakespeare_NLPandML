from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer 
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
