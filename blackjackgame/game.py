#! /usr/bin/env python3
# Matthew Jun
# Matt.j@csu.fullerton.edu
# @mwjun

"""Game of blackjack"""

# import some stuff

from blackjackgame.player import *
from blackjackgame.cards import  *
from random import choice
import sys
import json


def load_ai_data():
    try:
        with open('ai_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"hands": {}}

def save_ai_data(ai_data):
    with open('ai_data.json', 'w') as file:
        json.dump(ai_data, file, indent=4)

def ai_decision(hand, ai_data):
    hand_key = " ".join(sorted([str(card) for card in hand]))  # Ensure the hand is properly represented
    stats = ai_data["hands"].get(hand_key, {"win": 0, "lose": 0})
    if stats["win"] / (stats["win"] + stats["lose"] + 1) > 0.5:
        return "stand"
    else:
        return "hit"
    

class BlackJackGame:
    """the blackjack gm"""
    def __init__(self):
        self._is_game_over = False
        # self._players = [Player('Matt',10000)
        # self._robots = [Dealer("dealer")]
        self._all_participants = []
        self._deck = Deck()
        
        self._betcount = []
        self.namephase = True
        self.bettingphase = True
        self.playingphase = True
        self.decisionphase = True
        self.dealingphase = True
        self.scorecompare = True
        self. playagain = False

    def play(self):
        while not self._is_game_over:
                if self.playagain == False:
            # for player in self._all_participants:
                    print('hello, welcome to blackjack')
                    num_players = int(input("how many players are playing?: "))
                    if self.namephase == True:
                        for i in range(num_players):
                            names = input("names of player?:  ")
                            self._all_participants.append(Player(names))
                        self._all_participants.append(Dealer("Dealer"))
                        print(self._all_participants)
                        print("\n")
                        self.namephase = False
                    

                if self.bettingphase == True:
                    #for player in range(len(self._all_participants)):
                    for player in self._all_participants:
                        if player.is_dealer() == False:
                            print(player)
                            bet = int(input( "how much do you want to wager?: "))
                            if player.get_bal() < bet:
                                player.dont_have_enough_msg()
                            else:
                                player.track_bet(bet)
                                player.withdraw(bet)
                                player.deduction_message(bet)
                                player.remaining_bal()
                        else:
                            print(self._all_participants)
                            self.bettingphase = False
                self._playercards = []
                if self.dealingphase == True:
                    self._deck.shuffle(3)
                    self._deck.cut()
                    for _ in range(2):
                        for player in self._all_participants: 
                        # self._deck.__next__()
                            card = self._deck.__getitem__(i)
                            i+=1
                            print(card.__str__)
                            amount = card.rank
                            print(type(amount))
                            if amount in ['Jack', 'Queen', 'King']:
                                amount = 10
                                valueOfcard = int(amount)
                                print(valueOfcard)
                                self._deck.__next__()
                                self._playercards.append(valueOfcard)
                            elif card.rank == 'Ace':
                                self._deck.__next__()
                                amount = 1
                                valueOfcard = int(amount)
                                print(valueOfcard)
                                self._playercards.append(valueOfcard)
                            else:
                                valueOfcard = int(amount)
                                print(valueOfcard)
                                self._deck.__next__()
                                self._playercards.append(valueOfcard)
                        print("end of gamephase")
                        
                        self.dealingphase = False
                        # for player in self._all_participants:
                    print(self._playercards)
                    pairs = list(zip(self._playercards[:len(self._playercards)//2], self._playercards[len(self._playercards)//2:]))
                    print(pairs)
                    pairtotal = [sum(pair) for pair in pairs]
                    print(pairtotal)
                    print("\n")
                    j = 0
                self.decisionphase = True
                if self.decisionphase == True:
                    for player in self._all_participants:
                    
                        playerbust = False
                        playerstay = False
                        
                        if player.is_dealer() == False:
                            if j < num_players:
                                print("Your turn: \n")
                                print(player.name)
                                print(pairtotal)
                                if player.is_dealer() == False:
                                        while not playerstay or not playerbust:
                                            print("player:\n")
                                            print(player.name)
                                            print(f'Your total is:\n')
                                            print(pairtotal[j])
                                            print(pairtotal)
                                            if pairtotal[j] != 21:
                                                action = input('''What do you want to do?:\n 
                                                "h" for hit\n  
                                                "s" for stay\n
                                                "d" for double down: ''')
                                                
                                                if action == 'D'.lower():
                                                    if player.get_bal() < bet:
                                                        player.dont_have_enough_msg()
                                                        continue
                                                    else:
                                                        player.withdraw(player.double_down())
                                                        player.remaining_bal()
                                                    card = self._deck.__getitem__(i)
                                                    i+=1
                                                    print(card.__str__)
                                                    amount = card.rank
                                                    print(type(amount))
                                                    if amount in ['Jack', 'Queen', 'King']:
                                                        amount = 10
                                                        valueOfcard = int(amount)
                                                        pairtotal[j] += valueOfcard
                                                        print(pairtotal[j])
                                                        print(pairtotal)
                                                        playerstay = True
                                                        if pairtotal[j] > 21:
                                                            player.busted()
                                                            print("\n")
                                                            j+=1
                                                            playerbust = True
                                                            break
                                                        else:
                                                            playerstay = True
                                                            break
                                                    elif card.rank == 'Ace':
                                                        self._deck.__next__()
                                                        amount = 1
                                                        valueOfcard = int(amount)
                                                        pairtotal[j] += valueOfcard
                                                        print(pairtotal)
                                                        playerstay = True
                                                        if pairtotal[j] > 21:
                                                            player.busted()
                                                            print("\n")
                                                            j+=1
                                                            playerbust = True
                                                            break
                                                        else:
                                                            playerstay = True
                                                            break
                                                    else:
                                                        valueOfcard = int(amount)
                                                        print(valueOfcard)
                                                        self._deck.__next__()
                                                        pairtotal[j] += valueOfcard
                                                        print(pairtotal[j])
                                                        print(pairtotal)
                                                        playerstay = True
                                                        if pairtotal[j] > 21:
                                                            player.busted()
                                                            print("\n")
                                                            j+=1
                                                            playerbust = True
                                                            break
                                                        else:
                                                            playerstay = True
                                                            break
                    
                                                if action == 'S'.lower():
                                                    print(player.name)
                                                    player.player_stay()
                                                    playerstay = True
                                                    print('your total is:')
                                                    pairtotal[j]
                                                    print(pairtotal)
                                                    j+=1
                                                    break
                                                if action == 'H'.lower():  
                                                    card = self._deck.__getitem__(i)
                                                    i+=1
                                                    print(card.__str__)
                                                    amount = card.rank
                                                    print(type(amount))
                                                    if amount in ['Jack', 'Queen', 'King']:
                                                        amount = 10
                                                        valueOfcard = int(amount)
                                                        pairtotal[j] += valueOfcard
                                                        print(pairtotal[j])
                                                        print(pairtotal)
                                                        if pairtotal[j] > 21:
                                                            player.busted()
                                                            print("\n")
                                                            j+=1
                                                            playerbust = True
                                                            break
                                                    elif card.rank == 'Ace':
                                                        self._deck.__next__()
                                                        if pairtotal[j] > 10:
                                                            amount = 1
                                                            valueOfcard = int(amount)
                                                            pairtotal[j] += valueOfcard
                                                            print(pairtotal)
                                                        else:
                                                            valueOfcard = 11
                                                            pairtotal[j] += valueOfcard
                                                        if pairtotal[j] > 21:
                                                            player.busted()
                                                            print("\n")
                                                            j+=1
                                                            playerbust = True
                                                            break
                                                    else:
                                                        valueOfcard = int(amount)
                                                        print(valueOfcard)
                                                        self._deck.__next__()
                                                        pairtotal[j] += valueOfcard
                                                        print(pairtotal[j])
                                                        print(pairtotal)
                                                        if pairtotal[j] > 21:
                                                            player.busted()
                                                            print("\n")
                                                            j+=1
                                                            playerbust = True
                                                            break                                        
                                            else:
                                                playerstay = True
                                
                    
                    else:
                        print("Dealer's turn")
                        print("Dealer has:\n")
                        print(pairtotal[j])
                        if pairtotal == 21:
                            playerstay = True
                        if pairtotal[j] < 16:
                            card = self._deck.__getitem__(i)
                            i+=1
                            print(card.__str__)
                            amount = card.rank
                            print(type(amount))
                            print(pairtotal[j])
                            if amount in ['Jack', 'Queen', 'King']:
                                amount = 10
                                valueOfcard = int(amount)
                                pairtotal[j] += valueOfcard
                                print("dealer's total:\n")
                                print(pairtotal[j])
                                if pairtotal[j] >= 16:
                                    player.player_stay()
                                    playerstay = True
                                if pairtotal[j] > 21:
                                    player.busted()
                                    print("\n")
                                    playerbust = True
                            elif card.rank == 'Ace':
                                self._deck.__next__()
                                if pairtotal[j] > 10:
                                    amount = 1
                                    valueOfcard = int(amount)
                                    pairtotal[j] += valueOfcard
                                    print("dealer's total:\n")
                                    print(pairtotal[j])
                                else:
                                    
                                    valueOfcard = 11
                                    pairtotal[j] += valueOfcard
                                if pairtotal[j] >= 16:
                                    player.player_stay()
                                    playerstay = True
                                if pairtotal[j] > 21:
                                    player.busted()
                                    print("\n")
                                    playerbust = True
                            else:
                                valueOfcard = int(amount)
                                print(valueOfcard)
                                self._deck.__next__()
                                pairtotal[j] += valueOfcard
                                print("dealer's total:\n")
                                print(pairtotal[j])
                                if pairtotal[j] >= 16:
                                    player.player_stay()
                                    playerstay = True
                                if pairtotal[j] > 21:
                                    player.busted()
                                    print("\n")
                                    playerbust = True
                        
                    self.decisionphase = False

                i = 0

                if self.scorecompare == True:
                    for player in self._all_participants:
                        if player.is_dealer():
                            if pairtotal[i] > pairtotal[-1]:
                                print(player.get_bet())
                                bet = player.get_bet()
                                player.deposit(bet)
                                print(player)
                                i+=1
                                player.remaining_bal()
                            if pairtotal[i] == pairtotal[-1]:
                                print(player.name)
                                print("Push, you get your wager back, but don't win anyting")
                                bet = player.get_bet()
                                player.deposit(bet)
                                print(player)
                                player.remaining_bal()
                                i+=1
                            else:
                                print("nothing to update for this player.")
                                player.remaining_bal()
                                i+=1
                    print(self._all_participants)
                    player.remaining_bal()
                    self.scorecompare = False
                    self.decisionphase = True

                    if self.decisionphase == True:
                        choice = input("""What do yo want to do?:\n
                                                                'n' for new game:  \n
                                                                'q' to quit: """)
                        if choice == 'Q'.lower():
                            self.decisionphase = False
                            break
                        if choice == "N".lower():
                            self.decisionphase = False
                            self.namephase = True
                            self.bettingphase = True
                            self.playingphase = True
                            self.dealingphase = True
                            self.scorecompare = True
                            self.playagain = True
                            
        self.is_game_over = True
        
                    #         Card.card_value()


                
      
                        
                        
                    
                
                

          

            
        

game = BlackJackGame()
game.play()


