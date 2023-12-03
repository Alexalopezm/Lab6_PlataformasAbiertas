# Lab6_PlataformasAbiertas
## Universidad de Costa Rica
### IE 0117 - Programación Bajo Plataformas Abiertas
#### Laboratorio 6: Callbacks y Lambda (segundo ciclo del 2023)

- Alexa López Marcos, B94353

# Código `datamanager.py`
Este código depende el código eventos.py para su correcta función.
- `DataRealTimeDataManager`: Clase principal que gestiona la generación de datos en tiempo real.
- `start_real_time_updates()`: Inicia las actualizaciones en tiempo real.
- `generate_real_time_data()`: Genera datos aleatorios de temperatura y humedad.
- `print_updated_data(data)`: Función de callback que imprime los datos actualizados en la consola.
- `EventManager`: Gestiona la suscripción y notificación de eventos.

# Código `eventos.py`
- `subscribe(event, callback)`: Permite suscribir una función de callback a un evento específico.
- `unsubscribe(event, callback)`: Cancela la suscripción de una función de callback a un evento.
- `notify(event, data=None)`: Notifica a todas las funciones de callback suscritas sobre la ocurrencia de un evento.

# Código `calc.py`
- `get_user_input()`: Función que solicita al usuario dos números y una operación.
- `ejecutar_operacion(user_input, callback)`: Ejecuta la operación seleccionada según los números ingresados.
- `main()`: Función principal que maneja el flujo del programa.
- `operations`: Diccionario que mapea cada operación a su respectiva función lambda.

# Resultados
## Callbacks
Los resultados al ejecutar el código `datamanager.py` es un print con actualizaciones constantes impresas en la consola por el código `eventos.py`, estos códigos son dependientes entre si y solo se ejecuta `datamanager.py`

## Lambda
Los resultados de ejecutar el código `eventos.py` son un un tipo de menu interactivo con el usuario, que le permite ingresar los 2 numeros con los que se va a realizar la operacion y el signo que corresponde a la accrion a realizar.

