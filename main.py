import threading
import time
from queue import Queue

class Nodo:
    def __init__(self, nombre, vecinos):
        self.nombre = nombre
        self.vecinos = vecinos  # {nombre_nodo: costo}
        self.tabla_enrutamiento = {nombre: (nombre, costo) for nombre, costo in vecinos.items()}
        self.tabla_enrutamiento[nombre] = (nombre, 0)  # a sí mismo
        self.inbox = Queue()
        self.lock = threading.Lock()
        self.activo = True

    def enviar_tabla(self):
        for vecino in self.vecinos:
            paquetes = (self.nombre, self.tabla_enrutamiento.copy())
            red[vecino].inbox.put(paquetes)

    def procesar_paquetes(self):
        while not self.inbox.empty():
            origen, tabla_vecino = self.inbox.get()
            actualizado = False

            for destino, (next_hop, costo) in tabla_vecino.items():
                nuevo_costo = costo + self.vecinos[origen]
                if destino not in self.tabla_enrutamiento or nuevo_costo < self.tabla_enrutamiento[destino][1]:
                    self.tabla_enrutamiento[destino] = (origen, nuevo_costo)
                    actualizado = True

            if actualizado:
                self.enviar_tabla()

    def run(self):
        self.enviar_tabla()
        while self.activo:
            self.procesar_paquetes()
            time.sleep(1)

    def imprimir_tabla(self):
        with self.lock:
            print(f"🔗 Tabla de enrutamiento de {self.nombre}:")
            for destino in sorted(self.tabla_enrutamiento):
                next_hop, costo = self.tabla_enrutamiento[destino]
                print(f"  Destino: {destino}, Vía: {next_hop}, Costo: {costo}")
            print("-" * 40)

# Crear red
red = {
    'A': Nodo('A', {'B': 1, 'C': 5}),
    'B': Nodo('B', {'A': 1, 'C': 2, 'D': 1}),
    'C': Nodo('C', {'A': 5, 'B': 2, 'D': 2}),
    'D': Nodo('D', {'B': 1, 'C': 2}),
}

# Lanzar nodos
hilos = []
for nodo in red.values():
    hilo = threading.Thread(target=nodo.run)
    hilo.start()
    hilos.append(hilo)

# Dejar que converja (simulación de RIP)
time.sleep(10)

# Mostrar tablas
for nodo in red.values():
    nodo.activo = False
    nodo.imprimir_tabla()

# Esperar a que terminen los hilos
for hilo in hilos:
    hilo.join()