with open('data.txt', 'r') as f:
    lines = f.read().splitlines()

res = ""
for i in lines:
    shift = False
    data = i.split(':')
    if data[0] == "20":
        shift = True
    c = int(data[2], 16)
    if not c:
        continue
    if c < 0x1e:
        if shift:
            res += chr(ord('A')+c-4)
        else:
            res += chr(ord('a')+c-4)            
    elif c < 0x27:
        res += chr(ord('0')+c-0x1d)
    elif c == 0x27:
        res += '0'
    elif c == 0x2d:
        if shift:
            res += '_'
        else:
            res += '-'
    elif c == 0x30:
        if shift:
            res += '}'
        else:
            res += ']'
    elif c == 0x2f:
        if shift:
            res += '{'
        else:
            res += '['
    else:
        pass
print res

