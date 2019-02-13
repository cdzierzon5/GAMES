import games, cards
deck = cards.Deck()
deck.populate()
deck.shuffle()

print("Welcome to the game")

again = None
while again != "n":
    players = []
    num = games.ask_number(question = "How many player? (2-10): ",low = 2, high = 11)
    for i in range(num):
        name = input("Player name: ")
        player = games.Player(name)
        player.append(player)
    hands=[]
    for player in players:
        hand = player.hand
        hands.append(hand)
    deck.deal(hands,1)
    print("\nhere are the results: ")
    for player in players:
        print(player)

    again = games.ask_yes_no("\ndo you want to play again? (y/n): ")

input("\n\nPress the enter key to exit")
