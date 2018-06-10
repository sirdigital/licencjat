from pyplwnxml import PlwnxmlParser

wordnet_location = '/Users/dawidbodych/Downloads/plwordnet_3_0/plwordnet-3.0.xml'
wordnet = PlwnxmlParser(wordnet_location).read_wordnet()

fname = '/Users/dawidbodych/dane_cloud/most_common_words.txt'


def get_synonyms(word):
    synonyms = []
    lemmas = wordnet.lemma(word)
    for i in range(len(lemmas)):
        for lu in lemmas[i].synsets[0].lexical_units:
            if lu.name != word:
                synonyms.append(lu.name)

    synonyms_final = [word] + [s for s in synonyms if len(s.split(' ')) == 1] +\
                     [s.split(' ')[0] for s in synonyms if len(s.split(' ')) > 1]

    return list(set(synonyms_final))


with open(fname) as f:
    content = f.readlines()

content = [x.strip().split(' ')[1] for x in content]

list_results = []

for word in content:
    list_results.append(get_synonyms(word))

file = open("synonyms.txt", "w")

for line in list_results:
    file.write(",".join(line))
    file.write('\n')

file.close()
