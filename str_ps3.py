#!/usr/bin/env python
#problem set3
from string import *

def countSubStringMatch(target, key):
  if target.find(key) == -1:
    return "not found"
  else:
    print(target.find(key))
    return target.find(key)


def init();
  target = "atgacatgcacaagtatgcat" 
  key = "atgc"
  return countSubStringMatch(target, key)


init()

