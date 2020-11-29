# coding=utf-8
file = open("nombre.txt", "a+")
from random import randint
a = 1
i = 0
nombre  = int(input("Quel nombre vouslez vous trouver : "))
while a != nombre:
    a = randint(0, 9999)
    i += 1
    if a == nombre:
        print("=====================")
        print("========={}=========" .format(a))
        print("=====================")
        print("    ")
        print("Trouver ! Après {} tirages" .format(i))
        print("-----------------------------")
        chance = 100/i
        print("Il y a donc moins de {} chance sur 100 d'avoir un {}".format(chance, nombre))
    else:
        print("====================================================================================================================")
        print("Tour numéro ", i)
        print("====================================================================================================================")
        print(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a,a, a, a, a, a, a, a, a, a, a, a, a, a, a, a)

a = str(a)
i = str(i)
file.write(a + " avec " + i + " tirages \n")
file.close()
