#!/usr/bin/env python
# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 2

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    value = 0
    l = 0
    for letter in word:
      value += SCRABBLE_LETTER_VALUES[letter]
      l += 1
    if l == n:
      value += 50
    return value



#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print ("current hand: ")
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    new_hand = hand.copy()
    #print ('new hand: ',new_hand)
    for letter in word:
      if new_hand[letter] != 0:
        new_hand[letter] -= 1
      else:
        return False
    return new_hand



#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    #print hand.keys()
    new_hand = hand.copy()
    for letter in word:
      if letter not in hand.keys():
        return False
      new_hand[letter] -= 1
      if new_hand[letter] < 0:
        return False

    if word not in word_list:
      return False
    else:
      return True


#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list,tot_score, rmn_time):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    if len(hand) == 0:
      return tot_score
    display_hand(hand)
    start_time = time.time()
    word = raw_input("Enter word or n, r, e:  ")
    while not is_valid_word(word,hand, word_list):
      if word == "e":
        print ("total score: %d points"% tot_score)
        return tot_score
      elif word == "r":
        return play_hand(old_hand, word_list, 0)
      elif word == "n":
        return test_all()
      else:
        word = raw_input("Choose another word:")
    end_time = time.time()
    tot_time = end_time - start_time
    rmn_time = rmn_time - tot_time
    print ("It took %0.2f seconds to provide an answer."%tot_time)
    
    if rmn_time < 0:
      print("Total time exceeds %0.2f seconds."% lim_time)
      print ("total score: %d points"% tot_score)
      return tot_score
    else:
      new_hand = update_hand(hand, word)
      score = get_word_score(word,HAND_SIZE)
      tot_score += score
      print ("%s earned %d points. Total: %d points"%(word, score,
             tot_score))
      print("You have %0.2f seconds remaining."% rmn_time)
      play_hand(new_hand, word_list, tot_score, rmn_time)


def get_word_to_points(word_list):
  wd_pts = {}
  for word in word_list:
    for letter in word:
      wd_pts[word] = wd_pts.get(word, 0) + SCRABBLE_LETTER_VALUES[letter]
  return wd_pts


def pick_best_word(hand,word_list, pts_dict):
  hi_pt = 0
  ans = 'NONE' 
  for word in word_list:
    if is_valid_word(word, hand, word_list) and pts_dict[word] > hi_pt:
      ans = word
      hi_pt = pts_dict[word]
  if ans == 'NONE':
    print("No answer.")
    return '.'
  else:
    print("The best word is %s. "%ans)
    return ans


def test_all():
  tot_score = 0
  word_list = load_words()
  global pts_dict 
  pts_dict = get_word_to_points(word_list)
  hand = deal_hand(HAND_SIZE)
  global old_hand
  old_hand = hand.copy()
  sel = raw_input("h player or c player?")
  if sel == 'c':
    display_hand(hand)
    return pick_best_word(hand, word_list, pts_dict)
  elif sel == 'h':
    global lim_time
    lim_time = float(raw_input("Enter time limit, for players: "))
    rmn_time = lim_time
    return play_hand(hand, word_list, tot_score, rmn_time)
  else:
    print("Choose again.")
    return test_all()
 
test_all()





'''
#5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    print "play_game not implemented."         # delete this once you've completed Problem #4
    play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
#    hand = deal_hand(HAND_SIZE) # random init
#    while True:
#        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
#        if cmd == 'n':
#            hand = deal_hand(HAND_SIZE)
#            play_hand(hand.copy(), word_list)
#            print
#        elif cmd == 'r':
#            play_hand(hand.copy(), word_list)
#            print
#        elif cmd == 'e':
#            break
#        else:
#            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
'''
