# importer math for senere at bruge funktionen ceil. Denne funktion runder værdien op til nærmeste hele tal.
#global a er længden som gennem i denne variabel
import math
global a

#############################################################################################################

# menu giver brugeren valgmuligheden for at vælge single mode, multi mode eller at stoppe denne beregner.
def menu():
    global valg
    global x
    global y
    print('''
    1 - SM
    2 - MM
    0 - STOP BEREGNER''')
    valg=int(input())
    if valg==1:
        x=0.35
        y=0.2
        return længde()
    elif valg==2:
        x=2.5
        y=0.6
        return længde()
    elif valg==0:
        return stop()

#længden indtastes her, hvis der er valgt multimode og længden smatidig overskrider 2 km vil en tekst fremkomme samt brugeren returneres til menu.
# Ellers returneres der til statet passiver.
def længde():
    global a
    print('indtast længden på strækningen')
    a=int(input())
    if valg==2 and a>2:
        print('Overskrider 2km, vælg en SM')
        return menu()
    else: return Passiver()

#passiver er et state hvor brugeren skal indtaste antal konnekteringer og splidsninger, ydermere bruges math funktionen her sammen med længden af fiberen,
#til at fastlægge en reparations margin.
def Passiver():
    global sikkerhed
    global splids
    global kon, rep
    print('antal konnektore')
    kon=int(input())*0.5
    print('antal splidsninger')
    splids=int(input())*0.1
    sikkerhed=3
    rep=(math.ceil(a/10)*0.5)
    print('repmargin',rep,'dB')
    if valg==1:
        return sm_udregn()
    if valg==2:
        return mm_udregn()

#udregner hvor stort overskud der skal være meller SFP sender og modtager på 850nm samt 1300nm,
#der returneres til menu
def mm_udregn():
    print('for at kunne klare strækningen skal sfp modulerne have et brutto overskud på:')
    B850=splids+kon+(a*x)+sikkerhed+rep
    print('850nm =','%4.2f'%B850,'dB')
    B1300=splids+kon+(a*y)+sikkerhed+rep
    print('1300nm =','%4.2f'%B1300,'dB')
    return menu()

#udregner hvor stort overskud der skal være meller SFP sender og modtager på 850nm samt 1300nm,
#der returneres til menu
def sm_udregn():
    print('for at kunne klare strækningen skal sfp modulerne have et brutto overskud på:')
    B1310=splids+kon+(a*x)+sikkerhed+rep
    print('1310nm =','%4.2f'%B1310,'dB')
    B1550=splids+kon+(a*y)+sikkerhed+rep
    print('1550nm =','%4.2f'%B1550,'dB')
    return menu()

#stop statet printer en tekst og returnere til None som i dette program stopper beregneren.
def stop():
    print('beregneren er stoppet')
    return None
state=menu()
while state: state=menu()

