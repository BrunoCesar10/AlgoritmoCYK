# Algoritmo CYK 💼
O algoritmo CYK (Cocke-Younger-Kasami) é um algoritmo de análise sintática para gramáticas livres de contexto que utiliza programação dinâmica para determinar se uma determinada palavra pertence à uma gramática, e é notório por sua alta eficiência computacional. Para que uma gramática possa ser analisada pelo algoritmo CYK, ela deve estar na forma normal de Chomsky. 

## Leitura de arquivo 📑
Para que o programa funcione, substitua a gramática existente no arquivo 'gramatica.txt' na pasta file com a que deseja analisar.

Importante: O arquivo deve estar em formato txt, as regras devem sempre estar organizadas uma por linha e devem seguir o formato X => YZ ou X => x, com letras maiúsculas sendo não-terminais e letras minúsculas sendo terminais.

A gramática utilizada deve sempre estar na forma normal de Chomsky.

## Analisando palavras 🖨
Execute o arquivo 'main.py' na pasta src. Um prompt textual o pedirá para inserir a palavra que deseja analisar. Após inserir a palavra e apertar Enter, o programa retornará a impressão da gramática salva no arquivo.txt, a execução do algoritmo CYK, e se a palavra inserida é aceita pela gramática ou não.

