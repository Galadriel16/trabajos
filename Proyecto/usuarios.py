import usuarios
import estadisticas

# función que crea un nuevo usuario

def crear_usuario():
    todos = estadisticas.toma_usuario()
    nuevo_usuario = ''
    while True:
        nuevo_usuario = input('Ingrese el nuevo usuario: ')
        if nuevo_usuario in todos:
            print('El usuario ya existe')
        else:
            break
    f = open('usuarios.txt', 'a')
    f.write(nuevo_usuario + '\n')
    f.close()

    return nuevo_usuario

# función que selecciona un usuario ya creado desde el archivo usuarios.txt

def seleccion_usuario():
    todos = estadisticas.toma_usuario()
    if len(todos) == 0:
        print("No hay usuarios disponibles")
        return crear_usuario()
    else:
        print('Digite el número del usuario que desea')
        for i in range(0, len(todos)):
            print(f'{i+1}- {todos[i]}')
    usuario = int(input('Número de usuario: ')) - 1

    return todos[usuario]
