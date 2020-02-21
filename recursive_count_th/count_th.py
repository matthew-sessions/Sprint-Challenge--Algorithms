'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, ind=0, count=0):
    if len(word) < 2:
        return count
    if len(word) == 2:
        if word == 'th':
            count += 1
            return count
        else: 
            return count
    if word[:2] == 'th':
        count += 1
    return(count_th(word[1:], ind, count))
    
print(count_th('thisithsathad'))