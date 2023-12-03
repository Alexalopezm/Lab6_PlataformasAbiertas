import time
import random
from eventos import EventManager

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()

    def generate_real_time_data(self):
        old_data = dict(self.data)  # Guardar copia de los datos antes de la actualización
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

        # Notificar cambios solo si los datos han cambiado
        if old_data != self.data:
            self.event_manager.notify("datos_actualizados", self.data)

# Crear una instancia
real_time_data_manager = RealTimeDataManager()

# Función de callback para imprimir los datos actualizados
def print_updated_data(data):
    print(f"Datos en tiempo real actualizados: {data}")

# Suscribir la función de callback al evento 'datos_actualizados'
real_time_data_manager.event_manager.subscribe("datos_actualizados", print_updated_data)

# Actualizaciones en tiempo real en segundo plano
import threading
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")