#!/usr/bin/env python
# coding: utf-8

# Nom         : Friedrich
# Prenom      : Paul
# N. Etudiant : 

# # Exercice 1: sérialisation de liste
# 
# On souhaite enregistrer une liste de mots dans un fichier afin de pouvoir la réutiliser plus tard.
# 
# ## Écriture
# 
# Réaliser une fonction `write_list_to_file(wordlst, filename)` prenant comme paramètres une liste de mots `wordlst` et un nom de fichier `filename`,. La fonction devra stocker les mots de la liste dans un fichier (encodage UTF8), un mot par ligne.

# In[1]:



 # votre code ici

def write_list_to_file(wordlist, filename):
 file = open(filename, "w+")
 file.write(str(wordlist))
 file.close()
 return
 
write_list_to_file(["Jeder", "Mensch", "hat", "angeborne", "schon", "durch", "die", "Vernunft", "einleuchtende", "Rechte", "und", "ist", "daher", "als", "eine", "Person", "zu", "betrachten", "Sclaverey", "oder", "Leibeigenschaft", "und", "die", "Ausübung", "einer", "darauf", "sich", "beziehenden", "Macht", "wird", "in", "diesen", "Ländern", "nicht", "gestattet"], "mon_test.txt")


# ## Lecture
# 
# Réaliser une fonction `read_list_from_file(filename)` permettant de récupérer la liste des mots originale à partir du fichier nommé `filename`.

# In[2]:





    # votre code ici

def read_list_from_file(filename):
    file = open(filename, "r")
    t =str(file.read())
    file.close()
    return t


# In[3]:


## Vos tests ici

t = read_list_from_file("mon_test.txt")
print(t)


# # Exercice 2: conjugueur
# 
# Soit la liste `ps` des pronoms personnels sujets, et la liste `ip1` des terminaisons des verbes du 1er groupe à l'indicatif présent.

# In[4]:


ps = 'je tu il nous vous ils'.split()
ip1 = 'e es e ons ez ent'.split()


# ## Conjugue
# 
# Définir `conjugue(v, n)` qui prend une chaîne telle que `v` et un nombre `n` entre 1 et 6 (la personne), et qui génère la forme conjuguée correspondante; par exemple:
# 
# ```pycon
# >>> conjugue('tirer', 4)
# 'nous tirons'
# ```

# In[5]:



    # votre code ici
def conjugue(v, n):
    print (ps[n-1] + " " + v[:-2] + ip1[n-1])    


# In[6]:


## Tests de la fonction

conjugue("parler", 6)


# ## Conjugaison
# 
# A partir de l'exercice précédent, coder la conjugaison de `v`, générant la liste des 6 formes (par exemple: `['je tire', 'tu tires', 'il tire', …]`).

# In[7]:


#votre code ici
def conjugaison(v):
    for i in range(1,7):
        conjugue(v,i)
    return


# In[8]:


## Tests de la fonction

conjugaison("tester")


# # Exercice 3: pluriel de mots
# 
# Coder une fonction `pluriel(mot)` pour former correctement le pluriel d'à peu près n'importe quel nom ou adjectif, majuscule ou minuscule.
# 
# Si vous ne vous souvenez pas vraiment des règles, vous pouvez consulter la page de votre choix sur internet, par exemple [celle ci](https://leconjugueur.lefigaro.fr/fr_pluriel_nom.php).

# In[9]:



    # votre code ici
def pluriel(mot):
    if mot[-3:] == "ail":
        print (mot[0:-3] + "ails")
    elif mot[-2:] == "al":
        print (mot[0:-2] + "aux")
    elif mot[-2:] == "au" or mot[-2:] == "eu":
        print (mot + "x")
    elif mot[-2:] == "ou":
        print (mot + "s")
    elif mot[-1:] == "z" or mot[-1:] == "s" or mot[-1:] == "x":
        print (mot)
    else:
        print("...c'est difficile...")
        
        
pluriel("oeil")


# In[10]:


## Tests de la fonction

tests = [
    'corail', 'ail', 'détail',              # mots en ail
    'canal', 'animal', 'bal', 'chacal',     # mots en al
    'drapeau', 'tuyau', 'landau',           # mots en au
    'cheveu', 'pneu', 'bleu',               # mots en eu
    'sou', 'clou', 'pou', 'bijou',          # mots en ou
    'nez', 'gaz',                           # mots en z
    'bois', 'radis',                        # mots en s
    'roux', 'faux', 'prix',                 # mots en x
    'oeil', 'monsieur'                      # cas particuliers
]


# ## Script autonome
# 
# Réaliser un script `pluriel.py`, capable de prendre plusieurs mots et d'afficher leur pluriel.
# 
# Exemple:
# 
# ```
# $ plusieurs.py clou bleu rouillé
# clous
# bleus
# rouillés
# ```
