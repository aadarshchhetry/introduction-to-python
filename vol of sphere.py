def vol(r):
    return 4/3*22/7*r**3
radius = int(input('enter radius'))
volume = vol(radius)
print(f'volume = {volume}')