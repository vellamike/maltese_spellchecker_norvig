# -*- coding: utf-8 -*-
"""
This is just an example of an application
"""

from spellcorrect import grammars
from spellcorrect import models

alphabet = list('abcdefghijklmnopqrstuvwxyzħċġż')
alphabet.append('ie')
alphabet.append('għ')

#we have a grammar for the language
grammar = grammars.Grammar(alphabet=alphabet)

#now we need a model
maltese_wiki_random_selection = open('./resources/maltese_wiki_random_selection.txt').read()
maltese_model = models.BaseModel(source_text = maltese_wiki_random_selection)

print(maltese_model.word_frequency('kruha'))
