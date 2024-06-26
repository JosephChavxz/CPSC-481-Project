#! /usr/bin/env python3
# Matthew Jun
# Matt.j@csu.fullerton.edu
# @mwjun

# Leoanrdo Medrano
# lm1014367@csu.fullerton.edu
# @FenTheDeer

# Joseph Chavez
# jchavez0026@csu.fullerton.edu
# @JosephChavxz

"""Game of blackjack"""

from blackjackgame.player import *
from blackjackgame.cards import *
import json

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.setup_game()
        self.all_players_history = []
        self.ai_players_history = []

    def setup_game(self):
        """Helps set up game by asking how many human and AI players are playing."""
        print('Welcome to Blackjack!')
        num_players = int(input("How many human players are playing?: "))
        num_ai = int(input("How many AI players?: "))
        for i in range(num_players):
            name = input(f"Name of player {i + 1}: ")
            self.players.append(Player(name))
        for j in range(num_ai):
            ai_name = f"AI_Player_{j + 1}"
            self.players.append(AiPlayer(ai_name, is_ai=True))
        print("\n")
        self.players.append(Dealer("Dealer", is_dealer=True))
        self.deck.shuffle()
        self.initial_deal()

    def initial_deal(self):
        """Deals the initial two cards to each player."""
        for _ in range(2):  # Deal two cards to each player
            for player in self.players:
                player.add_card(self.deck.draw_card())
        self.show_hands()
        self.player_options()

    def show_hands(self):
        """Function that shows the hands and total hand value of every player."""
        for player in self.players:
            print(f"{player.name} has {player.display_hand()} with a total of {player.hand_value()}")

    def player_options(self):
        """Function that allows players/ai/dealer to hit or stay."""
        for player in self.players:
            print("\n")
            # Dealer's turn
            if player.is_dealer:
                if player.hand_value() < 17:
                    player.add_card(self.deck.draw_card())
                    print(f"{player.name}'s new hand: {player.display_hand()} with a total of {player.hand_value()}")
                else:
                    player.stay()
                    print(f"{player.name} stays with a total of {player.hand_value()}")
            # AI's turn
            elif player.is_ai:
                self.ai_plays(player)
            # Human player's turn
            else:
                self.human_plays(player)

    def human_plays(self, player):
        """Human player's turn to play."""
        # Checks if the player is busted or staying, which if so, it will skip their turn.
        while not player.is_busted and not player.is_staying:
            print(f"{player.name}'s turn. Your cards: {player.display_hand()}")
            choice = input("Would you like to 'hit' or 'stand'? ").lower()
            if choice == 'hit':
                player.add_card(self.deck.draw_card())
                print(f"{player.name} now has {player.display_hand()} and a value of: {player.hand_value()}")
                if player.is_busted:
                    print(f"{player.name} has gone over 21!")
                    print("\n")
                    break
            elif choice == 'stand':
                print("\n")
                player.stay()
                break


    def ai_plays(self, player):
        """AI player's turn to play."""
        # Checks if AI is busted or staying, which if so, it will skip their turn.
        while not player.is_busted and not player.is_staying:
            # decide_move() returns 'h' or 's' for hit or stay based on the AI's logic
            move = player.decide_move()
            while move == 'h':
                player.add_card(self.deck.draw_card())
                print(f"{player.name}, hit, so now it has a value of {player.hand_value()}")
                if player.hand_value() > 21:
                    player.bust()
                    print(f"{player.name} has gone over 21!")
                    return
                move = player.decide_move()
            player.stay()
        print(f"{player.name}'s final hand: {player.display_hand()} with a total of {player.hand_value()}")
    
    def check_winners(self):
        """Function that checks the outcome of the game, and saves the history of the game."""
        for player in self.players:
            self.compare_scores(player)

        # Load existing data
        try:
            with open('history/history.json', 'r') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []

        try:
            with open('history/ai_history.json', 'r') as f:
                existing_ai_data = json.load(f)
        except FileNotFoundError:
            existing_ai_data = []

        # Append new data
        existing_data.extend(self.all_players_history)
        existing_ai_data.extend(self.ai_players_history)

        # Prints the history of the game to be saved into the history.json or ai_history.json file
        print("\nReal players' history to be saved: ")
        for player in self.all_players_history:
            print(player)
        print("\nAI players' history to be saved: ")
        for player in self.ai_players_history:
            print(player)

        # Write ai players' history to a JSON file
        with open('history/ai_history.json', 'w') as f:
            json.dump(existing_ai_data, f, indent=4)

        # Write real players' history to a JSON file
        with open('history/history.json', 'w') as f:
            json.dump(existing_data, f, indent=4) # Indent for easier reading, otherwise it'll all be one line.
            
    def compare_scores(self, player):
        """Function that compares the player's score to the dealer's score to determine outcome."""
        if player.is_dealer:
            return
        # Finds the dealer to start comparing scores
        dealer = next(p for p in self.players if p.is_dealer)
        dealer_score = dealer.hand_value()
        player_score = player.hand_value()

        # If the player and dealer have the same score, the player ties with the dealer.
        if (player_score == dealer_score and player_score <= 21):
            print(f"{player.name} ties with the dealer.")
            player.outcome = 'tie'
            if player.is_ai:
                self.ai_players_history.append(player.history_to_json())
            else:
                self.all_players_history.append(player.history_to_json())

        # If the player has a lower score than the dealer, the player loses.
        elif player_score < dealer_score and dealer_score <= 21:
            print(f"{player.name} loses, dealer has {dealer_score}, closer to 21 as the player has {player_score}.")
            player.outcome = 'loss'
            if player.is_ai:
                self.ai_players_history.append(player.history_to_json())
            else:
                self.all_players_history.append(player.history_to_json())

        # If the player has a higher score than the dealer, the player wins as long as the player is not busted.
        elif not player.is_busted and (player_score <= 21 or player_score > dealer_score or dealer_score > 21):
            print(f"{player.name} wins!")
            player.outcome = 'win'
            if player.is_ai:
                self.ai_players_history.append(player.history_to_json())
            else:
                self.all_players_history.append(player.history_to_json())

        # Self explanatory, if the player is busted, the player loses.
        elif player.is_busted:
            print(f"{player.name} loses by bust.")
            player.outcome = 'loss'
            if player.is_ai:
                self.ai_players_history.append(player.history_to_json())
            else:
                self.all_players_history.append(player.history_to_json())


    def play(self):
        self.player_options()
        self.check_winners()



