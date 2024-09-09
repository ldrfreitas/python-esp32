from machine import Pin
import time

pir_sensor = Pin(2, Pin.IN)
rele = Pin(4, Pin.OUT)  

estado_anterior = pir_sensor.value()
inicio_periodo = time.time()

def monitorar_movimento():
    global estado_anterior

    while True:
        pir_status = pir_sensor.value()
        tempo_atual = time.time()

        if pir_status != estado_anterior:
            if estado_anterior == 1:
                rele.off()  
            else:
                rele.on() 
            
            estado_anterior = pir_status

        time.sleep(0.1)

monitorar_movimento()
