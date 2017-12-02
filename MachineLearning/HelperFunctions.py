from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.tag import pos_tag


import CleaningFunctions as c
import FilterFunctions as f

def make_wordBank(text):
    clean = cleaner(text)
    noExtraWords = f.unified_word_filter(clean)
    wordBank = lemmatizer(noExtraWords)
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




