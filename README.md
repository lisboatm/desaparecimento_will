# Desaparecimento de Will

Este projeto decifra mensagens enviadas por Will através de uma sequência de lâmpadas piscadas. Cada lâmpada está associada a uma letra do alfabeto, e a sequência de piscadas revela uma mensagem.

## Descrição do Problema

Will está desaparecido, mas consegue se comunicar por meio de uma sequência de 26 lâmpadas numeradas de 1 a 26. Cada lâmpada corresponde a uma letra do alfabeto. Quando Will deseja enviar uma mensagem, ele pisca as lâmpadas associadas às letras da mensagem, uma por vez. Sua tarefa é decifrar essas mensagens a partir de uma sequência dada de lâmpadas piscadas.

### Exemplo

Dada uma sequência de letras associadas às lâmpadas:
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
E uma sequência de lâmpadas piscadas:
```
8 5 12 16
```
A mensagem decifrada será:
```
HELP
```

## Entrada

O programa recebe vários casos de teste, cada um contendo:
1. Uma string de 26 letras maiúsculas, representando as letras do alfabeto, onde cada posição está associada a uma lâmpada numerada de 1 a 26.
2. Um número inteiro `N` representando o número de lâmpadas piscadas.
3. Uma sequência de `N` inteiros indicando as lâmpadas que foram piscadas.

A entrada termina com fim-de-arquivo (EOF).

## Saída

Para cada caso de teste, o programa imprime a mensagem decifrada.

## Exemplo de Entrada e Saída

**Entrada**
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
4
8 5 12 16
QWERTYUIOPASDFGHJKLZKCVBNM
10
16 3 19 19 9 2 9 4 19 13
```

**Saída**
```
HELP
HELLOWORLD
```

## Como Executar o Código

1. Salve o código em um arquivo, como `decifrar_mensagem.py`.
2. Execute o programa no terminal ou editor de sua escolha:
   ```bash
   python decifrar_mensagem.py
   ```
3. Digite a entrada diretamente no terminal ou redirecione a partir de um arquivo.

## Explicação da Lógica

1. **Associação das Letras**: Cada letra na primeira linha da entrada está associada a uma posição de lâmpada.
2. **Decodificação da Mensagem**: Para cada lâmpada piscada, o programa identifica a letra correspondente usando a posição indicada.
3. **Construção da Mensagem**: O programa monta a mensagem com base nas lâmpadas piscadas e exibe o resultado.
