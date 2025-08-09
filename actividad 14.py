def menu():
    print("=======menu principal======")
    print("1. agregar participante ")
    print("2. mostrar participante ordenapo por nombre")
    print("3. mostrar participante ordenado por edad")
    print("4. buscar por nombre si aparece en lista")
    print("5. salir")



class participante:
    def __init__(self,numero, nombre, edad, categoria):
        self.numero=numero
        self.nombre = nombre
        self.edad= edad
        self.categoria = categoria

    def __str__(self):
        return f"numero de dorsal:{self.numero} nombre completo:{self.nombre} edad:{self.edad} categoria: {self.categoria}"


class agr_participante:
    def __init__(self):
        self.participante = []


    def ordenar_numero(self):
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            else:
                pivote = lista[0]
                mayores = [x for x in lista[1:] if x.numero > pivote.numero]
                iguales = [x for x in lista if x.numero == pivote.numero]
                menores = [x for x in lista[1:] if x.numero < pivote.numero]
                return quick_sort(mayores) + iguales + quick_sort(menores)

        self.participante = quick_sort(self.participante)




competencia = agr_participante()
op=0
while op!=5:
    menu()

    op=int(input("ingrese una opcion aejecutar"))
    match op:
            case 1:

                cantidad = int(input("¿Cuántos participantes desea ingresar? "))

                for i in range(cantidad):
                     print(f"\nparticipante #{i + 1}")
                     try:
                            numero= int(input("Ingrese numero de dorsal: "))
                            nombre = input("Ingrese el nombre completo: ")
                            edad = int(input("Ingrese edad: "))
                            categoria = (input("Ingrese categoria: "))

                            participante = participante(numero,nombre, edad, categoria)
                            competencia.agr_paticipante(participante)
                     except ValueError as e:
                            print(f"Error al ingresar datos: {e}")

            case 2:
                break

            case 3:
                break

            case 4:
                break
            case 5:
                  print("fin de programa ")

            case _:
                print("ingrese una opcion valida")


