import art
import random
print(art.logo)

def numero_11(deck):
    """Dependendo da soma das cartas, o número 11 passará a ser o número 1,
    deste modo, a função avalia os requisitos para fazer essa troca.
    :param deck: seleciona o deck"""
    for i in range(len(deck)):
        if deck[i] == 11 and sum(deck) > 21:
            deck[i] = 1

def vencedor():
    print(f"\nSua mão: {meudeck} -- Seu Score: {sum(meudeck)}          Carta Dealer: {oponentedeck} -- Score: {sum(oponentedeck)}\n")
    if sum(meudeck) == sum(oponentedeck):
        return print("Empate! 🙃")
    elif sum(meudeck) == 21:
        return print("Você fez um Blackjack 😎\nVocê venceu!")
    elif sum(oponentedeck) == 21:
        return print("O opodente fez um Blackjack 😭\nVocê perdeu!")
    elif sum(oponentedeck) > 21:
        return print("O oponente estourou, você venceu! 😅")
    elif sum(meudeck) > sum(oponentedeck):
        return print("Você venceu! 😁")
    else:
        return print("Você perdeu! 😤")

def dealer_draw():
    if sum(oponentedeck) < 17:
        oponentedeck.append(random.choice(cards))

def cartas_e_score(deck1, deck2):
    print(f"\nSua mão: {deck1} -- Seu Score: {sum(deck1)}          Carta Dealer: {deck2}\n")

jogo = True
while jogo:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    meudeck = random.choices(cards, k=2)
    oponentedeck = random.choices(cards, k=1)

    cartas_e_score(meudeck, oponentedeck[0])
    oponentedeck.append(random.choice(cards))
    partida = True
    while partida:
        numero_11(meudeck)
        if sum(meudeck) > 21:
            print("Você estouru, você perdeu! 😫")
            partida = False
        else:
            nova_carta = input("Deseja outra carta? Digite 's' ou 'n':  ").lower()
            if nova_carta == 's':
                meudeck.append(random.choice(cards))
                dealer_draw()
                numero_11(meudeck)
                numero_11(oponentedeck)
                cartas_e_score(meudeck, oponentedeck[0])
            else:
                dealer_draw()
                vencedor()
                partida = False

    continuar = input("\nDeseja jogar outra partida? Digite 's' ou 'n':  ").lower()
    if continuar == "s":
        print("\n" * 40)
        print(art.logo)
    else:
        jogo = False
