def is_reverse(word1, word2): 
    if len(word1) != len(word2): 
        return False
    i = 0 
    j = len(word2) 
    while j > 0: 
        if word1[i] != word2[j-1]: 
            return False 
        i = i+1
        j = j-1 
    return True

word1 = 'pots'
word2 = 'stop'

print(is_reverse(word1, word2))
