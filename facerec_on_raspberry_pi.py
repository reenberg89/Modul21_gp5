# Programmet-  1.Kigger ned i databasen efter kendte ansigter 2. Ved tryk på knap, begynder at tage billeder som sammenlignes med de
# kendte ansigter fra databasen 3. Ansigt bliver genkendt og et sikkerhedsniveau bliver læst 4. Funktion fortages alt efter
# sikkerhedsniveau 5. Retunerer til standby

#For at programmet kan fungerer skal der importeres nogle subroutiner og laves nogle definationer:
#Impoterer sleep fra time, for at holde programmet i et stadie i noget tid før det forsætter
#impoterer button fra GPIO, for at holde programmet indtil der trykkes på en knap
#impoterer face_recognition, ansigtsgenkendelses som indlæser ansigter fra databasen, som der sammenlignes med kameraet
#impoterer picamera, kamera opsætning
#impoterer np fra numpy, anvendes som del af ansigtsgenkendelsespakken
#impoterer smtplib, anvendes til mail program
#impoterer config, specificere hvilken mail der sendes til og hvilken mail der logges ind med for at sende
#impoterer datetime, for at få tid og dato til logfilen
#impoterer test, for at få adgang til lysreguleringsprogrammet
#impoterer dør, for at få adgang til dør adgangsprogrammet
#def (navn)(): laver en subroutine der kan kaldes, frem for at skrive den samme kode flere gange
#return retunerer til det forgående stadie for def blev kaldt
#startknap=Button(18), ændre kaldenavnet til startknap

#Ekstra kode:
#hvis der er scripts der skal tilgåes fra lokationer uden for main scriptet kan man anvende sys for at tilgå dem, fx fra Desktop
    #import sys
    #sys.path.insert(0, '/home/pi/Desktop')
#from time import sleep
    #fylder mindre end time, da den kun anvender sleep fungtionen
#camera.framerate = 24
#camera.start_preview(fullscreen=True)
#import os


from gpiozero import Button
import face_recognition
import picamera
import numpy as np
import time
import smtplib
import config
import datetime
import test
import dør
startknap=Button(18)

#####################################################################################################

#Mail program
#Forbinder til gmail server
#kalder mail login og password fra config
#tilføjer modtager mail fra config
#kalder titel og besked fra Subject og msg
def send_email(subject, msg):
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS_rx, message)
        server.quit()
        print("Mail sendt til admin")

    except:
        print("Fejl mail ikke sendt")
        
#####################################################################################################

#Standby program
#Sætter sikkerhedsniveau tilbage til 0, bruges til at adskille funktioner fra forskellige brugere
#Venter på startknap
#Åbner kamera vindue efter startknap er trykket
#Retunerer til genkend 
def standby():
    camera.stop_preview()
    print ("Stanby")
    Niveau=0
    print('klar')
    startknap.wait_for_press()
    print('Kig i kameraet')
    print('Tager billede om 5 sekunder')
    camera.start_preview(fullscreen= False, window=(100,100,800,600))
    time.sleep (3)
    return genkend()

#####################################################################################################
#Genkend program
#Sætter sikkerhedsniveau til x, bruges til at adskille funktioner fra forskellige brugere
#Niveau, name, y og v er globale så de kan bruges flere steder
#Programmet er opsat i loop, så der prøves igen indtil der enter er fundet et kendt ansigt eller der er prøvet 10 gang
#Bliver der registreret et ukendt ansigt, forsøger den igen som normalt, bliver der registrerert ukendt ansigt 3 gang
# skrives der fejl og der retuneres til Fault
#Bliver et ansigt genkendt, sættes name og Niveau, og der retuneres til log programmet
def genkend():
    global Niveau
    global name
    global y
    global v
    y = 0
    v = 0    
    while True:    
        v=v+1
        time.sleep (2)
        if v==10:
                v=0
                return standby()

        camera.capture(output, format="rgb")

        face_locations = face_recognition.face_locations(output)
        print("Fundet {} ansigter i billedet.".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(output, face_locations)
        
        print(v,y)
 
        for face_encoding in face_encodings:
             
            match = face_recognition.compare_faces([biden_face_encoding], face_encoding)
            match1 = face_recognition.compare_faces([jan_face_encoding], face_encoding)
            match2 = face_recognition.compare_faces([emil_face_encoding], face_encoding)
            name = "<Unknown person>"           
            
            if match[0]:
                name = "biden"
                Niveau = 1
                print (name,"sikkerhedsniveau ",Niveau)
            
                return log()

            if match1[0]:
                name = "Jan  "
                Niveau = 2
                print (name,"sikkerhedsniveau ", Niveau)
                return log()
                     
            if match2[0]:
                name = "Emil "
                Niveau = 3
                print (name,"sikkerhedsniveau ", Niveau)
                return log()
            
            print("Registreret {}!".format(name))
        
            if name=="<Unknown person>":
                v=0
                y=y+1
                if y<3:
                    print ("Prøver igen")
                    
                else:
                    print('Fejl')
                    return fault()

#####################################################################################################

#Fault program
#Tager et billede af personen der forsøger at komme ind uden adgang
#Sender mail med overskriften "Advarsel" og beskeden "forsøg på uautoriseret adgang"
#Retunere til standby
def fault():
    print('Adgang ikke godkendt')
    time.sleep (1)
    camera.capture('/home/pi/Desktop/billeder/ukendt.jpg')
    subject ="Advarsel"
    msg="forsog paa uautoriseret adgang"
    send_email(subject, msg)   
    return standby()

#####################################################################################################

#Log program
#Opretter en tekstfil med navnet log i mappen billeder på skriveborderet
#Åbner log og skriver navn, sikkerhedsniveau og dato/tid, som den får fra genkend, i filen
#'/n', gør at hver ny indtastning fortagers på den næste linje i filen
#lukker log filen
#Retunere til et program alt efter hvilket sikkerhedsniveau der er sat
def log():
    print('Adgang skrevet til logfil')
    f= open("/home/pi/Desktop/billeder/log.txt", "a+")
    output="%(name)s       %(Niveau)s       %(datetime.datetime.now())s" %{'name': name, 'Niveau':Niveau, 'datetime.datetime.now()':datetime.datetime.now()}
    f.write(output + '\n')
    f.close()
    if Niveau==1:
        return Dør()
    elif Niveau==2:
        return gul()
    elif Niveau==3:
        return regulering()
    
#####################################################################################################

#Dør program
#Åbner DØR fra dør.py
#Retunerer til standby
def Dør():
    print('Adgangsniveau godkendt, dør åben')
    dør.DØR()
    return standby()

#####################################################################################################

#""Niveau2"" program
#gør et eller andet
#Retunerer til standby
def gul():
    print('gør noget... wauw')
#    os.system ("ls")
#    os.system("minecraft-pi")
#    minecraft
    return standby()

#####################################################################################################

#Lysregulering program
#Åbner alle def fra test, fx gron_rod som køre igennem og retunerer til regulering, derefter køres den næste i rækken
#Når o bliver større end 2 stopper kaldet til test.py
#Retunerer standby
def regulering():
    print('Lysregulering starter')
    o=0
    while o<2:
        o=o+1
        test.gron_rod()
        test.gul_rod()
        test.rod_rod()
        test.rod_rodgul()
        test.rod_gron()
        test.rod_gul()
        test.rod_rod1()
        test.rodgul_rod()
    return standby()

#####################################################################################################

#Opstartsfase
#Definerer pi kameraet som camera
#bestemmer opløsningen på kameraet
#Output anvendes til ansigtsgenkendelse
#Gemmer kendte ansigter, så de kan kaldes når kameraet tager billeder
#Køre standby programmet
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

print("Loader kendte ansigter...")
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
print ("25%")
jan_image = face_recognition.load_image_file("jan.jpg")
jan_face_encoding = face_recognition.face_encodings(jan_image)[0]
print ("66%")
emil_image = face_recognition.load_image_file("emil.jpg")
emil_face_encoding = face_recognition.face_encodings(emil_image)[0]
print ("98%")
face_locations = []
face_encodings = []

state=standby()
while state: state=state

#####################################################################################################