nbr = int(input())
syracuse = []
if(nbr==1):
   print("La suite de syracuse de premier terme "+ str(nbr)+" est [4,2,1]. Elle s'est faite en 3 etapes et de hauteur(max) : 4")
else:
    while (nbr != 1):
        if(nbr % 2 == 0):
            nbr = int(nbr/2)
        else:
            nbr = 3*nbr + 1
        syracuse.append(nbr)
    print("La suite de syracuse de premier terme "+ str(nbr)+" est :"+str(syracuse) +" Elle s'est faite en: "+ str(len(syracuse))+ " etapes et de hauteur(max) :"+ str(max(syracuse)))