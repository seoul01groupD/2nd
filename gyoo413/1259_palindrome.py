def find_palin(number):
    if len(number) == 0 or len(number) == 1:
        return 'yes'
    else:
        if number[0] != number[-1]:
            return 'no'
        else:
            number = number.replace(number[0], '', 2)
            return find_palin(number)

while(True):
    n = input()
    if n == '0':
        break
    else:
        n = n.lstrip('0')
        print(find_palin(n))
