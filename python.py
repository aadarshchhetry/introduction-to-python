def lesser_num(num1,num2):
    if num1%2==0 and num2%2==0:
        if num1>num2:
            return num2
        else:
            return num1
    elif num1>num2:
        return num1
    else:
        return num2

n1 = int(input('Enter num 1 : '))
n2 = int(input('Enter num2 : '))

result = lesser_num(n1,n2)
print(result)