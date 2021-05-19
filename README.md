# Sandy logiciel  

## Général  
*Context :*    
Les déchets plastiques sont ceux les plus répandus dans l'environnement marin. Ils représentes aujourd'hui un risque environnemental et sanitaire croissant.   

*Objectifs du logiciel :*    
Face à ce constat, le projet *Sandy* associé à un spectromètre IR permet d'analyser les microplsatiques présents sur une plage afin de les identifier et de les quantifier.

*Principe de fonctionnement :*  
Afin d'identifier la nature des corps étudiés par le spectromètre, nous allons utiliser les propriétés spectrales des matériaux. A l'aide d'un spectromètre mobile, nous allons pouvoir accéder au pourcentage de réflectance qui correspond à la proportion de lumière réfléchie par la surface d'un matériau. Le spectre de réflexion représentant la réflectance en fonction de la longueur d'onde va ainsi nous permettre d'identifier les plastiques.
Pour cela, nous avons besoin de spectre de réflexion de référence afin de pouvoir effectuer les comparaisons. Les spectres que nous avons utilisés ont été obtenu dans un environnement industriel de haute précision. 

*Plastiques étudiés :*  
* Polyéthylène téréphtalate (PET) : bouteille en plastique  
* Polypropylène (PP) : corde bleue
* Polyester (PEST) : corde orange
* Polyéthylène basse densité (PE-LD) : gobelet en plastique

## Installation  
_fonctionne avec python3_

**1. Cloner le projet git**  
```bash
git clone ......
```

**2. Installations des paquets nécessaires**  
```bash
python3 install -r requirements.txt
```

**3. Placer vous dans un environnement virtuel**
```bash
virtualenv venv
source venv/bin/activate
```
## Utilisation
