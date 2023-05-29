# # Ejercicio 5: Notas de clase. Se promedia la nota del estudiante de acuerdo con la información que aparece asignada previamente.

# # datos brindados previamente en el sistema
# sampleDict = {
#     "class": {
#         "student": {
#         "Nombre": "Mike",
#         "marks": {
#             "physics": 70,
#             "history": 80,
#             "math": 90
#             },
#         }
#     }
# }

# # función que promedia la información brindada anteriormente, misma que se incluye en un diccionario
# def promedio(diccionario):
#     nombre = diccionario["class"]["student"]["Nombre"]
#     fisica = diccionario["class"]["student"]["marks"]["physics"]
#     historia = diccionario["class"]["student"]["marks"]["history"]
#     mate = diccionario["class"]["student"]["marks"]["math"]
#     promedio = (fisica + historia + mate)/3
#     return {"Nombre": [nombre], "Promedio": [promedio]}
# print(promedio(sampleDict))


# Ejercicio con cambio al incluir lambda, así como funciones map() y filter()
sampleDict = {
    "class": {
        "student": {
            "Nombre": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
                "math": 90
            },
        }
    }
}

# se agrega una funcionalidad adicional utilizando filter(), map(), y lambda(). 
def promedio(diccionario):
    nombre = diccionario["class"]["student"]["Nombre"]
    calificaciones = diccionario["class"]["student"]["marks"]
    #Se calcula el promedio de todas las calificaciones del estudiante. 
    promedio = sum(calificaciones.values()) / len(calificaciones)
    
    # se utiliza filter() junto con una función lambda para filtrar las asignaturas con una calificación superior a 80.
    calificaciones_filtradas = filter(lambda x: calificaciones[x] > 80, calificaciones.keys())
    # map() se utiliza con una función lambda para capitalizar los nombres de las asignaturas filtradas.
    asignaturas_filtradas = map(lambda x: x.capitalize(), calificaciones_filtradas)
    
    #diccionario que contiene el nombre del estudiante, el promedio de las calificaciones y la lista de asignaturas aprobadas (filtradas y capitalizadas).
    return {"Nombre": nombre, "Promedio": promedio, "Asignaturas Aprobadas": list(asignaturas_filtradas)}

print(promedio(sampleDict))

# Ejemplo:
# "Nombre": "Luis",
#            "marks": {
#                "physics": 25,
#                "history": 72,
#                "math": 68