import users.usuarioModelo as usuarioModelo

def buscar(email):
    #[(10, 'name', 'last name', 'email', 'password', datetime.date(2021, 9, 7))]
    buscando = usuarioModelo.User.buscar(email)
    return buscando


def registrarUsuario():
    print('\n-----Datos de usuaio --------')
    nombre = input('Escribe tu nombre:   ')
    apellidos = input('Escribe tus apellidos:   ')
    email = input('Escribe tu email:   ')
    password = input('Escribe tu contraseña:   ')

    buscando = buscar(email)
    
    if len(buscando)!=0:
        return '¡Up! ya exste un usuario con este email'
    else:
        try:
            usuario = usuarioModelo.User(nombre,apellidos,email,password)
            guardar = usuario.guardar()
            return guardar
        except:
            return 'Error al registrar usuario en la bd'

def logiando():
    print('\n-----Datos de usuaio--------')
    email = input('Escribe tu email:   ')
    password = input('Escribe tu contraseña:   ')
    
    buscando = buscar(email)

    if len(buscando)==0:
        return '¡Up! Este usuario no existe'
    else:
        passwordBD = buscando[0][4]
        if passwordBD!=password:
            return ['¡Nop! Contraseña invalida','']
        else:
            return [True,buscando[0][1],buscando[0][0]]
