def master_yoda(s):
    word_list = s.split()
    size = len(word_list)
    i=0
    rev_word = ''
    while i < size:
        rev_word = word_list[i] + ' '+ rev_word
        i+=1
    return rev_word
non_rev = input('Enter your sentence here.')
reverse = master_yoda(non_rev)
print(f'Reversed: {reverse}')