import os
import string
import Utilities as u

arff = open("TF_IDF.arff", 'w')
scenesPath = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/Scenes"

os.chdir(scenesPath)

def build_vocabulary(Path):
    d = {}
    for filename in os.listdir(scenesPath):
        for w in u.prepare_text(filename):
            d[w] = 1
    return d

words = u.build_vocabulary(scenesPath)
vocab = list(words.keys())
arff.write("@RELATION scenes\n")
for word in vocab:
    arff.write("@Attribute " + word + " REAL\n" )
arff.write("@ATTRIBUTE Tragedy {Tragedy, Comedy}\n")
arff.write("@DATA\n")
for filename in os.listdir(scenesPath):
    sceneWords = u.prepare_text(filename)
    vector = u.build_vector(sceneWords, list(words.keys()))
    if(filename[0] == "t"):
        for word in vocab:
            arff.write(str(vector[word])+",")
        arff.write("Tragedy\n")
    else:
        for word in vocab:
            arff.write(str(vector[word])+",")
        arff.write("Comedy\n")
arff.close()    






