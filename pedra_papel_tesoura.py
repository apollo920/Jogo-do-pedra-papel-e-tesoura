# Joguinho do pedra papel e tesoura
import random
import time
escolhas_user=input("Digite a sua escolha: ").lower()
jogada_comp=random.choice(['pedra','papel','pesoura'])
def joguinho(jog_user,jog_comp):
    while True:
        print("Pedra, papeel, tesoouuuraaa!!!")
        time.sleep(1)
        if jog_comp == jog_user:
            print("Jogadas iguais, escolha novamente!")
            jog_user=input("Digite a sua escolha: ").lower()
        elif(jog_user == "papel" and jog_comp == "pedra"):
            print("Parabéns você venceu !!!!")
            break
        elif(jog_user == "pedra" and jogada_comp == "tesoura"):
            print("Parabéns você venceu !!!!")
            break
        elif(jog_user == "tesoura" and jog_comp == "papel"):
            print("Parabéns você venceu !!!!")
            break
        else:
            print("Sinto muito, você perdeu!!!")
            jog_comp=random.choice(['pedra','papel','pesoura'])
            jog_user=input("Digite a sua escolha: ").lower()
joguinho(escolhas_user,jogada_comp)
