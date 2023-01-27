# code from some nerd on stack overflow lmao
from pathlib import Path
fart = open('search ass.txt', 'w+')

for child in Path('.').iterdir():
    if child.is_file() and not str(child).startswith('search'):
        f = open(child.resolve(), 'r')
        x = f.readlines()
        for line in x:
            if line.lower().find('http') != -1:
                print(f'{child} | {line}')
                if line.endswith('\n'):
                    fart.write(f'{child} | {line}')
                else:
                    fart.write(f'{child} | {line}\n')
        f.close()

fart.close()
