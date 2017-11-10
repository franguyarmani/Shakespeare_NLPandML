from nltk.corpus import stopwords
from nltk.tag import pos_tag



def remove_stopwords(List):
    cleanList = []
    for word in List:
        if word not in stopwords.words('english'):
            cleanList.append(word)
    return cleanList



def remove_Pnouns(List):
    nounFree = []
    for word in List:
        lst = pos_tag(word)
        tup = lst[0]
        pos = tup[1]
        if pos != 'NNP':
            nounFree.append(word)
    return nounFree
            
def unified_word_filter(List): #combination of remove_Pnouns and remove stop_words for efficiency
    noExtra = []
    for word in List:
        lst = pos_tag(word)
        tup = lst[0]
        pos = tup[1]
        if pos != 'NNP' and word not in stopwords.words('english') and word not in m.Undesirable :
            noExtra.append(word)
    return noExtra
            


