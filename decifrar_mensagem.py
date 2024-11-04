import sys
input = sys.stdin.read

def decodificar_mensagem(entrada):
    dados = entrada.strip().splitlines()
    indice = 0
    resultado = []
    
    while indice < len(dados):
        alfabeto = dados[indice].strip()
        n = int(dados[indice + 1].strip())
        lampadas = list(map(int, dados[indice + 2].strip().split()))
        
        # Decodificar a mensagem baseada nas lâmpadas piscadas
        mensagem = ''.join(alfabeto[lampada - 1] for lampada in lampadas)
        resultado.append(mensagem)
        
        # Avança para o próximo caso de teste
        indice += 3
    
    return '\n'.join(resultado)

# Ler entrada e processar a mensagem
entrada = input()
print(decodificar_mensagem(entrada))
