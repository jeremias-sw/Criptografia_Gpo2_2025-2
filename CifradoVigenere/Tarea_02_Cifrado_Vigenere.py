arreglo = [chr(i) for i in range(65, 91)]  # Alfabeto de A a Z

def ajustaClave(mensaje, clave):
    longitud_mensaje = len(mensaje)
    longitud_clave = len(clave)

    if longitud_clave > longitud_mensaje:
        clave = clave[:longitud_mensaje]
    elif longitud_clave < longitud_mensaje:
        clave = (clave * ((longitud_mensaje // longitud_clave) + 1))[:longitud_mensaje]

    return clave  # <-- Devuelve la clave ajustada

def generaCifrado(mensaje, clave):
    cifrado_final = ""
    
    for i in range(len(mensaje)):
        pos_mensaje = arreglo.index(mensaje[i].upper())  
        pos_clave = arreglo.index(clave[i].upper())  
        
        pos_cifrado = (pos_mensaje + pos_clave) % 26
        
        # Añadimos la letra cifrada al resultado
        cifrado_final += arreglo[pos_cifrado]
    
    return cifrado_final

# Solicitar al usuario el mensaje y la clave
mensaje = input("Ingresa tu mensaje (Cualquier letra de la A a la Z, a excepcion de la Ñ y sin espacios): ")
clave = input("Ingresa tu clave (de la A a la Z sin espacios): ")
clave = ajustaClave(mensaje, clave)

# Generar y mostrar el cifrado
print("Mensaje cifrado:", generaCifrado(mensaje, clave))
