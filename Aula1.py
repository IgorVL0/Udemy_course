any = True
i = 0

while any:
    i += 1
    if i == 5:
        any = False
    else:
        print(f'{i} não é igual a 5 ainda')

print(i)
