# Cracking the Code Interview 
# making_anagrams.py
# Created by Mauro J. Pappaterra on 11 of March 2018.
FLAG = '*'

def number_needed(string_a, string_b):
    a = list(string_a)
    b = list(string_b)

    #FOR TESTING PURPOSES
    #print("".join(a) + "   " + "".join(b))

    for i,character_a in enumerate (a):
        for j,character_b in enumerate (b):
            if (character_a == character_b):
                a[i] = FLAG
                b[j] = FLAG
                #FOR TESTING PURPOSES
                print("".join(a) + "   " + "".join(b))
                break

    counter = [character for character in a + b if character != FLAG]
    print("".join(counter))
    return str(len(counter))

# FOR HACKER RANK EXTERNAL INPUT
#a = input().strip()
#b = input().strip()

#print(number_needed(a, b))

print(number_needed('abcdefg', 'gfedcba'))
print(number_needed('godsavesevasdog', 'godsavesevasdog'))
print(number_needed('ashortstring', 'notquiteashortstring'))
print(number_needed('noneoftheseareequal', 'somemight'))
print(number_needed('anotherrandomtext', 'somematchesoccurr'))




