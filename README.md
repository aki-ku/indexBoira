# Activitat 2 - Índex boira

## Enunciat

Al final dels 80 hi havia un còmic que apareixia per televisió, veieu un acudit d'ell:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/NizRszTrPDo/0.jpg)](https://www.youtube.com/watch?v=NizRszTrPDo)

Heu entès alguna cosa? Doncs aiò la seva gràcia era que no s'entenia res.

Doncs això passa amb molts textos, us passa alguna situació com aquesta:

- Hi ha textos que s'us fan fàcil de llegir? 
- D'altres més farragosos? 
- Hi ha persones que quan us parlen són més clares que altres? 

**Per què?**

Això es va preguntar en [Robert Gunning](https://en.wikipedia.org/wiki/Gunning_fog_index) l'any 1952 i es va "enpescar" una fórmula per classificar els textos. La fórmula és:

$$IndexBoira = 0.4 \times (MitjanaParaulesPerFrase+PercentatgeParaulesComplexes)$$ 

On:

$$mitjanaParaulesPerFrase = \frac{TotalParaulesText}{TotalFrases}$$

$$percentatgeDeParaulesComplexes = \frac{totalParaulesLlargues}{totalParaulesText} \times 100$$

A aquest índex el va anomenar índex de boira que té el text. **I quan més menor és  l'índex més fàcil de llegir és i més gran més complexe.**

Us atreviu a realitzar un programa que us calculi l'índex de boira d'un text?
Fem-ho pas a pas.

Hi ha una web que us fa aquest càlcul podreu comparar resultats tot i que nosaltres ho farem més senzilla. La web és [http://gunning-fog-index.com](http://gunning-fog-index.com)

## Exercici 1 Llegir el fitxer 


A l'inici del programa:

- demani el nom del fitxer, sempre estan dins la carpeta notícies.
- retorni en una cadena (String) tot el contingut del fitxer

Heu de tenir en compte possibles errors:

- arxius que no siguin de text. (Mirar que l'extensió sigui txt).
- que el nom que indica l'usuari sigui correcte. Que existeixi un arxiu amb aquest nom.


Fins que usuari no compleixi aquestes condicions es va demanant el nom de l'arxiu.
Com comprovar que un arxiu existeix mireu exemple:
```python3=
if (os.path.isfile(nom)):
    print("És fitxer")
else:
    print("No és fitxer")
```
Més informació a [https://docs.python.org/3/library/os.path.html#os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile)

Quan acabeu feu commit al repositori amb missatge "Exercici1 acabat"

## Exercici 2 Saber quantes paraules hi ha per frase

És té en compte que una frase és text que el **separa un punt** . 

Opcional:
- Delimitar frases també pels caràcters ;  o : . 
- Tractar els punts suspensius: canviar-los per un sol punt. 

Heu de realitzar diverses funcions:

- una que donat un text retorni el nombre de frases que hi ha. 
- una altra funció que compti quantes paraules hi ha en un text. 
- una altra funció que faci la mitja de paraules per frases. 

Quan acabeu feu commit al repositori amb missatge "Exercici2 acabat"

## Exercici 3 Conèixer les paraules complexes 

En la fórmula original és té en compte que una paraula és llarga si té més de 3 síl·labes excloent noms propis. En el nostre cas ho farem més senzill, una paraula serà llarga si té 5 lletres (això però s'hauria de poder modificar fàcilment) .

Heu de fer una funció que passat un text i un número que indiqui el nombre de lletres, retorni el nombre de paraules llargues que conté.

Quan acabeu feu commit al repositori amb missatge "Exercici3 acabat"

## Exercici 4 Donar la valoració del text 

Heu de fer una funció que faci el càlcul de l'index de boira, segons la fórmula explicada a la introducció i usant les funcions abans fetes. 

A part d'escriure el resultat doneu la classificació del text segons la taula que surt a la pàgina de la Wikipedia. 
Trobeu la taula a [https://en.wikipedia.org/wiki/Gunning_fog_index] (https://en.wikipedia.org/wiki/Gunning_fog_index)


Quan acabeu feu commit al repositori amb missatge "Exercici4 acabat"

## Exerecici 5 Configurar el programa des d'un arxiu 

Heu de permetre que els paràmetres (llindar lletres pel que es considera paraula llarga o els caràcters que delimiten les frases) siguin llegits d'un fitxer de configuració.

Configurar des de CSV (1 punt): 

L'arxiu anomenat configura.csv i el seu contingut seria:

5,.,;,:

On el primer caràcter és el nombre de lletres i la resta de caràcters són els caràcters que delimiten les frases. Els caràcters que delimiten pot ser un nombre variable. En aquest el CSV està orientat al caràcter ,  (coma).

Com modifiqueu el vostre programa? Què heu de fer?
