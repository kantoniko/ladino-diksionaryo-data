#!/usr/bin/env python

import csv
import os
import re
import sys
import yaml
import copy


signs = {
    r'\(f\)': "female",
    r'\(m\)': "male",
    r'\(v\)': "verb",
    r'\(adj\.\)': "adjective",
    r'\(adj\.': "adjective",
    r'\(adv\.\)': "adverb",
    r'\(adv\)': "adverb",
    r'\(prep\.\)': "preposition",
    r'\([pP]ron\.\)': "pronoun",
}

accents = {
    'á': 'a',
    'í': 'i',
    'é': 'e',
    'ó': 'o',
    'ú': 'u',
    'ü': 'u',
}
words_regex = f"^[ a-zA-Z{''.join(sorted(accents.keys()))}.-]+(\.\.\.|!|\?)?$"


def remove_accent(ladino):
    ladino = re.sub(r'á', 'a', ladino)
    ladino = re.sub(r'í', 'i', ladino)
    ladino = re.sub(r'é', 'e', ladino)
    ladino = re.sub(r'ó', 'o', ladino)
    ladino = re.sub(r'ú', 'u', ladino)

    return ladino

def get_grammar_types():
    types = {
        "female": False,
        "verb": False,
        "adjective": False,
        "adverb": False,
        "preposition": False,
        "pronoun": False,
    }
    for sign, grammar_type in signs.items():
        regex = r'^(.*?)\s+' + sign + r'\s*$'
        match = re.search(regex, ladino)
        if match:
            types[grammar_type] = True
            ladino = match.group(1)

def _err(msg):
    print(f"ERROR {msg}", file=sys.stderr)

def save_words(all_words):
    with open("words.txt", "w") as fh:
        for word in all_words:
            print(word, file=fh)

def save_librelingo_format(dictionary):
    data = {
        'Two-way-dictionary': dictionary,
    }
    filename = "ladinokomunita.yaml"
    #print(data)
    with open(filename, 'w') as fh:
        fh.write("# This is a generated file. Do not edit manually!\n\n")
        fh.write("Skill:\n")
        fh.write("  Name: Ladinokomunita\n")
        fh.write("  Id: 10000\n\n")
        fh.write("New words: []\n")
        fh.write("Phrases: []\n\n")
        yaml.dump(data, fh, Dumper=yaml.Dumper, allow_unicode=True, indent=4)

def save_yaml_format(full):
    filename = "dictionary.yaml"
    data = {
        'words': full
    }
    with open(filename, 'w') as fh:
        yaml.dump(full, fh, Dumper=yaml.Dumper, allow_unicode=True, indent=4)

def _extract_words(word):
    if ',' in word:
        return re.split(r'\s*,\s*', word)
    else:
        return word

def main():
    #filename = "diksionario_biervos_excel_corrected.csv"
    filename = "biervos.csv"
    dictionary = []
    full = []
    all_words = set()
    with open(filename) as fh:
        # Palavra,Eshemplos,Espanyol,English,Turkish,Origen,id,Portuguese,French
        rd = csv.DictReader(fh, delimiter=',')

        count = 50
        for row in rd:
            ladino = row['Palavra']
            eshemplos = row.get('Eshemplos')
            examples = []
            if eshemplos is not None and eshemplos != '':
                examples = [{
                    'ladino': eshemplos,
                }]
            entry = {
                'origen'     : row['Origen'],
                'id'         : row['id'],
                'examples'   : examples,
                'versions': [{
                    'translations': {
                        'english'    : _extract_words(row['English']),
                        'spanish'    : _extract_words(row['Espanyol']),
                        'turkish'    : _extract_words(row['Turkish']),
                        'portuguese' : _extract_words(row['Portuguese']),
                        'french'     : _extract_words(row['French']),
                    },
                }]
            }
            #print(ladino)
            #print(english)
            if ladino is None:
                _err(f"Ladino is None in {row}")
                continue

            match = re.search(r'^(?P<words>[^()]+?)\s*(\((?P<grammar>.*)\))?\s*$', ladino)
            if match is None:
                _err(f"Ladino does not match it is '{ladino}'")
                continue
            grammar = match.group('grammar')
            words_str = match.group('words')
            #print(words_str)
            words = re.split(r'\s*[/,]\s*', words_str)
            word = words[0]
            match = re.search(words_regex, word)
            if not match:
                _err(f"Word '{word}' does not match our rules from Ladino {ladino}")
                continue
            #print(word)
            if entry['versions'][0]['translations']['english'].__class__.__name__ == 'list':
                translated_words = entry['versions'][0]['translations']['english']
            else:
                translated_words = [entry['versions'][0]['translations']['english']]
            for translated_word in translated_words:
                dictionary.append({translated_word: word})
            plain_word = remove_accent(word)
            all_words.add(plain_word)
            #if plain_word in full:
            #    prev = copy.deepcopy(full[plain_word])
            #    #prev_accented = prev.pop('accented')
            #    _err(f"Ladino word '{plain_word}' already exists. (original '{word}' row: {row})")
            #    print(prev, file=sys.stderr)
            #    print(entry, file=sys.stderr)
            #    print('-----', file=sys.stderr)
            #    continue
            #full[plain_word] = copy.deepcopy(entry)
            data = copy.deepcopy(entry)
            data['versions'][0]['accented'] = word
            data['versions'][0]['ladino'] = plain_word
            #grammar_types = get_grammar_types(grammar)
            print(grammar)
            if grammar == 'v':
                grammar = 'verb'
                data['conjugations'] = {}
            elif grammar == 'f':
                grammar = None
                data['versions'][0]['gender'] = 'feminine'
                data['versions'][0]['number'] = 'singular'
            elif grammar == 'm':
                grammar = None
                data['versions'][0]['gender'] = 'masculine'
                data['versions'][0]['number'] = 'singular'
            elif grammar is None:
                pass
            elif grammar in ['adv.', 'adv']:
                grammar = 'adverb'
            elif grammar == 'adj.':
                grammar = 'adjective'
            elif grammar == 'prep.':
                grammar = 'preposition'
            elif grammar in ['pron.', 'Pron.']:
                grammar = 'pronoun'
            else: #grammar in ['adj.+ m/f', 'm+pron.', 'n+adj.', 'm/p', 'm/f']: #, 'm), arabá (f', 'distribuir', 'la', 'en teatro']:
                data['comments'] = [f'grammar: {grammar}']
                grammar = None
            data['grammar'] = grammar

            if len(words) > 1:
                data['versions'][0]['alternative-spelling'] = []
                for alt_word in words[1:]:
                    data['versions'][0]['alternative-spelling'].append({
                        'ladino': remove_accent(alt_word),
                        'accented': alt_word,
                    })

            if len(sys.argv) == 2 and sys.argv[1] == 'all':
                full.append(data)
            else:
                # Normally just save one:
                word_file = f"words/{data['versions'][0]['ladino'].lower()}.yaml"
                if os.path.exists(word_file):
                    exit(f"File {word_file} already exists")
                print(f"{word_file}\nword: {data['versions'][0]['ladino'].lower()}\nid: {data['id']}")
                with open(word_file, 'w') as fh:
                    yaml.dump(data, fh, Dumper=yaml.Dumper, allow_unicode=True, indent=4)
                count -= 1
                if count <= 0:
                    exit()

    #save_librelingo_format(dictionary)
    save_yaml_format(sorted(full, key=lambda this: this['versions'][0]['ladino']))
    #save_words(all_words)


            #if grammar is None:
            #    print(ladino)


            #ladino_words = [ladino]
            #if re.search(r'/', ladino):
            #    ladino_words = ladino.split('/')
            #elif re.search(r',', ladino):
            #    ladino_words = ladino.split(',')
            #elif re.search(r';', ladino):
            #    ladino_words = ladino.split(';')

            #err = False
            #for ladino in ladino_words:
            #    if not re.search(r'^[A-Za-z ]+(\s?\.\.\.)?$', ladino):
            #        #print(f"ERROR ladino word '{ladino}' has unhandled characer in this row: {row}")
            #        err = True
            #        continue
            #if err:
            #    continue

            #for ladino in ladino_words:
            #    ladino = ladino.strip(' ')
            #    #if re.search('^la\s+[a-zA-Z]+$', ladino):
            #    print(ladino)

            #print(row)
            #exit()

if __name__ == '__main__':
    main()
