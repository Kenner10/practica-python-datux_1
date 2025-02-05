###TAREA 2###
class Conductor:
    def _init_(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def agregar_horario(self, horario):
        if horario in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {horario}.")
        else:
            self.horarios.append(horario)
            print(f"Horario {horario} agregado al conductor {self.nombre}.")

    def esta_disponible(self, horario):
        return horario not in self.horarios

class Autobus:
    def _init_(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []
        self.conductor_asignado = None

    def agregar_ruta(self, ruta):
        self.ruta = ruta
        print(f"Ruta {ruta} agregada al bus {self.id_bus}.")

    def agregar_horario(self, horario):
        self.horarios.append(horario)
        print(f"Horario {horario} agregado al bus {self.id_bus}.")

    def asignar_conductor(self, conductor):
        if self.conductor_asignado:
            print(f"El bus {self.id_bus} ya tiene asignado un conductor.")
        else:
            self.conductor_asignado = conductor
            print(f"Conductor {conductor.nombre} asignado al bus {self.id_bus}.")

class Administracion:
    def _init_(self):
        self.autobuses = []
        self.conductores = []

    def agregar_bus(self, id_bus):
        bus = Autobus(id_bus)
        self.autobuses.append(bus)
        print(f"Bus {id_bus} agregado.")

    def agregar_ruta_a_bus(self, id_bus, ruta):
        bus = self.buscar_bus(id_bus)
        if bus:
            bus.agregar_ruta(ruta)
        else:
            print(f"Bus {id_bus} no encontrado.")

    def registrar_horario_a_bus(self, id_bus, horario):
        bus = self.buscar_bus(id_bus)
        if bus:
            bus.agregar_horario(horario)
        else:
            print(f"Bus {id_bus} no encontrado.")

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado.")

    def agregar_horario_a_conductor(self, nombre, horario):
        conductor = self.buscar_conductor(nombre)
        if conductor:
            conductor.agregar_horario(horario)
        else:
            print(f"Conductor {nombre} no encontrado.")

    def asignar_bus_a_conductor(self, id_bus, nombre_conductor):
        bus = self.buscar_bus(id_bus)
        conductor = self.buscar_conductor(nombre_conductor)
        if bus and conductor:
            if conductor.esta_disponible(bus.horarios[0]):
                bus.asignar_conductor(conductor)
                conductor.agregar_horario(bus.horarios[0])
            else:
                print(f"El conductor {nombre_conductor} no está disponible en el horario {bus.horarios[0]}.")
        else:
            print(f"Bus {id_bus} o conductor {nombre_conductor} no encontrado.")

    def buscar_bus(self, id_bus):
        for bus in self.autobuses:
            if bus.id_bus == id_bus:
                return bus
        return None

    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

def menu():
    admin = Administracion()
    while True:
        print("\n--- Menú de Gestión de Buses ---")
        print("1. Agregar bus")
        print("2. Agregar ruta a bus")
        print("3. Registrar horario a bus")
        print("4. Agregar conductor")
        print("5. Agregar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_bus = input("Ingrese el ID del bus: ")
            admin.agregar_bus(id_bus)
        elif opcion == "2":
            id_bus = input("Ingrese el ID del bus: ")
            ruta = input("Ingrese la ruta: ")
            admin.agregar_ruta_a_bus(id_bus, ruta)
        elif opcion == "3":
            id_bus = input("Ingrese el ID del bus: ")
            horario = input("Ingrese el horario (formato HH:MM-HH:MM): ")
            admin.registrar_horario_a_bus(id_bus, horario)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del conductor: ")
            admin.agregar_conductor(nombre)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del conductor: ")
            horario = input("Ingrese el horario (formato HH:MM-HH:MM): ")
            admin.agregar_horario_a_conductor(nombre, horario)
        elif opcion == "6":
            id_bus = input("Ingrese el ID del bus: ")
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            admin.asignar_bus_a_conductor(id_bus, nombre_conductor)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
   menu()