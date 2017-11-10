import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import reuters
from nltk import bigrams, trigrams

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

from collections import Counter, defaultdict
import re
import random

import CleaningFunctions as c

#=====================The Corpus======================

corpus_root = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(corpus_root, '.*.txt')


#==================Build Text================
text = ""
for file_id in plays.fileids():
    text += plays.raw(file_id)


# #=================Clean Text============                             #This is what I used to remove stage directions
# f = open('QuickClean.txt', 'w')                                      #and line queues however it took a long time so
# noBrackets = c.remove_directions_brackets(text)                      #I ran it once and loaded it into a text 
# noDirections = c.remove_directions_space(noBrackets)
# noAbrvNames = c.remove_abrv_names(noDirections)
# f.write(noAbrvNames)
# print ('directions removed')
# f.close()


# cleanText = noAbrvNames
# test = re.compile('[A-Z]*[A-Z]{4}\.')
# match = test.search(cleanText)
# cuts = []
# iter = 0
# f = open('DeepClean.txt', 'w') 
# while match != None:
#     start = match.start()
#     end = match.end()
#     cuts.append(cleanText[start:end])
#     cleanText = c.splice(start, end, cleanText)
#     match = test.search(cleanText)
# f.write(cleanText)
# print(cuts)
# f.close()



#=================Tokenize===================
f = open("DeepClean.txt", 'r')
cleanText = f.read()
tempList = cleanText.split()
cleanText = " ".join(tempList)
sentences = nltk.sent_tokenize(cleanText)

#==============Generate Model===============
model = defaultdict(lambda: defaultdict(lambda: 0))
for sentence in sentences:
    lst = sentence.split()
    for w1, w2 in bigrams(lst, pad_right=True, pad_left=True):
        model[w1][w2] += 1
 

for w1 in model:
    total_count = float(sum(model[w1].values()))
    for w2 in model[w1]:
        model[w1][w2] /= total_count


#==============Generag Text=============



iter = 0 
while iter <= 10:
    text = [None]
    sentence_finished = False
    while not sentence_finished:
        r = random.random()
        accumulator = .0
 
        for word in model[text[-1]].keys():
            accumulator += model[text[-1]][word]
 
            if accumulator >= r:
                text.append(word)
                break
 
        if text[-1:] == [None]:
            sentence_finished = True
    print (' '.join([t for t in text if t]))
    iter += 1
