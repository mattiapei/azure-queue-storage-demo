Demo di Azure Queue Storage con Python
======================================

Questo progetto contiene una demo di base su come utilizzare Azure Queue Storage con Python. 
Il progetto fa parte del video corso youtube Microsoft Azure Fundamentals [AZ-900 -  Corso in Italiano](https://www.youtube.com/playlist?list=PLrRt9ahDqfrhB6UqzIsIyWopc65otTIRB)
Il progetto è costituito da due file:

1.  `invia-messaggi.py`: Invia 10 messaggi a una coda Azure Queue Storage.
2.  `ricevi-messaggi.py`: Riceve 10 messaggi dalla stessa coda Azure Queue Storage.

Prerequisiti
------------

Prima di eseguire questa demo, assicurati di avere installato Python sul tuo sistema e di aver configurato un account Azure con uno storage account di archiviazione e una coda Queue Storage.

Setup
-----

Segui questi passaggi per configurare l'ambiente:

1.  Crea una coda in Azure Queue Storage.
    
2.  Copia il nome della coda e l'Azure Storage Connection String dal portale Azure.
    
3.  Crea un file `.env` nella root del progetto e aggiungi le seguenti variabili:
    
    plaintext
    
    Copy code
    
    `NOME_CODA=nome_coda_azure` 
    `AZURE_STORAGE_CONNECTION_STRING=tua_connection_string`
    
    Sostituisci `nome_coda_azure` con il nome effettivo della tua coda Azure e `tua_connection_string` con la stringa di connessione dell'account di archiviazione.
    

Utilizzo
--------

1.  Esegui il file `invia-messaggi.py` per inviare messaggi alla coda Azure Queue Storage.
    
    bash
    
    Copy code
    
    `python invia-messaggi.py`
    
2.  Esegui il file `ricevi-messaggi.py` per ricevere i messaggi dalla coda Azure Queue Storage.
    
    bash
    
    Copy code
    
    `python ricevi-messaggi.py`
    

Nota
----

Assicurati di aver installato tutte le dipendenze Python necessarie. Puoi farlo eseguendo:

bash

Copy code

`pip install -r requirements.txt`

Licenza
-------

Questo progetto è distribuito con licenza MIT.