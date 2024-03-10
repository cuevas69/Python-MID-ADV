#listas
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

print("Lista de frutas después de eliminar:", frutas)
print("Elemento eliminado:", eliminado)

#diccionarios
mi_dict = {"valores_1": {"v1": 3, "v2": 6}, "puntos": {"points1": 9, "points2": [10, 300, 15]}}
def obtener_segundo_elemento(diccionario):
    try:
        return diccionario["puntos"]["points2"][1]
    except (KeyError, IndexError):
        return None


print(obtener_segundo_elemento(mi_dict))

#update
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic.update({
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
})

# Muestra el diccionario actualizado en pantalla
print(mi_dic)