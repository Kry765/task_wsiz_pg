s = input('podaj username> ')

if len(s) < 5:
    print('za krótka nazwa; plz >=5 znaków')
    print('---')
if s.islower():
    print('małe litery są zabronione')
else:
    print(f'ok, witaj {s}')

if s.isupper():
    print('fajnie... same caps-y w nazwie...')

if s.isdigit():
    print('same cyfry w napisie')