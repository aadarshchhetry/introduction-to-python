def has_33(n_list):
    for v in n_list:
        if v == 3:
            v=+1
            if v == 3:
                return True

result = has_33([2,3,3])
if result:
    print('True')
else:
    print('False')