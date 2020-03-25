uniparser-grammar-moksha
========================

This is a formalized description of literary Moksha morphology, which also includes a number of dialectal elements and spelling variants. The description is carried out in the UniParser format and involves a description of the inflection (paradigms.txt), a grammatical dictionary (mdf_lexemes_XXX.txt files), a list of rules that annotate combinations of lexemes and grammatical values with additional Russian translations (mdf_lexrules_XXX.txt), and a short list of analyses that should be avoided (bad_analyses.txt). The dictionary contains descriptions of individual lexemes, each of which is accompanied by information about its stem, its part-of-speech tag and some other grammatical/borrowing information, its inflectional type (paradigm), and Russian translation.

This description can be used for morphological analysis of Moksha texts in the following ways:

1. The Wordlists directory contains two frequency lists of Moksha tokens and the output of the analyzer for these lists. First word list based on the Moksha literary corpus (1.74M words), and the second, on the tiny Moksha social media corpus (14 thousand words). "main_parsed.txt" contains all analyzed words from the literary corpus. Each line contains all possible analyses of a token in XML. The simplest solution is to use this list for analyzing your texts. The recall of the analyzer is currently 91% on literary texts and 79% on social media texts.

2. The Analyzer directory contains the UniParser set of scripts together with all necessary language files. You can use it to analyze your own frequency word list. Your have to name your list "wordlist.csv" and put it to that directory. Each line should contain one token and its frequency, tab-delimited. When you run analyzer/UniParser/analyze.py, the analyzer will produce two files, one with analyzed tokens, the other with unanalyzed ones. (You can also use other file names and separators with command line options, see the code of analyze.py.) This way, you will not be restricted by my word list, but the analyzer works pretty slowly (expect 300-400 tokens per second).

3. Finally, you are free to convert/adapt the description to whatever kind of morphological analysis you prefer to use.

This software is distributed under the MIT license (see LICENSE.md).
