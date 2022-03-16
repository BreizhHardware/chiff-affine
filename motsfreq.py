""" Programme d'analyse des fréquences de mots dans un
    fichier de texte.
    Le programme affiche les mots par ordre décroissant
    de fréquence en indiquant pour chacun son nombre d'occurrences
    dans le fichier.

    Uilisation :
        python mots-freq.py nomFichier

    où nomFichier est le nom du fichier à analyser
"""


from __future__ import annotations
import sys


def getWords(text : str
             )   -> list[str]:
    """ Découpe text en mots et renvoie la liste des mots.
    """
    i = 0
    word = ''
    words = []
    while i < len(text):
        # words contient la liste des mots complets trouvés avant l'indice i de text.
        # word contient le mot en cours de lecture avant l'indice i de text.
        if text[i].isalpha():
            word = word + text[i]
        elif word != '':
            words.append(word)
            word = ''
        i = i + 1
    if word != '':
        words.append(word)
        word = ''
    return words


def updateDict(wordDict : dict[str, int],
               words    : list[str]
               )       -> None:
    """ wordDict est un dictionnaire tel que
            * une clé est un mot
            * la valeur associée est la fréquence de ce mot.
            
        Met à jour wordDict avec la liste de mots words.
    """
    for word in words:
        if word in wordDict:
            freq = wordDict[word] + 1
        else:
            freq = 1
        wordDict[word] = freq


def getWordsList(wordsFreq : dict[str, int]
                 )        -> list[tuple[str, list]]:
    """ Renvoie la liste de couples (mot, freq) de wordsFreq.
        Les couples sont triés par ordre décroissant de freq.
    """
    wordsList = [(word, wordsFreq[word]) for word in wordsFreq]
    
    # Tri la liste wordsList par ordre décroissant de freq.
    # Adaptation de l'algorithme du tri par insertion.
    k = 1
    while k < len(wordsList):
        i = k
        while i > 0 and wordsList[i - 1][1] < wordsList[i][1]:
            wordsList[i - 1], wordsList[i] = wordsList[i], wordsList[i - 1] 
            i = i - 1  
        k = k + 1
    return wordsList


def printWords(wordsList : list[tuple[str, list]]
               )        -> None:
    """ Écrit la liste de mots sur la sortie standard.
    """
    for word, freq in wordsList:
        print(word, ' : ', freq)
    print('Nombre de mots : ', len(wordsList))
        


# PROGRAMME PRINCIPAL

filename = sys.argv[1]

fd = open(filename, 'r')
wordsFreq = dict()
for line in fd:
    words = getWords(line)
    updateDict(wordsFreq, words)
fd.close()

wordsList = getWordsList(wordsFreq)
printWords(wordsList)