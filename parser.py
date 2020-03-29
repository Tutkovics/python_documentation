import re


def textParser(self, text):
        """
        General description of function 
        :param self: 
        :param text: lorem ipsum come from...
        :return: something 
        """
    
    # regex defining what to consider as a word 
    word_regex = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
    words = word_regex.split(text)
    words = [word.lower() for word in words if len(word) > 0]
    return words
