import csv
import re
import sys
import yaml


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

def main():
    filename = "diksionario_biervos_excel_corrected.csv"
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')

        dictionary = []

        for row in rd:
            ladino = row.get('Palavra')
            english = row.get('English')
            #examples = row.get('Eshemplos')
            #Espanyol,Turkish,Origen,id,Portuguese,French
            #print(ladino)
            #print(english)
            if ladino is None:
                _err(f"Ladino is None in {row}")
                continue
            if english is None:
                _err(f"English is None in {row}")
                continue

            match = re.search(r'^(?P<words>[^()]+?)\s*(?P<grammar>\(.*\))?\s*$', ladino)
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
                if len(english) < 2:
                    continue
                dictionary.append({english: word})

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

            #if grammar is None:
            #    print(ladino)

            #grammer_types = get_grammer_types(ladino)
            #ladino = remove_accent(ladino)

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
