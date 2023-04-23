# Ejercicio 5: Notas de clase

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
def promedio(diccionario):
    nombre = diccionario["class"]["student"]["Nombre"]
    fisica = diccionario["class"]["student"]["marks"]["physics"]
    historia = diccionario["class"]["student"]["marks"]["history"]
    mate = diccionario["class"]["student"]["marks"]["math"]
    promedio = (fisica + historia + mate)/3
    return {"Nombre": [nombre], "Promedio": [promedio]}
print(promedio(sampleDict))
