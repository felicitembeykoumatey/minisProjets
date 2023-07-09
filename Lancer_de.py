import random

print ("1 : Lancer le dé 0 : Quitter le programme")
while True:
      #On demande à l'utilisateur de saisir un nombre

    x=int(input("Clique sur le bouton"))
      #conditions if elseif, else
      #Si l'utilisateur saisi 0, fin!
    if x==0:
          print("Bye, à la prochaine !")
          break
    elif x==1:
        print(random.randint(1,6))
    else:
       print("Je n'ai pas compris")
