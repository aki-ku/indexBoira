import os
#Exercici2
def comptarParaules(text):
  #TODO Heu de retornar el nombre de paraules que té un text
  cont = 0
  for i in text:
    cont = cont + 1
  return cont

def comptarFrases(text):
  frase = 0
  for i in text:
    if i == " ":
      frase = frase + 1
  #TODO Heu de retornar el nombre de frases. 
  #Com es separen les frases?
  return frase+1

def mitjanaParaulesPerFrase(text):
  mitjana = (comptarParaules(text)/comptarFrases(text))
  
  #TODO Heu de retornar la mitjana de paraules per frases?
  return mitjana

#Exercici 3
def numeroParulesComplexes(text):
  #TODO Heu de retornar el nombre de paraules complexes que té el text
  cont = 0
  paraula = text.split()

  for i in paraula:
    if len(i)>5:
      cont = cont + 1
  #Són aquelles que tenen méés de cinc lletres
  return cont

def percetantgeParaulesComplexes(text):
#TODO Fer-ho al final de tot el 5.
#Exericic 5 llegir configuració/
  mitjana = numeroParulesComplexes(text)/comptarParaules(text)
  return mitjana

#Exercici 1
t = False
while t == False:
  nomFitxer = input("Entra el nom de l'arxiu que vols analitzar ")
#TODO heu de completar el codi perquè la variable text tingui el contingut del fitxer
  if (os.path.isfile('noticies/'+nomFitxer)):
    t = True
    fitxer = open('noticies/'+nomFitxer,'r')
    text = fitxer.read()
    print("És fitxer")
  else:
    print("No és fitxer")
    t = False
print(comptarParaules(text))
print(comptarFrases(text))
print(mitjanaParaulesPerFrase(text))
print(numeroParulesComplexes(text))
print(percetantgeParaulesComplexes(text))
print("Gràcies!")



#Per provar exercici 2 i 3 podeu posar-vos print aquíí per comprovar si es compta béé paraules, si compta frases, si es fa la mitja i si es detecten les complexes.

#Exercici 4
#càlcul de la fórmula
index = (0.4 * ((comptarParaules(text))/ comptarFrases(text))) + 100 * ((numeroParulesComplexes(text))/ comptarParaules(text))

#TODO  Pinteu index per pantalla 
print(index)

#TODO Classifiqueu exercici segons índex
# Digueu com és el text seguint la taula https://en.wikipedia.org/wiki/Gunning_fog_inde

#TODO
#Heu de tancar el fitxer


