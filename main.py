#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, collections

def words(text): return re.findall('[a-zżħċġ]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

word_array = file('dictionary.txt').read()
wiki_word_array = file('maltese_wiki_random_selection.txt').read()

word_array += wiki_word_array
word_array = wiki_word_array

number_of_words = train(words(word_array))

print 'num of words:'
print number_of_words['xogħolijiet']

alphabet = 'abcdefghijklmnopqrstuvwxyzħċġż'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in number_of_words)

def known(words): return set(w for w in words if w in number_of_words)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    print candidates
    result = max(candidates, key=number_of_words.get)
    return result


def sentence_correct(str):
    corrected_words = []

    for word in string.split():
        print word
        corrected_words.append(correct(word))
    return " ".join(corrected_words)

#Example:
string = 'jien pjutttost mistagħgeb b\'kemm hi tajjba di l-ewwel verżjonii' #BECOMES jien pjuttost mistagħġeb kemm hi tajba di newwel verżjoni
string = 'xoghlijiet'
print sentence_correct(string)

print 'is it known?'
word = 'xogholijiet'
print known([word])
print 'xogħolijiet' in edits1(word.encode('utf8'))
