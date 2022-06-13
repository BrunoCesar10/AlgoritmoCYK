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
    palavra_str = palavra
    palavra = separar(palavra)

    for x in range(tamanho):
        if x == 0:
            linha = [0]
            for t in palavra:
                linha.append(t)
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

    for q in range(2, tamanho):
        for s in range(tamanho - 1):
            tabela[q].append(' ')

    print(gramatica)
    print('')

    #Preenchimento das outras linhas   
    n = tamanho

    try:
        for i in range(2, n):

            for j in range(1, (n - i + 1)):

                for k in range(1, i):

                    y = tabela[k][j]
                    z = tabela[i - k][j + k]
                    x = y + z

                    for regra in gramatica:
                        if isinstance(regra[1], tuple):
                            if x in regra[1]:
                                tabela[i][j] = regra[0] 
                        else:
                            if x == regra[1]:
                                tabela[i][j] = regra[0]
    except IndexError:
        print('Ops! Um dos caracteres da palavra inserida, ({}), não esta na gramatica'.format(palavra_str)) 

    for linha in tabela:
        print(linha)
    print('')

    if tabela[len(palavra)][1] == gramatica[0][0]:
        print('Palavra Aceita')
    else:
        print('Palavra Rejeitada')

def main():
    g = gramatica()
    p = str(input('Insira a palavra a ser analisada:\n'))
    reconhecedor(p, g)

if __name__ == '__main__':
    main()