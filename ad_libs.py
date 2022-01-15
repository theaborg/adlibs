import random
from CONSTANTS import *
from allowed_constructions import *
from ordklasser import *


def ad_libs(lyrics):
    """
    A function that generates the perfect ad libs.
    """
    ad_libs_list = []
    word_class_list = letters_to_words(lyrics)

    return grovfunktion(word_class_list, ad_libs_list)
    

def letters_to_words(lyrics):
    """
    Takes a string and returns a list of the words in the string.
    """
    word_class_list = []
    word = ""
    for letter in lyrics:
        if word and (letter == " " or letter == ","):
            word_class_list.append((word))
            word = ""
        else:
            word += letter

    word_class_list.append((word))
    
    return word_class_list


def grovfunktion(word_class_list, ad_libs_list):
    """ 
    Does the grovjobb.
    """
    i=0
    original_lyrics = word_class_list
    while i in range(10):
        checking_word = word_class_list\
                        [random.randint(0, len(word_class_list)-1)]
        if not ad_libs_list or ad_libs_list[-1] in COOL_WORDS_LIST:
            ad_libs_list.append(checking_word)
        else:
            if word_allowed(checking_word, ad_libs_list, original_lyrics):
                ad_libs_list.append(checking_word)
        i+=1

    return correct_ad_libs(ad_libs_list, original_lyrics)
