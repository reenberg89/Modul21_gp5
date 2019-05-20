#Impoterer LED fra GPIO, fordi der kun bruges LED Funktionen fra biblioteket
#Impoterer sleep fra time, for at holde programmet i et stadie i noget tid før det forsætter
#LED(x) henviser til udgang x på breakout boardet
#def (navn)(): laver en subroutine der kan kaldes, frem for at skrive den samme kode flere gange
#return retunerer til det forgående stadie for def blev kaldt
#rød=LED(22) giver udgang 22 navnet gron
#rød.on/rød.off tænder og slukker udgang 22
#sleep(5) holder stadiet i 5 sekunder
def gron_rod():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state1')
    grøn.on()
    grøn1.off()
    gul.off()
    gul1.off()
    rød.off()
    rød1.on()
    sleep(5)
    return 

def gul_rod():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state2')
    grøn.off()
    grøn1.off()
    gul.on()
    gul1.off()
    rød.off()
    rød1.on()
    sleep(2)
    return

def rod_rod():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state3')
    grøn.off()
    grøn1.off()
    gul.off()
    gul1.off()
    rød.on()
    rød1.on()
    sleep(1)
    return

def rod_rodgul():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state4')
    grøn.off()
    grøn1.off()
    gul.off()
    gul1.on()
    rød.on()
    rød1.on()
    sleep(2)
    return 

def rod_gron():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state5')
    grøn.off()
    grøn1.on()
    gul.off()
    gul1.off()
    rød.on()
    rød1.off()
    sleep(2)
    return

def rod_gul():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state6')
    grøn.off()
    grøn1.off()
    gul.off()
    gul1.on()
    rød.on()
    rød1.off()
    sleep(2)
    return 

def rod_rod1():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state7')
    grøn.off()
    grøn1.off()
    gul.off()
    gul1.off()
    rød.on()
    rød1.on()
    sleep(1)
    return 

def rodgul_rod():
    from gpiozero import LED
    from time import sleep
    rød=LED(22)
    rød1=LED(6)
    gul=LED(27)
    gul1=LED(5)
    grøn=LED(17)
    grøn1=LED(0)
    print('state8')
    grøn.off()
    grøn1.off()
    gul.on()
    gul1.off()
    rød.on()
    rød1.on()
    sleep(2)
    return