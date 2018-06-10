from pyplwnxml import PlwnxmlParser
# from gensim.models import KeyedVectors
import pandas as pd
import gensim
import adagram

wordnet_location = '/Users/dawidbodych/Downloads/plwordnet_3_0/plwordnet-3.0.xml'
wordnet = PlwnxmlParser(wordnet_location).read_wordnet()

# word_vectors = KeyedVectors.load_word2vec_format('/Users/dawidbodych/dane_cloud/word2vec_cbow_default.txt', binary=False)
# m = gensim.models.KeyedVectors.load_word2vec_format('/Users/dawidbodych/dane_cloud/fasttext_skipgram.vec')


def get_synonyms(word):
    synonyms = []
    lemmas = wordnet.lemma(word)
    for i in range(len(lemmas)):
        for lu in lemmas[i].synsets[0].lexical_units:
            if lu.name != word:
                synonyms.append(lu.name)

    synonyms_final = [s for s in synonyms if len(s.split(' ')) == 1] +\
                     [s.split(' ')[0] for s in synonyms if len(s.split(' ')) > 1]

    return set(synonyms_final)

def check_most_similar(word, synonyms):
    if len(synonyms) < 2:
        return {'word': word, 'len_syns': len(synonyms), 'synonyms': list(synonyms),
                'len_common': 0, 'similar': [], 'common': []}
    else:
        try:
            # similar = word_vectors.most_similar(positive=[word], topn=33)
            similar = m.wv.most_similar(positive=[word], topn=33)
        except KeyError:
            try:
                word = word.title()
                # similar = word_vectors.most_similar(positive=[word], topn=33)
                similar = m.wv.most_similar(positive=[word], topn=33)
            except KeyError:
                return {'len_syns': len(synonyms), 'synonyms': synonyms,
                        'len_common': 0, 'similar': [], 'common': []}

        similar_words = [t[0] for t in similar]

        common = list(set(similar_words)-(set(similar_words)-synonyms))

        return {'word': word, 'len_syns': len(synonyms), 'synonyms': list(synonyms),
                'len_common': len(common), 'similar': similar_words,
                'common': list(common)}


fname = '/Users/dawidbodych/dane_cloud/most_common_words.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip().split(' ')[1] for x in content]

list_results = []

for word in content:
    list_results.append(check_most_similar(word, get_synonyms(word)))

df = pd.DataFrame(list_results)

df.to_csv('fasttext_skipgram.csv', sep=';')
