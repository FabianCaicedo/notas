import users.usuarioFunciones as usuarioFunciones
import notes.notaFunciones as notaFunciones

def iniciar():
    
    print('----------Bienvenido -----------')
    print('Que deseas hacer?  \n   Crear usuario (registrarme) \n   Iniciar sesion (acceder)')
    opcion=input('Deseo:   ')
    
    if opcion!='registrarme' and opcion!='acceder':
        print('Opcion invalida')
    else:
        if opcion == 'registrarme':
            registrarUser = usuarioFunciones.registrarUsuario()
            print(registrarUser)
        else:
            login = usuarioFunciones.logiando()
            if login[0] != True:
                print(login)
            else:
                idUser = login[2]
                print(f'\n-------Bienvenido {login[1]} ------')
                accion=''
                while accion !='salir':
                    print('\n   <<<--menu-->>>')
                    print('   Crear nota (crear) \n   Mostrar Notas (mostrar) \n   Eliminar nota (eliminar) \n   Salir (salir)')
                    accion = input('¿Qué deseas aparte de fama y riquesa?:  ')
                    
                    if accion == 'crear':
                        registrarNote = notaFunciones.registrarNota(idUser)
                        print(registrarNote)
                    elif accion == 'mostrar':
                        notas = notaFunciones.mostrarTodas()
                        for nota in notas:
                            print(f'{nota[2]} => {nota[3]}  \n')
                    elif accion == 'eliminar':
                        notas = notaFunciones.mostrarTodas()
                        for nota in notas:
                            print(f'{nota[2]}')
                        notaEliminada = input("¿Cual nota va a eliminar?   ")
                        eliminar = notaFunciones.eliminarNota(notaEliminada)
                        print(eliminar)
                    elif accion == 'salir':
                        print('Adios ')
                    else:
                        print('Accion invalida')

    

iniciar()