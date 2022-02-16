from datetime import date
nascimento=int(input('Informe seu ano de nascimento:'))
atual= date.today().year
idade= atual - nascimento
saldo=idade-18
if idade <= 17:
    print('Você ainda precisará se alistar!')
    print('Ainda faltam {} para o seu alistamento!'.format(18-idade))
    print('Seu alistamento será em {}' .format(atual+saldo))
elif idade == 18:
    print('Você deverá se alistar esse ano!')
elif idade > 18:
    print('Você já deveria ter se alistado!')
    print('Seu alistamento foi no ano de {}!'.format(atual-saldo))
    print('Então já se passaram {} anos do prazo'.format(atual - (atual- saldo)))
