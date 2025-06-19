import time
import random

tiempo = random.uniform(0,10)
time.sleep(tiempo)

principio = time.time()
input("AHORA!!")
final = time.time()
tiempo_reaccion = final - principio
if tiempo_reaccion < 10:
    print(f"Has tardado {tiempo_reaccion} segundos!")
else: 
    print(f"Has tardado {tiempo_reaccion} segundos!! Eres lentisimo primo.")