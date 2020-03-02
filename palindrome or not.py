def palindrome(s):
    palined = ''
    for char in s[::-1]:
        palined+=char
    return s == palined
result=palindrome(input('Enter a string : '))
if result:
    print('it is palindrome')
else:
    print('it is not a palindrome')