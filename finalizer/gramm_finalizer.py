import re
import os

rxDiacritics = re.compile('[ӥӧӵӟӝё]')
rxDiaPartsStem = re.compile('( stem:)( *[^\r\n]+)')
rxDiaPartsFlex = re.compile('(-flex:)( *[^\r\n]+)')
rxStemVariants = re.compile('[^ |/]+')
rxFlexVariants = re.compile('[^ /]+')
dictDiacritics = {'ӥ': 'и', 'ӧ': 'о', 'ӝ': 'ж',
                  'ӟ': 'з', 'ӵ': 'ч', 'ё': 'е'}
rxParadigmChange = re.compile('( stem: *[^\r\n]+ӟ\.\n(?: [^\r\n]*\n)*)'
                              '( paradigm: (?:Noun|connect_verbs)[^\r\n]+?)((?:-consonant)?)\n',
                              flags=re.DOTALL)


def collect_lemmata():
    lemmata = ''
    lexrules = ''
    for fname in os.listdir('..'):
        if fname.endswith('.txt') and fname.startswith('mdf_lexemes'):
            f = open(os.path.join('..', fname), 'r', encoding='utf-8-sig')
            lemmata += f.read() + '\n'
            f.close()
        elif fname.endswith('.txt') and fname.startswith('mdf_lexrules'):
            f = open(os.path.join('..', fname), 'r', encoding='utf-8-sig')
            lexrules += f.read() + '\n'
            f.close()
    lemmataSet = set(re.findall('-lexeme\n(?: [^\r\n]*\n)+', lemmata, flags=re.DOTALL))
    # lemmata = '\n'.join(sorted(list(lemmataSet),
    #                            key=lambda l: (re.search('gramm: *([^\r\n]*)', l).group(1), l)))
    lemmata = '\n'.join(sorted(list(lemmataSet)))
    return lemmata, lexrules


def add_diacriticless(morph):
    """
    Add a diacriticless variant to a stem or an inflection
    """
    morph = morph.group(0)
    if rxDiacritics.search(morph) is None:
        return morph
    return morph + '//' + rxDiacritics.sub(lambda m: dictDiacritics[m.group(0)], morph)


def process_diacritics_stem(line):
    """
    Remove diacritics from one line that contains stems.
    """
    morphCorrected = rxStemVariants.sub(add_diacriticless, line.group(2))
    return line.group(1) + morphCorrected


def process_diacritics_flex(line):
    """
    Remove diacritics from one line that contains inflextions.
    """
    morphCorrected = rxFlexVariants.sub(add_diacriticless, line.group(2))
    return line.group(1) + morphCorrected


def russify(text):
    """
    Add diacriticless variants for stems and inflections.
    """
    text = rxParadigmChange.sub('\\1\\2\\3\n\\2-soft\n', text)
    text = rxDiaPartsStem.sub(process_diacritics_stem, text)
    text = rxDiaPartsFlex.sub(process_diacritics_flex, text)
    return text


def main():
    """
    Put all the lemmata to lexemes.txt. Put all the lexical
    rules to lexical_rules.txt. Create separate versions of
    relevant files for diacriticless texts.
    """
    lemmata, lexrules = collect_lemmata()
    fOutLemmata = open('lexemes.txt', 'w', encoding='utf-8')
    fOutLemmata.write(lemmata)
    fOutLemmata.close()
    fOutLexrules = open('lex_rules.txt', 'w', encoding='utf-8')
    fOutLexrules.write(lexrules)
    fOutLexrules.close()


if __name__ == '__main__':
    main()
