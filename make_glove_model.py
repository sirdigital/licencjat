from gensim import utils, corpora, matutils, models
import glove

# Restrict dictionary to the 30k most common words.
corpus_file_name = ''

wiki = models.word2vec.LineSentence(corpus_file_name)
id2word = corpora.Dictionary(wiki)
id2word.filter_extremes(keep_n=30000)
word2id = dict((word, id) for id, word in id2word.iteritems())

# Filter all wiki documents to contain only those 30k words.
filter_text = lambda text: [word for word in text if word in word2id]
filtered_wiki = lambda: (filter_text(text) for text in wiki)  # generator

# Get the word co-occurrence matrix -- needs lots of RAM!!
cooccur = glove.Corpus()
cooccur.fit(filtered_wiki(), window=10)

# and train GloVe model itself, using 10 epochs
model_glove = glove.Glove(no_components=600, learning_rate=0.05)
model_glove.fit(cooccur.matrix, epochs=10)

model_glove.save('glove_default_30k.model')