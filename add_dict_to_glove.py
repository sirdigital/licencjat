from glove import Glove, Corpus
from gensim import utils, corpora, matutils, models
import os

corpus_file_name = ''

wiki = models.word2vec.LineSentence(corpus_file_name)
id2word = corpora.Dictionary(wiki)
id2word.filter_extremes(keep_n=30000)
word2id = dict((word, id) for id, word in id2word.iteritems())

# Filter all wiki documents to contain only those 30k words.
filter_text = lambda text: [word for word in text if word in word2id]
filtered_wiki = lambda: (filter_text(text) for text in wiki)  # generator


corpus = Corpus()

corpus.fit(filtered_wiki(), window=10)

HERE = os.path.dirname(os.path.dirname(__file__))
PS_FILE = os.path.join(HERE, "glove_default_30k.model")

glove = Glove.load(PS_FILE)

glove.add_dictionary(corpus.dictionary)

glove.save('glove_default_30k_with_dict.model')