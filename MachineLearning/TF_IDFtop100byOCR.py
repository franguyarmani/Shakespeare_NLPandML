import math
import os
import collections

import Utilities as u

arff = open("TF_IDFtop100byOCR.arff", 'w')
scenesPath = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/Scenes"

os.chdir(scenesPath)

def build_occurences(vocabulary, Path):
    d = dict.fromkeys(vocabulary, 0)
    for filename in os.listdir(Path):
        text = u.prepare_text(filename)
        for w in vocab:
            if (w in text):
                d[w] += 1
    return d    

def build_weights(vocabulary, ocr):
    d = dict.fromkeys(vocabulary, 0)
    for w in vocabulary:
        d[w] = math.log10(nDocs/ocr[w])
    return d




words = u.build_vocabulary(scenesPath)
vocab = list(words.keys())
occurences = build_occurences(vocab, scenesPath)
nDocs = len(os.listdir(scenesPath))
weights = build_weights(vocab, occurences)

top100 = (collections.Counter(occurences)).most_common(100)
print(len(top100))


arff.write("@RELATION scenes\n")
for word, weight in top100:
    arff.write("@Attribute " + word + " REAL\n")
arff.write("@ATTRIBUTE Tragedy {Tragedy, Comedy}\n")
arff.write("@DATA\n")
for filename in os.listdir(scenesPath):
    sceneWords = u.prepare_text(filename)
    vector = u.build_vector(sceneWords, list(words.keys()))

    if(filename[0] == "t"):
        for word, weight in top100:
            arff.write(str(vector[word]*weights[word])+",")
        arff.write("Tragedy\n")
    else:
        for word, weight in top100:
            arff.write(str(vector[word]*weights[word])+",")
        arff.write("Comedy\n")
arff.close()    
