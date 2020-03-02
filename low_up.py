def up_low(s):
    u=0
    l=0
    for word in s:
        if word.isupper():
            u+=1
        elif word.islower():
            l+=1
    print(f'Number of uppercase = {u}/nNumber of lowercase = {l}')
up_low(input('Enter string'))