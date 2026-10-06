# main.py

# Importiamo la funzione "stampa_array"
# dal file "array_generator.py".
from array_generator import stampa_array, inverti_array


# Creiamo un array (lista) di numeri.
array = [10, 20, 30, 40, 50]


# Chiamiamo la funzione "stampa_array"
# passando il nostro array come parametro.
stampa_array(array)
array_invertito = inverti_array(array)
# Stampiamo l'array invertito
print("Array invertito:")
stampa_array(array_invertito)
