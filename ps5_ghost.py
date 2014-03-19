#!/usr/bin/env python
# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def get_letter():
  letter = raw_input().lower()
  if letter in string.ascii_letters:
    return letter
  else:
    print ("Choose another letter : ")
    return get_letter()


def is_valid_word(fragment):
  for word in wordlist:
    if word[:len(fragment)] == fragment:
      if len(fragment) == len(word):
        ans = 1
        return ans 
      else:
        ans = 0
        return ans
  ans = 2
  return ans
      

def play_ghost(player, fragment):
  print ("current word fragment: %s"%fragment)
  if player > 2:
    player = 1
  print ("Player%d's turn."% player)
  letter = get_letter()
  fragment += letter
  print ("player%d says letter: %s"%(player, letter))
  if is_valid_word(fragment) == 1:
    if len(fragment) < 4:
      print ("%s is a word, but it's OK.  "% fragment)
      return play_ghost(player+1, fragment)
    else:
      print ("player%d is lost because %s is a word."%(player, fragment))
      return True
  elif is_valid_word(fragment) == 2:
    print ("player%d is lost because no word begin with %s."%(player,
                                                               fragment))
    return True
  else:
    return play_ghost(player+1, fragment)

def run_ghost():
  fragment = ''
  player = 1
  print ("Welcome to ghost!")
  play_ghost(player, fragment) 

run_ghost()

  



