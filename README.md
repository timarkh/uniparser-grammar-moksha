# Moksha morphological analyzer
This is a rule-based morphological analyzer for Moksha (``mdf``; Uralic > Mordvinic). It is based on a formalized description of literary Moksha morphology, which also includes a number of dialectal elements, and uses [uniparser-morph](https://github.com/timarkh/uniparser-morph) for parsing. It performs full morphological analysis of Moksha words (lemmatization, POS tagging, grammatical tagging, glossing).

## How to use
### Python package
The analyzer is available as a Python package. If you want to analyze Moksha texts in Python, install the module:

```
pip3 install uniparser-moksha
```

Import the module and create an instance of ``MokshaAnalyzer`` class. Set ``mode='strict'`` if you are going to process text in standard orthography, or ``mode='nodiacritics'`` if you expect some words to lack the diacritics (which often happens in social media). After that, you can either parse tokens or lists of tokens with ``analyze_words()``, or parse a frequency list with ``analyze_wordlist()``. Here is a simple example:

```python
from uniparser_moksha import MokshaAnalyzer
a = MokshaAnalyzer(mode='strict')

analyses = a.analyze_words('Морфологиять')
# The parser is initialized before first use, so expect
# some delay here (usually several seconds)

# You will get a list of Wordform objects
# The analysis attributes are stored in its properties
# as string values, e.g.:
for ana in analyses:
        print(ana.wf, ana.lemma, ana.gramm, ana.gloss)

# You can also pass lists (even nested lists) and specify
# output format ('xml' or 'json')
# If you pass a list, you will get a list of analyses
# with the same structure
analyses = a.analyze_words([['А'], ['Мон', 'тонь', 'келькте', '.']],
	                       format='xml')
analyses = a.analyze_words(['Морфологиять', [['А'], ['Мон', 'тонь', 'келькте', '.']]],
	                       format='json')
```

Refer to the [uniparser-morph documentation](https://uniparser-morph.readthedocs.io/en/latest/) for the full list of options.

### Disambiguation
Disambiguation is not yet available for this language.

### Word lists
Alternatively, you can use a preprocessed word list. The ``wordlists`` directory contains a list of words from a 1.7-million-word [Moksha corpus](http://moksha.web-corpora.net/) (``wordlist_main.csv``), list of analyzed tokens (``wordlist_analyzed.txt``; each line contains all possible analyses for one word in an XML format), and list of tokens the parser could not analyze (``wordlist_unanalyzed.txt``). The recall of the analyzer is 91% on literary texts and 79% on social media texts.

## Description format
The description is carried out in the ``uniparser-morph`` format and involves a description of the inflection (paradigms.txt), a grammatical dictionary (kpv_lexemes_XXX.txt files), a list of rules that annotate combinations of lexemes and grammatical values with additional Russian translations (lex_rules.txt), and a short list of analyses that should be avoided (bad_analyses.txt). The dictionary contains descriptions of individual lexemes, each of which is accompanied by information about its stem, its part-of-speech tag and some other grammatical/borrowing information, its inflectional type (paradigm), and Russian translation. See more about the format [in the uniparser-morph documentation](https://uniparser-morph.readthedocs.io/en/latest/format.html).
