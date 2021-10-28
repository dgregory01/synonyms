import argparse

import synonyms.find_synonyms as s

# e.g.: python synonyms/cli.py --w hello
parser = argparse.ArgumentParser(prog='synonyms',
                                 description='Return a list of synonyms')

parser.add_argument('--word',
                    metavar='word',
                    type=str,
                    help='The word to find synonyms for')

args = parser.parse_args()

word = args.word

find_synonyms = s.FindSynonyms(s.THESAURUS_BASE_URL)

synonyms = find_synonyms.get_synonyms(word)

print(f'Synonyms for: {word}')

for synonym in synonyms:
    print(synonym)
