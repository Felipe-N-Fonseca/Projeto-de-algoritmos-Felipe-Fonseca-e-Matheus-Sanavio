# Felipe Fonseca (tia 4221536-6)
# Matheus Sanavio (tia 4221654-0)
# versão: 1.0
# data e hora da versão: 24/10/2022 02:51

def verificadorDeQuadrante(n1, n2, x, y):
    if n1 == x or n2 == y:
        return 'eixo coordenado'

    elif n1 > x:
        if n2 > y:
            return '1° quadrante'
        else:
            return '4° quadrante'
    else:
        if n2 > y:
            return '2° quadrante'
        else:
            return '3° quadrante'


xInicial = int(input('digite o valor inteiro do x da origem: '))
yInicial = int(input('digite o valor inteiro do y da origem: '))
N = int(input('número de coordenadas que serão pedidas: '))
maisLonge = ''
menosLonge = ''
maior = 0
menor = 0

for c in range(0, N):
    x = int(input(f'{c+1}° x: '))
    y = int(input(f'{c+1}° y: '))
    print(f'Ponto ({x},{y}) está no {verificadorDeQuadrante(x, y, xInicial, yInicial)}')
    distancia = ((x - xInicial) ** 2 + (y - yInicial) ** 2) ** 0.5

    if c == 0:
        maior = distancia
        maisLonge = f'({x},{y})'
        menor = distancia
        menosLonge = f'({x},{y})'
    else:
        if maior < distancia:
            maior = distancia
            maisLonge = f'({x},{y})'
        if menor > distancia:
            menor = distancia
            menosLonge = f'({x},{y})'

print(f'Ponto {menosLonge} é o mais próximo, distância = {menor:.2f}.')
print(f'Ponto {maisLonge} é o mais distante, distância = {maior:.2f}.')
