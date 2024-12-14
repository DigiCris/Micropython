from machine import Pin
from time import sleep

l_roj1 = Pin(5, Pin.OUT)
l_amr1 = Pin(4, Pin.OUT)
l_ver1 = Pin(0, Pin.OUT)
l_roj2 = Pin(14, Pin.OUT)
l_amr2 = Pin(12, Pin.OUT)
l_ver2 = Pin(13, Pin.OUT)

def semaforo():
#inicio 1
    l_roj1.on()
    l_amr1.off()
    l_ver1.off()
    #-----------
    l_roj2.off()
    l_amr2.off()
    l_ver2.on()
    sleep(4)
#prendo amarillo2
    l_amr2.on()
    sleep(.3)
#prendo amarillo1
    l_amr1.on()
    sleep(.2)
#apago amarillo2 y verde2
#enciendo rojo2    
    l_amr2.off()
    l_ver2.off()
    l_roj2.on()
    sleep(.8)
#apago rojo1 y amarillo1
#prendo verde1
    l_roj1.off()
    l_amr1.off()
    l_ver1.on()
    sleep(4)
#----------------------
#prendo amarillo1
    l_amr1.on()
    sleep(.3)
#prendo amarillo2
    l_amr2.on()
    sleep(.2)
#apago amarillo1 y verde1
#enciendo rojo1
    l_amr1.off()
    l_ver1.off()
    l_roj1.on()
    sleep(.8)

while True:
    semaforo()
    