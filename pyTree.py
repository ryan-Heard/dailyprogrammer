
tip = int(input('Insert starting point: '))

while tip != 0:
    if tip % 3 == 0:
        print(str(tip) +' +0')
        tip = tip / 3
    elif tip % 3 == 1:
        print(str(tip) +' -1')
        tip = (tip - 1 ) / 3
    else:
        print(str(tip) +' +1')
        tip = (tip +1) / 3
