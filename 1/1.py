#print(6**10000)

kwota = 100
procent = 1.06
n_lat = 10**4

pytanie = 'ile lat? '

print(type(kwota))
print(type(procent))
print(type(pytanie))

print(kwota * (procent)**n_lat)
print(len(str(kwota * (procent)**n_lat)))

netto = 2439.1
vat = 0.23
netto = 3000 - 3000 * 0.23 
brutto = netto + 3000 * 0.23 
print(brutto)
print(round(brutto))
print(2 + 2 * 2)

kwota = 3.14
s = f'Kwota do zapłaty wynosi {kwota} zł. Prosimy o uregulowanie zobowiązania.'
print(s)

napis = f'faktura Vat kwota brutto wynosi {brutto} kwota netto wynosi {netto} podatek vat wynosi {vat}'
print(napis)