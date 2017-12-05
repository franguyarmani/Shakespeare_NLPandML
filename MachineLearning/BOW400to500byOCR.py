import os
import string
import Utilities as u
import collections

arff = open("BagOfWord400to500byOCR.arff", 'w')
scenesPath = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/Scenes"

os.chdir(scenesPath)

def build_vocabulary(Path):
    for filename in os.listdir(scenesPath):
        for w in u.prepare_text(filename):
            words[w] = 1

words = u.build_vocabulary(scenesPath)
vocab = list(words.keys())
occurences = u.build_occurences(vocab, scenesPath)
top500 = (collections.Counter(occurences)).most_common(500)


arff.write("@RELATION BagOfWord400to500byOCR\n")
for word, OCR in top500[400:499]:
    arff.write("@Attribute " + word + " REAL\n" )
arff.write("@ATTRIBUTE Tragedy {Tragedy, Comedy}\n")
arff.write("@DATA\n")
for filename in os.listdir(scenesPath):
    sceneWords = u.prepare_text(filename)
    vector = u.build_vector(sceneWords, list(words.keys()))
    if(filename[0] == "t"):
        for word, weight in top500[400:499]:
            arff.write(str(vector[word])+",")
        arff.write("Tragedy\n")
    else:
        for word, weight in top500[400:499]:
            arff.write(str(vector[word])+",")
        arff.write("Comedy\n")
arff.close()    






