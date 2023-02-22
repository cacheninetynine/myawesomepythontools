import requests
url = 'http://google.com'
request = requests.get(url=url)
href0 = request.text
while True:
    href1 = href0.find('href="')
    if href1 == -1:
        break
    href2 = href0[href1+6:]
    href3 = href2.find('"')
    href4 = href2[:href3]
    if not href4.startswith("http"):
        href4 = url+href4
    href5 = href2[href3+1:]
    href0 = href5
    print(href4)
