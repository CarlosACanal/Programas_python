'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
 as notas de cada aluno individualmente.'''
lista_geral=[]
dados=[]
while True:
    nome = str(input('Digite o nome:'))
    nota1=float(input('Digite a 1ª nota:'))
    nota2 = float(input('Digite a 2ª nota:'))
    media= (nota1+nota2)/2
    r=str(input('Quer adicionar outro aluno?[S/N]')) . lower()
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)
    lista_geral.append(dados[:])
    dados.clear()
    if 'n' in r:
        break
print('=-'*30)
print(f'{"Nª":<4}{"Aluno":<10}{"Média":<8}')
for p,a in enumerate(lista_geral):
    print(f'{p:<4}{a[0]:<10}{a[3]:<8.1f}')
print('=-'*30)
while True:
    r=int(input('Deseja ver as notas de qual aluno? Informe o nª. [999 sair]'))
    if r==999:
        break
    print(f'As notas de {lista_geral[r][0]} são {lista_geral[r][1]} e {lista_geral[r][2]}')
