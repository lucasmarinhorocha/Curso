import random

secreto = random.randint(1,100)
tentativas = 3

print("====NUMERO_SECRETO====")


while tentativas > 0:

    numero = int(input("informe um numero"))
    if numero != secreto:
        tentativas -=1
        print(f"TENTE NOVAMENTE, voce tem: {tentativas} tentativas")
        
        if secreto > numero:
            print(f"\no numero é maior")
       
        else :
            print("\no numero que quer é menor")
     
    elif numero == secreto and tentativas > 0 :
            print(f"PARABENS, VOCE ACERTOU EM:{tentativas} tentativas o numero {numero} ")
            tentativas = -1
            

if tentativas == 0:
   print(f"suas chances acabaram o numero secreto era: {secreto}")