"""
Given two strings check to see of they are anagrams
Anagram --> when two strings can be written using the same letters (just need
to rearrange letters to get a different word)
Example:
"public relations" --> "crap built on lies"
"clint eastwood"  --> "old west action"

Ignore spaces and capitalization;
def anagram(string1, string2)

anagram('dog', 'god') --> true
anagram ('mam', 'cat') --> false

"""

# My solution --> Probably O(n^2); brute force (i think it's O(n))
def anagram(s1, s2):
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()
    for s in s1:
        if s not in s2:
            return False

    return True

# Instructor Solution
# Instructor logic --> Since both strings contain the same letters they will
# be similar strings when sorted!! O(1) --> Amazing!!!!!
# Not optimal since doesn't really show your thinking..proper solution with Dict
def anagramInst(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

# Instructor Dictionary solution - preferred solution - O(n)
def anagramInst2(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    # Edge case check
    if len(s1) != len(s2):
        return False

    count = {}
    # First time around add counts for the letters in the dict
    # Second time around remove or decrement count
    # If anagram end count will be 0

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

if __name__=="__main__":
    # my function test!
    print("Aditya Test")
    print(anagram("dog","god"))
    print(anagram("mam","cat"))
    print(anagram("public relations","crap built on lies"))
    print(anagram("clint eastwood","old west action"))
    print(anagram("Happy birthday","goodnight dear"))
    print("-"*50)

    # Instructor Test - Sorted
    print("Instructor test - Sorted")
    print(anagramInst("dog","god"))
    print(anagramInst("mam","cat"))
    print(anagramInst("public relations","crap built on lies"))
    print(anagramInst("clint eastwood","old west action"))
    print(anagramInst("Happy birthday","goodnight dear"))
    print("-"*50)

    # Instructor Test - Sorted
    print("Instructor test - Dict")
    print(anagramInst2("dog","god"))
    print(anagramInst2("mam","cat"))
    print(anagramInst2("public relations","crap built on lies"))
    print(anagramInst2("clint eastwood","old west action"))
    print(anagramInst2("Happy birthday","goodnight dear"))
