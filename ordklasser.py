from CONSTANTS import *

def adjective(word):
    """
    Determines whether a word is an adjective or not.
    """
    return word in ODD_ADJECTIVES or (word[-2:] == "ig" and word \
           not in PEOPLE_2) or word[-3:] == "lld" or word[-3:] == "igt" 


def verb(word):
    """ß
    Determines whether a word is a verb or not.
    """
    return word[-1] == "a" or word[-1] == "e"


def counting(word):
    """
    Determines whether a word is a räkneord or not.
    """
    return word in COUNTING


def needs_following(word):
    """
    Determines whether a word can stand on
    its own or not.
    """
    return word in NEEDS_FOLLOWING


def noun(word):
    """
    Determines whether a word is a noun or not.
    """
    if word[-2:] == "en" or "ett":
        return True
    if str.isupper(word[0]):
        return True
    return not verb(word) and not adjective(word) and not counting(word)


def place_pronomen(word):
    """
    Determines whether a word is a 
    (typ positionspronomen elr ngt) or not.
    """
    return word in PLACE_PRONOMEN


def people_1(word):
    """
    Determines whether a word is a personal
    reference (?) or not.
    """
    return word in PEOPLE_1


def people_2(word):
    """
    Determines whether a word is a personal
    reference (?) or not.
    """
    return word in PEOPLE_2

def possesive_pronomen(word):
    return word in POSSESSIVE_PRONOMEN