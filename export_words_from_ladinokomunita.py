import csv
import re

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

def main():
    filename = "diksionario_biervos_excel_corrected.csv"
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')

        for row in rd:
            ladino = row.get('Palavra')
            english = row.get('English')
            #examples = row.get('Eshemplos')
            #Espanyol,Turkish,Origen,id,Portuguese,French
            #print(ladino)
            #print(english)
            if ladino is None:
                print(f"ERROR Ladino is None in {row}")
                continue
            if english is None:
                print(f"ERROR English is None in {row}")
                continue

            match = re.search(r'^[^()]+(\(.*\))?$', ladino)
            if match is None:
                print(f"ERROR in Ladino '{ladino}'")

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
