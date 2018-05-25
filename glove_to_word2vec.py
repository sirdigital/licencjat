import glove
import pprint
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fit a GloVe model.')


glove = glove.Glove.load('glove_default_30k.model')

parser = argparse.ArgumentParser(description='Fit a GloVe model.')

parser.add_argument('--query', '-q', action='store',
                    default='',
                    help='Get closes words to this word.')
args = parser.parse_args()

pprint.pprint(glove.most_similar(args.query, number=10))