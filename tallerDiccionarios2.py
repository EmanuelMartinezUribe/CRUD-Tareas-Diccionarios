tareas = {
    "01" : {
        "descripcion" : "Levantamiento de requisitos",
        "estado" : "pendiente",
        "tiempo" : 60
    },
    "02" : {
        "descripcion" : "Programacion de Citas medicas",
        "estado" : "pendiente",
        "tiempo" : 180
    },
    "03" : {
        "descripcion" : "CRUD Clientes",
        "estado" : "pendiente",
        "tiempo" : 50
    }
}

def read(tareas):
    for identificador, tarea in tareas.items():
        print(identificador, "-", end="")
        for clave, valor in tarea.items():
            print(f"{valor}, ", end="")
        print()
    
def estaElemento(identificador, tareas):
    claves = tareas.keys()
    if identificador in claves:
        return True
    else:
        return False

def create(tareas, identificador, tareaNueva):
    tareas[identificador] = tareaNueva 
    return tareas

def update(tareas, identificador, tareaActualizada):
    tareas[identificador] = tareaActualizada
    return tareas

def delete(tareas, identificador):
    del(tareas[identificador])
    return tareas

while True:
    print(" ")
    print("-- Aplicacioon CRUD Tareass Pendientes ---")
    print("1. Adicionar Tarea")
    print("2. Listar Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
    opcion = int(input("Ingresa una opcion: "))
    #Create
    if opcion == 1:
        print()
        print("->Adicionar Tarea")
        while True:
            identificador = input("Ingrese identificador de la Tarea:")
            if estaElemento(identificador, tareas):
                print("Este identificador ya existe, utilice otro... ")
            else:
                break
        descripcion = input("Ingrese descripcion Tarea: ")
        estado = input("Ingrese estado Tarea: ")
        tiempo = int(input("Ingrese tiempo Tarea: "))

        tareaNueva={
            "descripcion":descripcion,
            "estado":estado,
            "tiempo":tiempo
        }


        tareas = create(tareas, identificador, tareaNueva)
        print(f"Tarea {identificador} creada con exito !!")
    #Read
    elif opcion == 2:
        print()
        print("Listado de tareas")
        read(tareas)
    #Update
    elif opcion == 3:
        print()
        print("->Actualizar Tarea")
        while True:
            identificador = input("Ingrese identificador de la Tarea: ")
            if estaElemento(identificador, tareas):
                break
            else:
                print("Este identificador no existe, utilice otro... ")
        descripcion = input("(No ingrese nada para que sea la misma)  - Ingrese nueva descripcion Tarea: ")
        estado = input("Ingrese nuevo estado Tarea: ")
        tiempo = int(input("Ingrese nuevo tiempo Tarea: "))

        if descripcion == "":

            tareaActualizada={
            "descripcion":tareas[identificador]["descripcion"],
            "estado":estado,
            "tiempo":tiempo
        }

        else:
            tareaActualizada={
                "descripcion":descripcion,
                "estado":estado,
                "tiempo":tiempo
            }


        tareas = update(tareas, identificador, tareaActualizada)
        print(f"Tarea {identificador} actualizada con exito !!")
    #Delete
    elif opcion == 4:
        while True:
            identificador = input("Ingrese el identificador de la tarea que desea borrar: ")
            if identificador in tareas:
                tareas = delete(tareas, identificador)
                print("Tarea eliminada con exito")
                break
            else:
                print("Ese identificador no existe")

    #Exit
    elif opcion == 5:
        print("Has salido exitosamente")
        break
    else:
        print("Ingrese una opcion valida")

    