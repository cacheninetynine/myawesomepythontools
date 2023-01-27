import requests
x = open('port.txt', 'w+')
for i1 in range(0,65537):
    ip = f'https://beta.character.ai:{i1}'
    ip2 = f'https://beta.character.ai/:{i1}'
    try:
        r = requests.get(ip, verify=False, timeout=0.2)
        if r.status_code == 200:
            print(f'!!!!! {ip} {r.status_code}\n')
            x.write(f'!!!!! {ip} {r.status_code}\n')
        elif r.status_code == 403:
            print(f'????? {ip} {r.status_code}\n')
            x.write(f'????? {ip} {r.status_code}\n')
        else:
            print(f'{ip} {r.status_code}\n')
            x.write(f'{ip} {r.status_code}\n')
    except:
        print(f'{ip} FAKE\n')
        x.write(f'{ip} FAKE\n')
    try:
        r2 = requests.get(ip2, timeout=0.2)
        if r.status_code == 200:
            print(f'!!!!! {ip2} {r2.status_code}\n')
            x.write(f'!!!!! {ip2} {r2.status_code}\n')
        elif r.status_code == 403:
            print(f'????? {ip2} {r2.status_code}\n')
            x.write(f'????? {ip2} {r2.status_code}\n')
        else:
            print(f'{ip2} {r2.status_code}\n')
            x.write(f'{ip2} {r2.status_code}\n')
    except:
        print(f'{ip2} FAKE\n')
        x.write(f'{ip2} FAKE\n')
    print('=============================\n')
    x.write(f'=============================\n')
x.close()
                
