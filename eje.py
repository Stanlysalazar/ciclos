clave_correcta = 123
intentos_maximos = 3
intentos = 0

while intentos < intentos_maximos:
    clave_ingresada = input("Ingresa la clave: ")
    
    if clave_ingresada == clave_correcta:
        print("¡Clave correcta! Acceso permitido.")
        break  # Salir del ciclo si la clave es correcta
    else:
        intentos += 1
        print("Clave incorrecta. Intento", intentos, "de", intentos_maximos)
        
if intentos == intentos_maximos:
    print("Has excedido el número máximo de intentos. Acceso denegado.")


