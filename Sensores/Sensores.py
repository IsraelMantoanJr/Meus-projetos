import psutil # Importa a biblioteca psutil
import time # Importa a biblioteca time

while True: # Cria um loop infinito
    cpu_percent = psutil.cpu_percent() # Obtém o uso da CPU em porcentagem
    virtual_memory = psutil.virtual_memory() # Obtém informações sobre a memória virtual
    print("Uso da CPU:", cpu_percent, "%") # Exibe o uso da CPU
    print("Uso da memória:", virtual_memory.used / (1024 * 1024), "MB") # Exibe o uso da memória em MB
    time.sleep(1) # Aguarda 1 segundo antes de repetir o loop

