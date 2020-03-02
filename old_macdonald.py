def old_macdonald(s):
    new = []
    for i in s:
        new.append(i)
    new[0] = new[0].upper()
    new[3] = new[3].upper()
    word = ''
    for p in new:
        word = word + p
    return word
new_word = old_macdonald('macdonalds')
print(new_word)