import nltk
caesar = nltk.corpus.gutenberg.words('shakespeare-caesar.txt')
hamlet = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
print(hamlet[:400])