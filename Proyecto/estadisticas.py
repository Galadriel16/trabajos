import estadisticas

# función que permite agregar un usuario al archivo txt para registrar el mismo

def toma_usuario():
    archivo = open('usuarios.txt', 'r')
    usuariolista = []
    for line in archivo:
        usuariolista.append(line.rstrip('\n'))
    archivo.close()
    return usuariolista

# archivo que agregar el estado si ganó o perdió el jugador 

def agrega_estadist(usuario, resulta):
    filename = usuario.replace(' ', '').lower()
    # escribe un nuevo archivo
    archivo = open(f'{filename}-estadísticas.txt', 'a')
    archivo.write(f'{usuario} {resulta}\n')
    archivo.close()