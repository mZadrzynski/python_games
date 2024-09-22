import karty, gry

class W_Hand(karty.Hand):
    """reka w black jacku"""
    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name
        self.cards = karty.Hand()


class W_Fight_Hand(karty.Hand):
    """reka w black jacku"""
    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.cards = karty.Hand()


class Player(W_Hand):
    def lose(self):
        print(self.name, "przegrywa")
    
    def win(self):
        print(self.name, "wygrywa")
    
    def push(self):
        print(self.name, "remisuje")

    def name(self):
        print(self.name + " :")
    
    
#klasa rozgrywki
class W_Game_Start(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = Player(name)
            self.players.append(player)
        self.deck = karty.Deck()
        

    #rozdac wszystkie karty z tali do rak graczy
    def play(self):
        self.deck.populate()
        self.deck.suffle()
        
        print(self.deck)
        i_range = int(len(self.deck.cards) * 0.5)

        for i in range (0, i_range+1):
             self.deck.deal(self.players, per_hand= 1)
        #for player in self.players:
        #    print(player)
        #    print(player.cards[0].card_value())
    
    def round(self, names):
        #jedna runda gry
        if_winner = True
        self.round_reward = karty.Deck()
        self.draw_reward = karty.Deck()
        values_counter  = []

        #zabiera kazdego braczowi po jednej karcie
        for player in self.players:
            print("gracz o nazwie " +str(player.name)+ " posiada karte:") 
            print(player.cards[0])
            values_counter.append(player.cards[0].card_value())
            player.give(player.cards[0], self.round_reward)
            
        max_value = max(values_counter)
        
        #pokazuje co jest w puli do zdobycia
        #print("karty w puli to :")
        #print(self.round_reward)

        # Find all indices where the maximum value occurs
        id_winners = [i for i, value in enumerate(values_counter) if value == max_value]
        if len(id_winners) == 1:
            id_winner = id_winners[0]
            while self.round_reward.cards:
                    card = self.round_reward.cards[0]
                    self.round_reward.give(card, self.players[id_winner].cards)
            print("wygrywa :")
            print(self.players[id_winner].name)
        else:
            while len(id_winners) != 1:
                print("jest remis, dogrywka!")
                print(values_counter)
                print(id_winners)
                values_counter = []
                while self.round_reward.cards:
                    card = self.round_reward.cards[0]
                    self.round_reward.give(card, self.draw_reward)
                for player in self.players:
                    player.give(player.cards[0], self.draw_reward)
                    print("gracz o nazwie " +str(player.name)+ " posiada karte:") 
                    print(player.cards[0])
                    values_counter.append(player.cards[0].card_value())
                    player.give(player.cards[0], self.round_reward)
                print("karty przekazane do nowej puli")
                print(self.draw_reward)
                print(self.round_reward)
                max_value = max(values_counter)
                id_winners = [i for i, value in enumerate(values_counter) if value == max_value]
                #print(id_winners)
                #id_winner = id_winners[0]
                #print(id_winner)
            if  len(id_winners) == 1:
                id_winner = id_winners[0]
                print(id_winner)
                while self.round_reward.cards:
                    card = self.round_reward.cards[0]
                    self.round_reward.give(card, self.players[id_winner].cards)
                while self.draw_reward.cards:
                    card = self.draw_reward.cards[0]
                    self.draw_reward.give(card, self.players[id_winner].cards)
                for player in self.players:
                    player.cards.suffle()
                print("wygrywa :")
                print(self.players[id_winner].name)

        for player in self.players:
            #print("gracz o nazwie " +str(player.name)+ " posiada karty:") 
            #print((player))
            print("gracz o nazwie " +str(player.name)+ " posiada kart w puli:")
            print(len(player))

        print("\n karty do zdobycia w puli: ")
        print(self.round_reward)
        input("aby rozegrac nastepna ture nacisnij enter\n")

        if len(self.players[0].cards) == 0:
            print("wygrywa")
            print(self.players[1].name)
            if_winner = False
        if len(self.players[1].cards) ==0:
            print("wygrywa")
            print(self.players[0].name)
            if_winner = False
        return if_winner
    
    #def player_shuffle(self, names):
    #    for player in self.players:
    #        self.players[player].cards.shuffle()


def main():        

    print("\n witaj w grze wojna")

    names = []
    number =  2 #gry.ask_number("podaj liczbe graczy (1-4)", low = 1, high = 4)
    for i in range(number):
        name = input("wprowadz nazwe gracza: ")
        names.append(name)  

    game = W_Game_Start(names)
    game.play()
    round_count = 0
    while game.round(names):
        game.round(names)
        round_count += 1
        print("zaczynamy runde: " + str(round_count))
    print("gra dobiegla koncza")

        #if round_count == 10:
        #    round_count == 0
        #game.player_shuffle()
        
    
    
    #again = None
    #while again != "n":
    #    game.play()
    #    again = gry.ask_yes_no("\n czy chcesz grac ponowniestss")
        
main()