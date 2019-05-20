#Impoterer LED fra GPIO, fordi der kun bruges LED Funktionen fra biblioteket
#Impoterer sleep fra time, for at holde programmet i et stadie i noget tid før det forsætter
#LED(0) henviser til udgang 0 på breakout boardet
#def (navn)(): laver en subroutine der kan kaldes, frem for at skrive den samme kode flere gange
#return retunerer til det forgående stadie for def blev kaldt
#gron=LED(0) giver udgang 0 navnet gron
#gron.on/gron.off tænder og slukker udgang 0
#sleep(3) holder stadiet i 3 sekunder
def DØR():
    from gpiozero import LED
    from time import sleep
    gron=LED(0)
    rod2=LED(22)
    rod=LED(6)
    gul2=LED(27)
    gul=LED(5)
    gron2=LED(17)
    sleep(1)
    gron.on()
    rod.off()
    gul.off()
    gron2.off()
    gul2.off()
    rod2.off()
    sleep(3)
    gron.off()
    return