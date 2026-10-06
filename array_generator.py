# array_generator.py

# Definiamo una funzione chiamata "stampa_array".
# La funzione riceve come parametro un array (lista).
def stampa_array(array):

    # Stampiamo un messaggio per indicare
    # che stiamo per visualizzare l'array.
    print("Contenuto dell'array:")

    # Scorriamo tutti gli elementi dell'array
    # uno alla volta.
    for elemento in array:

        # Stampiamo l'elemento corrente.
        print(elemento)

# Definiamo una funzione chiamata "inverti_array".
# La funzione riceve come parametro un array (lista).
def inverti_array(array):
    # Creiamo un nuovo array vuoto.
    risultato = []

    # Partiamo dall'ultimo elemento dell'array
    # e procediamo verso il primo.
    for i in range(len(array) - 1, -1, -1):

        # Aggiungiamo l'elemento corrente
        # al nuovo array.
        risultato.append(array[i])

    # Restituiamo l'array invertito.
    return risultato