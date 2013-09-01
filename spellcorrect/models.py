# -*- coding: utf-8 -*-
"""
Model for the maltese language.

Initially the concept is that for a word the return value
is the probability that it is the correct word.

In future this concept can be extended to include cotext.

A grammar should be able to be used by the model to help
it understand what it is parsing.
"""

import re
import collections

class BaseModel():
    def __init__(self,source_text,grammar=None):
        self.source_text = source_text
        self.word_frequency_dict = self.__number_of_words()

    def __train(self,features):
        
        frequency_dict = collections.defaultdict(lambda: 1)
        for f in features:
            frequency_dict[f] += 1
        return frequency_dict
        
    def __number_of_words(self):
        num_words = self.__train(self.__words)
        return num_words

    @property
    def __words(self):
        return re.findall('[a-zżħċġ]+', self.source_text.lower()) 

    def word_frequency(self,word):
        return self.word_frequency_dict[word]
