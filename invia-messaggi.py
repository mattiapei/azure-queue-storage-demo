import os
import sys
import time
from azure.storage.queue import QueueClient

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
queue_name = os.getenv("NOME_CODA")

if connection_string is None or queue_name is None:
    print("Manca una variabile di ambiente.")
    sys.exit(1)
    
# Creiamo un QueueClient usando la stringa di connessione
queue = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)

try:
    # Invio 10 messaggi   
    for i in range(10): 
        queue.send_message(f"Ciao. Questo è il messaggio numero {i}")
        print(f"Messaggio {i} inviato")
        time.sleep(1)

except:
  print("Errore nell'invio dei messaggi")
  sys.exit(1)
