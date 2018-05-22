from multiprocessing import Pool
import treetaggerwrapper
from interruptingcow import timeout


def process_file(out_file_name):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='pl')
    f = open(out_file_name + '.txt', 'r')
    w = open(out_file_name + '_lemmatized.txt', 'w')
    i = 0
    wrong_pos = ['SENT', 'interp']

    for line in f:
        try:
            with timeout(5, exception=RuntimeError):
                tags = tagger.tag_text(line)
                tag_list = []

                tags2 = treetaggerwrapper.make_tags(tags)

                for tag in tags2:
                    if tag.pos not in wrong_pos:
                        tag_list.append(tag.lemma)

                w.write(' '.join(tag_list) + '\n')

                i += 1
                if i % 100:
                    print(i)

        except RuntimeError:
            continue


def main():
    file_names = ['raw_corpus_' + str(i) for i in range(1, 9)]
    p = Pool()
    p.map(process_file, file_names)

if __name__ == '__main__':
    main()
