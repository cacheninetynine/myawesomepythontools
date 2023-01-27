x = open('text.txt').read()
out = ''
vowels = 'aeiouy'
consonats = 'BCDFGHJKLMNPQRSTVWXZ'.lower()
special = r'!@#$%^&*() _+-=1234567890<>?:"}{\/[]|;'
extraspecial = '\n'

for i in range(0,len(x)-2,3):
    d = x[i]+x[i+1]+x[i+2]
    try:
        if d[0] == 'V':
            out += vowels[int(d[1:])]
        if d[0] == 'C':
            out += consonats[int(d[1:])]
        if d[0] == 'S':
            out += special[int(d[1:])]
        if d[0] == 'E':
            out += extraspecial[int(d[1:])]
    except IndexError:
        out+='⚠️'
    
        
print(out)
