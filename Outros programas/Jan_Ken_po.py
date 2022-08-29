#Jogo de pedra, papel ou tesoura
from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def Opcao_jogador():
    esc_jogador = input ("Escolha pedra, papel ou tesoura: ")
    esc_jogador.lower()
    if esc_jogador in {"pedra", "papel", "tesoura"} :
        return esc_jogador
    else:
        print("opcao invalida. Tente novamente")
        esc_jogador = Opcao_jogador()
        return esc_jogador
      
def Opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina

while True:
    esc_maquina = Opcao_maquina()
    esc_jogador = Opcao_jogador()
    if (esc_jogador == esc_maquina):
        print (f"Jogador escolheu {esc_jogador} e a Maquina escolheu "
            f"{esc_maquina} - Resultado : Empate")
    elif (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            print(f"Jogador escolheu {esc_jogador} e a Maquina escolheu "
            f"{esc_maquina} - Resultado : Voce Ganhou")
            jogador_vitorias += 1
    elif (esc_jogador == "pedra") and (esc_maquina == "papel") \
        or (esc_jogador == "papel") and (esc_maquina == "tesoura") \
            or (esc_jogador == "tesoura") and (esc_maquina == "pedra"):
            print(f"Jogador escolheu {esc_jogador} e a Maquina escolheu "
            f"{esc_maquina} - Resultado : A maquina Ganhou")
            maq_vitorias += 1    
    print("-"*30)
    print(f"Vitorias do Jogador: {jogador_vitorias}")
    print(f"Vitorias da Maquina: {maq_vitorias}")
    print("-"*30)

    esc_jogador = input("Voce quer jogar de novo? ")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["Nao", "NAO", "nao", "n", "N"]:
        break
    else:
        break
