import psutil # Importa a biblioteca psutil
import time # Importa a biblioteca time

while True: # Cria um loop infinito
    
    cpu_percent = psutil.cpu_percent() # Obtém o uso da CPU em porcentagem
    
    virtual_memory = psutil.virtual_memory() # Obtém informações sobre a memória virtual
    
    disk_usage = psutil.disk_usage("/") # Obtém informações sobre o uso do disco
    
    temperature = psutil.sensors_temperatures()['coretemp'][0].current # Obtém a temperatura da CPU

    print("CPU Usage:", cpu_percent, "%") # Exibe informações sobre o uso da CPU

    print("Memory Usage:", virtual_memory.used / (1024 * 1024), "MB") # Exibe informações sobre o uso da memória

    print("Disk Usage:", disk_usage.percent, "%") # Exibe informações sobre o uso do disco

    print("CPU Temperature:", temperature, "°C") # Exibe a temperatura da CPU

    print("<-------------------------------->") # Separador entre cada checagem

    time.sleep(3) # Aguarda 3 segundos antes de repetir o loop
