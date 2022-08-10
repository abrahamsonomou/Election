from os import system,name
from time import sleep

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

sonomou=0
josias=0
bulletin_nul=0
nombre_bulletin=0
liste={
    '1':'SONOMOU Abraham Sékou',
    '2':'AZIABOU Josias'
}

nbinscrit=int(input('Donner le nombre d''inscrits: '))
sleep(1)
clear()
def menuChoix():
    print('1 pour SONOMOU Abraham Sékou')
    print('2 pour AZIABOU Josias')
    print('0 pour bulletin nul')

compteur=0
while compteur< nbinscrit:
    nombre_bulletin+=1
    menuChoix()
    verification_choix=True
    while verification_choix:
        choix=int(input('Faite votre choix: '))
        clear()
        if( choix >2 or choix <0):
            print("\n")
            print("\t\tVotre choix est incorrecte, veuillez reprendre s'il-vous-plait !:  \n")
            menuChoix()
            verification_choix=True
        else:
            verification_choix=False
    
    if choix==1:
        sonomou+=1
    elif choix==2:
        josias+=1
    else:
        bulletin_nul+=1
    compteur+=1

clear()
suffrageValablementExprime=compteur-bulletin_nul

pourcentageSonomou=(sonomou/suffrageValablementExprime)*100
pourcentageJosias=(josias/suffrageValablementExprime)*100

print("\t Les statistiques du vote")
print('Nombre d''inscrits :',nbinscrit)
sleep(1)
print('Total votant :',compteur)
sleep(1)
print('Bulletins nuls :',bulletin_nul)
sleep(1)
print('Suffrage valablement exprimé :',suffrageValablementExprime)
sleep(1)
print('Suffrage par candidat')
sleep(1)
print(liste['1'],' a obtenu ',sonomou,'voix, soit ',pourcentageSonomou,' %')
sleep(1)
print(liste['2'],' a obtenu ',josias,'voix, soit ', pourcentageJosias,' %')
t=input('')
sleep(2)
clear()
print('\t\t\tVoici les résultats provisoirs ')
if sonomou>josias:
    print('\t\tIl est admis au poste de Délegé Géneral M. :',liste['1'],' avec ',pourcentageSonomou,' %')
elif sonomou<josias:
    print('\t\tIl est admis au poste de Délegé Géneral M. :',liste['2'],' avec ',pourcentageJosias, '%')
else:
    print('\t\tLes deux candidats ont obtenus les mêmes voix, second tour')


