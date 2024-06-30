import time
import random

# Inicializa o contador como 0
contador = 0

def gerar_id():
    global contador
    timestamp = int(time.time() * 1000)  # Obtém o timestamp atual em milissegundos
    numero_aleatorio = random.randint(10000, 99999)  # Gera um número aleatório de 5 dígitos
    
    # Incrementa o contador para garantir unicidade
    contador += 1
    
    # Concatena o timestamp, número aleatório e contador
    id_unico = f'{timestamp}{numero_aleatorio}{contador}'  
    
    return id_unico
