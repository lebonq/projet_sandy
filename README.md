[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/lebonq/projet_sandy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/lebonq/projet_sandy/context:python)

# Sandy logiciel  

## Général

**1. Contexte :**

Les déchets plastiques sont ceux les plus répandus dans l'environnement marin. Ils représentent aujourd'hui un risque environnemental et sanitaire croissant. Sous l'effet des éléments et l'impact du temps, les macro-plastiques se fragmentent en morceaux de plus en plus petits et incontrôlables. Ces microplastiques contaminent les écosystèmes ainsi que l'ensemble de la chaîne alimentaire alors que leurs effets sur la santé sont encore mal connus.   

**2. Objectifs du logiciel :**

Face à ce constat, le projet *Sandy* associé à un spectromètre Raman permet d'analyser les microplastiques présents sur une plage afin de les identifier et de les quantifier. Ce logiciel a pour mission de soutenir la recherche scientifique afin de permettre une meilleure compréhension de la pollution par les microplastiques, notamment ses impacts environnementaux et sanitaires. Les informations collectées aideront par la suite les décideurs et acteurs concernés dans la mise en place de mesures efficaces pour lutter contre l’invasion de nos écosystèmes par le plastique.


**3. Principe de fonctionnement :**  

Afin d'identifier la nature des corps étudiés par le spectromètre, nous allons utiliser les propriétés spectrales des matériaux. A l'aide d'un spectromètre mobile, nous allons pouvoir accéder à l'intensité en fonction du nombre d'onde. Ces données sint caractéristiques de la composition d'un matériau puisqu'elles dépendent du type d'atome, de la force des liaisons, de sa géométrie, etc.  
Pour cela, nous avons besoin de spectre de référence afin de pouvoir effectuer les comparaisons. Les spectres que nous avons utilisés ont été obtenu dans un environnement de laboratoire de haute précision. 

**4. Plastiques étudiés :**

* Polyéthylène téréphtalate (PET) 
* Polypropylène (PP) 
* Polycarbonate (PC)
* Polyéthylène basse densité (PE-LD) 
* Polyéthylène haute densité (PE-HD)
* Acide polyactique (PLA)

Caractéristiques spectrales - *exemple du PELD en présence de sable*

<img src="https://github.com/lebonq/projet_sandy/blob/main/analysePELD.PNG"/>  


## Installation

_fonctionne avec python3_   

**1. Cloner le projet git**

```bash
git clone https://github.com/lebonq/projet_sandy
```

**2. Installations des paquets nécessaires**

```bash
python3 install -r requirements.txt
```

## Utilisation
```bash
cd logiciel_pc
python3 interface.py
```
