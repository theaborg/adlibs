from CONSTANTS import *
from ordklasser import *
import random


def get_index(word, original_lyrics):
    """ 
    Returns the index of a specific word in the original lyrics.
    """
    i = 0
    for og_word in original_lyrics:
        if og_word == word:
            break
        i += 1
    return i    


def adjective_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if an adjective can be put at this position
    in the ad_libs_list.
    """
    if adjective(word):
        index = get_index(word, original_lyrics)
        if original_lyrics[index-1] == ad_libs_list[-1]:
            return True
        elif ad_libs_list[-1] in NEEDS_FOLLOWING:
            return False
        elif len(ad_libs_list) > 1: 
            return not (adjective(ad_libs_list[-1]) and \
                   adjective(ad_libs_list[-2]))
        elif len(ad_libs_list) == 1:
            return True
    else:
        return False


def noun_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a noun can be put at this position
    in the ad_libs_list.
    """
    if noun(word):
        index = get_index(word, original_lyrics)
        if original_lyrics[index-1] == ad_libs_list[-1]:
            return True
        else:
            return not noun(ad_libs_list[-1]) 
    else:
        return False


def counting_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a räkneord can be put at this position
    in the ad_libs_list.
    """
    if counting(word):
        index = get_index(word, original_lyrics)
        return original_lyrics[index-1] == ad_libs_list[-1]
    else:
        return False


def needs_following_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a word which needs a following word
    can be put at this position in the ad_libs_list.
    """
    if needs_following(word):
        #index = get_index(word, original_lyrics)
        #return ad_libs_list[-1] == original_lyrics[index-1]
        return True
    else:
        return False


def place_pronomen_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a (positionspronomen) can be put at this position
    in the ad_libs_list.
    """
    if place_pronomen(word):
        return verb(ad_libs_list[-1])


def people1_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a (positionspronomen) can be put at this position
    in the ad_libs_list.
    """
    if people_1(word):
        last_word = ad_libs_list[-1]
        if people_2(last_word) or noun(last_word) or people_1(last_word):
            return False
        else:
            return last_word in COOL_WORDS_LIST 
    else:
        return False


def people2_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a (positionspronomen) can be put at this position
    in the ad_libs_list.
    """
    if people_2(word):
        last_word = ad_libs_list[-1]
        index = get_index(word, original_lyrics)
        if people_1(last_word) or people_2(last_word) or noun(last_word):
            print("Pls")
            return False
        elif original_lyrics[index-1] == last_word:
            print("nehe")
            return True
        else:
            print("VA")
            return verb(last_word) or needs_following(last_word)


def possessive_pronomen_allowed(word, ad_libs_list, original_lyrics):
    """
    Determines if a possessive pronomen can be put at this 
    position in the ad_libs_list.
    """
    if possesive_pronomen(word):
        return ad_libs_list[-1] in COOL_WORDS_LIST or\
                verb(ad_libs_list[-1])
    else:
        return False


def correct_ad_libs(ad_libs_list, original_lyrics):
    """
    This function checks the ad libs for faulty constructions
    and fixes them by adding cool words B)
    """
    last_word = ad_libs_list[-1]
    index = get_index(last_word, original_lyrics)
    for word in ad_libs_list:
        if word in NO_GO_WORDS:
            index = get_index(word, ad_libs_list)
            ad_libs_list[index] = COOL_WORDS_LIST[random.randint(0, len(COOL_WORDS_LIST)-1)]
    if last_word in NEEDS_FOLLOWING or COUNTING or people_1(last_word):
        ad_libs_list.append(COOL_WORDS_LIST[random.randint(0, len(COOL_WORDS_LIST)-1)])
    elif possesive_pronomen(last_word) or place_pronomen(last_word):
        ad_libs_list.append(original_lyrics[index+1])
    elif len(ad_libs_list) < 2:
        if ad_libs_list[0] in NOT_ALONE:
            ad_libs_list = [' på', ' gud', ' due', ' fitta']
        ad_libs_list.append(COOL_WORDS_LIST[random.randint(0, len(COOL_WORDS_LIST)-1)])
    #vill kolla om vi "kastar om" orden kostigt 
    return ad_libs_list


def word_allowed(word, ad_libs_list, original_lyrics):
    """
    Checks if a specific word can be appended to the ad libs.
    """
    if not ad_libs_list[-1] == word:
        return adjective_allowed(word, ad_libs_list, original_lyrics) or noun_allowed(word, ad_libs_list, original_lyrics) or \
               counting_allowed(word, ad_libs_list, original_lyrics) or needs_following_allowed(word, ad_libs_list, original_lyrics) or \
                place_pronomen_allowed(word, ad_libs_list, original_lyrics) or people1_allowed(word, ad_libs_list, original_lyrics) or \
                people2_allowed(word, ad_libs_list, original_lyrics) or possessive_pronomen_allowed(word, ad_libs_list, original_lyrics)
