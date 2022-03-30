import csv
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
words_regex = f"^[ a-zA-Z{''.join(sorted(accents.keys()))}]+(\.\.\.|!|\?)?$"


def remove_accent(ladino):
    ladino = re.sub(r'á', 'a', ladino)
    ladino = re.sub(r'í', 'i', ladino)
    ladino = re.sub(r'é', 'e', ladino)
    ladino = re.sub(r'ó', 'o', ladino)
    ladino = re.sub(r'ú', 'u', ladino)

    return ladino

def get_grammer_types():
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

def main():
    filename = "diksionario_biervos_excel_corrected.csv"
    dictionary = []
    full = []
    all_words = set()
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')


        for row in rd:
            ladino = row.get('Palavra')
            eshemplos = row.get('Eshemplos')
            examples = []
            if eshemplos is not None and eshemplos != '':
                examples = [eshemplos]
            entry = {
                'english'    : row.get('English'),
                'examples'   : examples,
                'spanish'    : row.get('Espanyol'),
                'turkish'    : row.get('Turkish'),
                'origen'     : row.get('Origen'),
                'id'         : row.get('id'),
                'portuguese' : row.get('Portuguese'),
                'french'     : row.get('French'),
            }
            #print(ladino)
            #print(english)
            if ladino is None:
                _err(f"Ladino is None in {row}")
                continue
            #if entry['english'] is None:
            #    _err(f"English is None in {row}")
            #    continue
            #if len(entry['english']) < 2:
            #    _err(f"English is too short in {row}")
            #    continue

            match = re.search(r'^(?P<words>[^()]+?)\s*(\((?P<grammar>.*)\))?\s*$', ladino)
            if match is None:
                _err(f"Ladino does not match it is '{ladino}'")
                continue
            grammar = match.group('grammar')
            words_str = match.group('words') #.encode('utf-8').decode('utf-8')
            #print(words_str)
            words = re.split(r'\s*[/,]\s*', words_str)
            for word in words:
                match = re.search(words_regex, word)
                if not match:
                    _err(f"Word '{word}' does not match our rules from Ladino {ladino}")
                    continue
                #print(word)
                dictionary.append({entry['english']: word})
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
                data['accented'] = word
                data['ladino'] = plain_word
                data['grammar'] = grammar
                full.append(data)
            #if len(list(full.keys())) > 500:
            #    break

    save_librelingo_format(dictionary)
    #print(full)
    save_yaml_format(sorted(full, key=lambda entry: entry['ladino']))
    with open("words.txt", "w") as fh:
        for word in all_words:
            print(word, file=fh)

            #if grammar is None:
            #    print(ladino)

            #grammer_types = get_grammer_types(ladino)

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
