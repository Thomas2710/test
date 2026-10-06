


def stampa_array(array):
    # Scorriamo tutti gli elementi dell'array
    # e li stampiamo uno alla volta.
    for elemento in array:
        print(elemento)


def somma_array(array1, array2):
    # Creiamo un nuovo array vuoto.
    # Qui inseriremo i risultati delle somme.
    risultato = []

    # Scorriamo gli indici degli elementi.
    # Usiamo len(array1) perché assumiamo che
    # i due array abbiano la stessa lunghezza.
    for i in range(len(array1)):

        # Sommiamo gli elementi che si trovano
        # nella stessa posizione nei due array.
        somma = array1[i] + array2[i]

        # Aggiungiamo il risultato al nuovo array.
        risultato.append(somma)

    # Restituiamo il nuovo array contenente
    # i risultati delle somme.
    return risultato