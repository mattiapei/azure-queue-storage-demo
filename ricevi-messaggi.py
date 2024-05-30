import os
import sys
import time
from azure.storage.queue import QueueClient
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
queue_name = os.getenv("NOME_CODA")

if connection_string is None:
    print("Manca la variabile di ambiente AZURE_STORAGE_CONNECTION_STRING")
    sys.exit(1)
    
# Creiamo un QueueClient usando la stringa di connessione
queue = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)
    
# Verifichiamo per 10 volte se ci sono dei messaggi, Se ci sono li togliamo dalla coda
for i in range(10):
    msg = queue.receive_message()
    if not msg:
        print("Nessun Messaggio")
    else:
        print(f"Identificativo: ", msg.id)
        print(f"Contenuto: ", msg.content, "\n")
        queue.delete_message(msg)
    time.sleep(1)
