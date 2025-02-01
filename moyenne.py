def calculer_moyenne(note,coefficients):
    total= sum(note*coefficients)
    total_coef=sum(coefficients)
    return total / total_coef

def rattrapage(note,coefficients):
    moyenne= calculer_moyenne(note,coefficients)
    if moyenne< 10 :
       return ("vous devez aller au rattrapage")
    else:
        return ("vous avez validé")

note= [13,8,4,5]
coefficients= [2,3,1,4]
resultat= calculer_moyenne(note,coefficients)
print(resultat)
