def animal_cracker(s):
    wl = []
    wl = s.split()

    if wl[0,0]==wl[1,0]:
        return True
    else:
        return False

if animal_cracker('slim shady') :
    print('True')
else:
    print('False')