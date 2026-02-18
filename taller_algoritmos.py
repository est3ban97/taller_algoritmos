import time
import tracemalloc


# Parte 1 - Complejidad O(1) 


def es_par(n):
    return n % 2 == 0  

def ultimo_digito(n):
    return n % 10      

def mayor(a, b):
    return a if a > b else b  

def busqueda_binaria(lista, valor):
    izquierda, derecha = 0, len(lista) - 1
    comparaciones = 0
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista[medio] == valor:
            return medio, comparaciones
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones


# Parte 2 - Mejor, promedio y peor caso


def busqueda_lineal(lista, valor):
    comparaciones = 0
    for i, elem in enumerate(lista):
        comparaciones += 1
        if elem == valor:
            return i, comparaciones
    return -1, comparaciones

def insertar_ordenado(lista, valor):
    i = 0
    while i < len(lista) and lista[i] < valor:
        i += 1
    lista.insert(i, valor)
    return lista


# Parte 3 - Medición y comparación


def medir_busquedas(n):
    lista = list(range(n))
    valor = n + 1  
    # Lineal
    inicio = time.perf_counter()
    busqueda_lineal(lista, valor)
    t_lineal = time.perf_counter() - inicio
    
    # Binaria
    inicio = time.perf_counter()
    busqueda_binaria(lista, valor)
    t_binaria = time.perf_counter() - inicio
    
    return n, t_lineal*1000, t_binaria*1000

def cuadrados_lista(n):
    return [i**2 for i in range(1, n+1)]

def cuadrados_generador(n):
    for i in range(1, n+1):
        yield i**2

def medir_memoria(n):
    tracemalloc.start()
    lista = cuadrados_lista(n)
    mem_lista = tracemalloc.get_traced_memory()[1] / (1024*1024)
    tracemalloc.stop()

    tracemalloc.start()
    gen = list(cuadrados_generador(n))
    mem_gen = tracemalloc.get_traced_memory()[1] / (1024*1024)
    tracemalloc.stop()

    return mem_lista, mem_gen


# Menú 

def menu():
    while True:
        print("\n--- Taller: Complejidad y Eficiencia ---")
        print("1. Operaciones O(1)")
        print("2. Búsqueda binaria (O(log n))")
        print("3. Búsqueda lineal (mejor/promedio/peor caso)")
        print("4. Inserción en orden")
        print("5. Comparar búsqueda lineal vs binaria")
        print("6. Comparar uso de memoria (lista vs generador)")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            n = int(input("Ingresa un número: "))
            print("¿Es par?:", es_par(n))
            print("Último dígito:", ultimo_digito(n))
            a, b = map(int, input("Ingresa dos números separados por espacio: ").split())
            print("Mayor:", mayor(a, b))
        
        elif opcion == "2":
            lista = list(range(1, 21))
            valor = int(input("Valor a buscar en lista 1..20: "))
            idx, comp = busqueda_binaria(lista, valor)
            print("Resultado:", idx, "Comparaciones:", comp)
        
        elif opcion == "3":
            lista = list(range(1, 11))
            print("Mejor caso:", busqueda_lineal(lista, 1))
            print("Promedio:", busqueda_lineal(lista, 5))
            print("Peor caso:", busqueda_lineal(lista, 11))
        
        elif opcion == "4":
            lista = [1,2,3,4,5]
            valor = int(input("Número a insertar en [1,2,3,4,5]: "))
            print("Lista resultante:", insertar_ordenado(lista, valor))
        
        elif opcion == "5":
            for n in [1000, 10000, 100000]:
                tam, t_lin, t_bin = medir_busquedas(n)
                print(f"n={tam}, Lineal={t_lin:.4f} ms, Binaria={t_bin:.4f} ms")
        
        elif opcion == "6":
            n = int(input("Ingresa tamaño n (ej: 100000): "))
            mem_lista, mem_gen = medir_memoria(n)
            print(f"Lista: {mem_lista:.2f} MB")
            print(f"Generador: {mem_gen:.2f} MB")
        
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
