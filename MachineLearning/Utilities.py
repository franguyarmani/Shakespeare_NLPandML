
def build_vector(textList, vocabulary):
    d = dict.fromkeys(vocabulary, 0)
    for w in textList:
        d[w] += 1
    return d

def prepare_text(name):
    f = open(name, 'r')
    text = f.read()
    f.close()
    return text.split(" ")

def build_vocabulary(Path):
    d = {}
    for filename in os.listdir(scenesPath):
        for w in u.prepare_text(filename):
            d[w] = 1
    return d
