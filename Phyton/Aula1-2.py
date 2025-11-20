nota1 =int(input("Nota 1"))
nota2 =int(input("Nota 2"))
nota3 =int(input("Nota 3"))

media = (nota1+nota2+nota3)/3

if(media >= 8):
    print("passou de ano: ")
elif (media>=5 and media <8):
    print("Esta na media: ")
else : print ("recuperação: ")
