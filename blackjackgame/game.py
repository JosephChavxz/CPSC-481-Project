#! /usr/bin/env python3
# Matthew Jun
# Matt.j@csu.fullerton.edu
# @mwjun

"""Game of blackjack"""

from blackjackgame.player import *
from blackjackgame.cards import *
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

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.setup_game()

    def setup_game(self):
        print('Welcome to Blackjack!')
        num_players = int(input("How many human players are playing?: "))
        num_ai = int(input("How many AI players?: "))
        for i in range(num_players):
            name = input(f"Name of player {i + 1}: ")
            self.players.append(Player(name))
        for j in range(num_ai):
            ai_name = f"AI_Player_{j + 1}"
            self.players.append(AiPlayer(ai_name, is_ai=True))
        self.players.append(Dealer("Dealer", is_dealer=True))
        self.deck.shuffle()
        self.initial_deal()

    def initial_deal(self):
        for _ in range(2):  # Deal two cards to each player
            for player in self.players:
                player.add_card(self.deck.draw_card())
        self.show_hands()
        self.player_options()

    def show_hands(self):
        for player in self.players:
            print(f"{player.name} has {player.display_hand()} with a total of {player.hand_value()}")

    def player_options(self):
        for player in self.players:
            if player.is_dealer:
                print("finally")
                if player.hand_value() < 17:
                    player.add_card(self.deck.draw_card())
                    print(f"{player.name}'s final hand: {player.display_hand()} with a total of {player.hand_value()}")
            elif player.is_ai:
                print('oops')
                self.ai_plays(player)
            else:
                self.human_plays(player)

    def human_plays(self, player):
        while not player.is_busted and not player.is_staying:
            print(f"{player.name}'s turn. Your cards: {player.display_hand()}")
            choice = input("Would you like to 'hit' or 'stand'? ").lower()
            if choice == 'hit':
                player.add_card(self.deck.draw_card())
                print(f"{player.name} now has {player.display_hand()}")
                if player.is_busted:
                    print(f"{player.name} has busted!")
                    break
            elif choice == 'stand':
                player.stay()
                break


    def ai_plays(self, player):
        while player.hand_value() < 17:
            player.add_card(self.deck.draw_card())
        if player.hand_value() > 21:
            player.bust()
            print(f"{player.name} has busted!")
        else:
            player.stay()
        print(f"{player.name}'s final hand: {player.display_hand()} with a total of {player.hand_value()}")

    def check_winners(self):
        for player in self.players:
            if player.is_busted:
                print(f"{player.name} loses by bust.")
            else:
                self.compare_scores(player)

    def compare_scores(self, player):
        dealer = next(p for p in self.players if p.is_dealer)
        dealer_score = dealer.hand_value()
        player_score = player.hand_value()
        if player_score > dealer_score or dealer_score > 21:
            print(f"{player.name} wins!")
        elif player_score < dealer_score:
            print(f"{player.name} loses.")
        else:
            print(f"{player.name} ties with the dealer.")

    def play(self):
        self.player_options()
        self.check_winners()



