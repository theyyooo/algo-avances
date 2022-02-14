def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k

# Programme principal pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab) 
print ("Le tableau trié est: \n")
print (tab)

# invariant de boucle
# on souhaite prouver que le tableau A sera trié
# -> le tableau T de 1 à j-1 est trié
#
# initialisation j = 2  donc T =< A[1] > il y a un seul élément : il est trié
# conservation si T de taille j est trié alors après une itersion T de taille j + 1 est toujours trié (après insertion de A[j+1])
# terminaison lorsque j = taille(A), T est trié et contient tout A (permutation)