import os
import time

def mostrar_memoria(titulo):
    print("\n" + titulo)
    os.system("free -m")
    os.system("ps -o pid,ppid,%mem,%cpu,cmd -p " + str(os.getpid()))

print("Proceso Python iniciado. PID:", os.getpid())

mostrar_memoria("Estado inicial de memoria:")

print("\nReservando memoria...")
x = [0] * 50000000

mostrar_memoria("Estado después de reservar memoria:")

print("\nEsperando 10 segundos...")
time.sleep(10)

print("\nLiberando memoria...")
del x

mostrar_memoria("Estado después de liberar memoria:")

print("\nPrograma finalizado.")
