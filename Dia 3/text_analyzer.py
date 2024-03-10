texto = input("Ingresa un texto a elección: ")
#array de letras
letras = []

#convertir texto en minusculas
texto = texto.lower()

#añadir al array de letras un elemento ingresado por teclado
letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))

#salto de linea
print("\n")
print("CANTIDAD DE LETRAS")
#contar las letras del array letras disponibles en la variable texto
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

#imprimir en consola la busqueda de letras en el texto
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
#contar las palabras que hay en la frase introducida en variable texto
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
#letra del principio y letra del final
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
#invertir texto
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
#boolean para encontrar la palabra Python en texto mediante un diccionario
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")