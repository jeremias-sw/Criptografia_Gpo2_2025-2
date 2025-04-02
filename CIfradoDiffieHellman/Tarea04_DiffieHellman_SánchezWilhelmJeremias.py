# Función para verificar si un número es primo
def es_primo(n):
    """Verifica si un número es primo"""
    if n <= 1:  # Los números menores o iguales a 1 no son primos
        return False
    for i in range(2, int(n**0.5) + 1):  # Itera desde 2 hasta la raíz cuadrada de n
        if n % i == 0:  # Si n es divisible por i, no es primo
            return False
    return True  # Si no se encontró divisor, el número es primo

# Función para verificar si un número es una raíz primitiva de un número primo dado
def es_raiz_primitiva(a, p):
    """Verifica si 'a' es una raíz primitiva de 'p'"""
    residuos = set()  # Conjunto para almacenar los residuos únicos
    for i in range(1, p):  # Itera desde 1 hasta p-1
        residuos.add(pow(a, i, p))  # Calcula (a^i) % p y lo agrega al conjunto
    return len(residuos) == p - 1  # Verifica si hay p-1 residuos únicos

# Función para encontrar la primera raíz primitiva de un número primo
def encontrar_raiz_primitiva(p):
    """Encuentra la primera raíz primitiva de 'p'"""
    for g in range(2, p):  # Itera desde 2 hasta p-1
        if es_raiz_primitiva(g, p):  # Verifica si g es una raíz primitiva
            return g  # Retorna la primera raíz primitiva encontrada
    return None  # Retorna None si no se encuentra una raíz primitiva

# Inicio del programa
print("Intercambio de clave segura mediante Diffie-Hellman \n")

# Mensaje de bienvenida
print("Hola, bienvenido al sistema de generación de clave de sesión")

# Solicita el nombre del usuario
nombre = input("\n Ingresa tu nombre: ")

print("\n Selección de datos Públicos \n")

# Validación del número primo
while True:
    # Solicita al usuario un número primo
    p = int(input("Hola " + nombre + " ingresa un número primo, recuerda que debe ser el mismo que el de amigo: "))
    if es_primo(p):  # Verifica si el número ingresado es primo
        break  # Si es primo, sale del bucle
    else:
        # Si no es primo, muestra un mensaje de error y ejemplos de números primos
        print(f"{p} no es un número primo. Por favor, ingresa un número primo. Aquí tienes algunos ejemplos de números primos:")
        print("Ejemplos de números primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29")
        
# Encuentra automáticamente la raíz primitiva del número primo ingresado
a = encontrar_raiz_primitiva(p)
print(f"\nLa raíz primitiva de {p} es: {a}")

print("\n Selección de datos Privados \n")

# Solicita al usuario su clave privada
cprivada = int(input(nombre + " ingresa tu clave privada: "))

# Calcula la clave pública del usuario usando la fórmula (a^clave_privada) % p
cpublica = (a**cprivada) % p
print(nombre + " tu clave pública es: ", cpublica)

# Solicita al usuario la clave pública de su amigo
yb = int(input("\n " + nombre + " ingresa la clave pública de tu amigo: "))

print("\n Clave de sesión \n")

# Calcula la clave de sesión compartida usando la fórmula (clave_publica_amigo^clave_privada) % p
k = (yb**cprivada) % p
print(nombre + " la clave de sesión es: ", k)
