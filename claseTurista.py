class Vehiculo:

    def __init__(self):
        self.capacidadV = self.capacidad()
    def capacidad(self):
        return 6
        
        

class miniBus(Vehiculo):

    def __init__(self):
        super().__init__()
        self.ocupados = 0
        self.capacidadBus = self.capacidad()
        self.asientosLibres =  self.calcularLibres()
        self.pasajeros = []

    def capacidad(self):
        return 5

    def agreagrPasajero(self, idPasajero,nombre, destino):
        pasajero = Pasajero(idPasajero, nombre , destino)
        self.pasajeros.append(pasajero)
        self.ocupados += 1
        self.asientosLibres =  self.calcularLibres()
        return self.hayLugar()
        
    def hayLugar(self):
        if self.ocupados == self.capacidadBus:
            return 1
        else:
            return 0

    def calcularLibres(self):
        return (self.capacidadBus - self.ocupados)

    def estaEnBus(self,idPasajero):
        for i in self.pasajeros:
            if  i.id == idPasajero:
                print(f"Pasajero con id : {i.id} cuyo nombre es {i.nombre} ya esta en el bus")
                return True
    
    def mostrarPasajeros(self):

        print(" ")
        print("_____________________________________________________________________________________")
        print("Listo para irnos !!!!")
        print(" ")
        print(" Lista de Pasajeros/as:  ")
        print("-------------------------------------------------------------------------------------")
        for i in self.pasajeros:
            print(f"Pasajero {i.id} - Nombre: {i.nombre} - Destino: {i.destino}")
            print("-------------------------------------------------------------------------------------")

            
class Pasajero:
    def __init__(self, id ,nombre, destino):
        self.id =  id
        self.nombre = nombre
        self.destino = destino

#____________________________________________________________________________________________________________

rta = True
print("______________________________________________________________________________________________________________")
print("                                          Bienvenido a MI BUS")
print("______________________________________________________________________________________________________________")
miMiniBus = miniBus()

print(f"Asientos libres: {miMiniBus.asientosLibres}")
    
while rta:  

    try:
     idPasajero= int(input(f"Ingrese id de pasajeros [número]: "))

     if (miMiniBus.estaEnBus(idPasajero)):
        continue
     nombre= input(f"Ingrese nombre: ")
     destino= input(f"Ingrese destino: ")
    except ValueError:
        print("Error al ingrear datos - id  debe ser entero")
        continue

    
    add = miMiniBus.agreagrPasajero(idPasajero,nombre,destino)

    if add == 0:
        print("El pasajero se agrego con exito")
        print("-------------------------------------------------------------------------------------")
    elif add == -1:
        print("-------------------------------------------------------------------------------------")
        pass
    elif add == 1:
        miMiniBus.mostrarPasajeros()
        break
    
    print(f"Asientos libres: {miMiniBus.asientosLibres}")
    respuesta = input("Quiere agregar otro pasajero [si] - [no] : ")

    if(respuesta == "SI" or respuesta =="si"):
        rta= True
    else:
        rta=False
        miMiniBus.mostrarPasajeros()


print("BUEN VIAJE  .. :)")