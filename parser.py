import re


def textParser(self, text):
    """General description of my text parser function

    :param self: default parameter
    :param text: lorem ipsum come from other method
    :type text: string
    :return: something importanat
    :rtype: int
    """
    
    # regex defining what to consider as a word 
    word_regex = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
    words = word_regex.split(text)
    words = [word.lower() for word in words if len(word) > 0]
    return words
