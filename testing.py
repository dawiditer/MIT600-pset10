handDict = {"s":1,"d":2,"a":3,"e":3,"f":2,"c":4}
letters_freq_dict = {"a":2,"e":1,"z":1}

def getFrequencyDict(sequence):
    """
    Given a sequence of letters, convert the sequence to a dictionary of
    letters -> frequencies. Used by containsLetters().

    returns: dictionary of letters -> frequencies
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

#variant 1
def containsLetters(handDict, letters_freq_dict):
    """
    Test if this hand contains the characters required to make the input
    string (letters)

    returns: True if the hand contains the characters to make up letters,
    False otherwise
    """
    # TODO
    for letter in letters_freq_dict:
       if letter not in handDict or handDict[letter] - letters_freq_dict[letter] < 0:
           return False
    return True

print containsLetters(handDict, letters_freq_dict)

#variant 2
def containsLetters2(handDict, letters):
    try:
       return not bool([L for L in letters.keys() if handDict[L] - letters[L] < 0])
    except KeyError:
        return False    
print containsLetters2(handDict, letters_freq_dict) 

#### Variant 1 is better since it can exit before finishing the loop, while Variant 2
#### will have to loop through everything
