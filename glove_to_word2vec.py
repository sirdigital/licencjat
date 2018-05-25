import glove
import pprint
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fit a GloVe model.')

import os

HERE = os.path.dirname(os.path.dirname(__file__))
PS_FILE = os.path.join(HERE, "glove_default_30k.model")

glove = glove.Glove.load(PS_FILE)

parser = argparse.ArgumentParser(description='Fit a GloVe model.')

parser.add_argument('--query', '-q', action='store',
                    default='',
                    help='Get closes words to this word.')
args = parser.parse_args()

pprint.pprint(glove.most_similar(args.query, number=10))

