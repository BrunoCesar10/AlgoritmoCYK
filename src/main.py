import os
dirname = os.path.dirname(__file__)
text_file = os.path.join(dirname, '../file/gramatica.txt')

def gramatica():
    gramatica = []
    with open(text_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        regra = line.split('=')[0].replace(' ', '')
        valor = line.split('>')[1].replace(' ', '').replace('\n', '')

        if '|' in valor:
            lista_valores = []
            valores = valor.split('|')

            for valor in valores:
                lista_valores.append(valor)

            valor = tuple(lista_valores)
       
        gramatica.append((regra, valor))

    return gramatica

def separar(palavra):
    return [char for char in palavra]

def reconhecedor(palavra, gramatica):
    tabela = []
    gramatica = gramatica
    tamanho = len(palavra) + 1
    palavra = separar(palavra)

    for x in range(tamanho):
        if x == 0:
            linha = [0]
            for y in palavra:
                linha.append(y)
            tabela.append(linha)

        else:
            linha = [x]
            tabela.append(linha)


    #Preenchimento da Primeira Linha
    for letra in palavra:
        for regra in gramatica:
            for r in regra[1]:
                if letra in r:
                    tabela[1].append(regra[0])
                    continue

    print(tabela)

    #Preenchimento das outras linhas
    n = tamanho
    j = 1
    k = 1

    for i in range(2, n):
        print('i: {}'.format(i))
        for j in range(1, (n - i + 1)):
            print('j: {}'.format(j))
            for k in range(1, (i - 1)):
                print('k: {}'.format(k))
                valor = tabela[k][j]+tabela[i - k][j + k]
                print(valor)
                valor_regra = ''
                for regra in gramatica:
                    if valor == regra[1]:
                        valor_regra = regra[0]
                tabela[i].append(valor_regra)




def main():
    g = gramatica()
    p = str(input('Insira a palavra a ser analisada:\n'))
    reconhecedor(p, g)

if __name__ == '__main__':
    main()