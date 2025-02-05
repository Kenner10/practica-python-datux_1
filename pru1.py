class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de horarios asignados (ejemplo: [(8, 16), (16, 20)])

    def agregar_horario(self, inicio, fin):
        nuevo_horario = (inicio, fin)
        for h in self.horarios:
            if max(h[0], nuevo_horario[0]) < min(h[1], nuevo_horario[1]):
                return False
        self.horarios.append(nuevo_horario)
        return True