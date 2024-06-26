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

import json
import random

class Player:
    """Player class that handles both human and AI players."""

    def __init__(self, name, is_ai=False, is_dealer=False):
        self.name = name
        self.is_ai = is_ai
        self.is_dealer = is_dealer
        self.hand = []
        self.is_staying = False  # Boolean to track if player is staying
        self.is_busted = False   # Boolean to track if player has busted
        self.is_dealer = False   # Boolean to track if player is the dealer
        self.player_history = [] # List to store the player's hand history
        self.history = []        # List to store the player's hand history
        self.done = False

    def add_card(self, card):
        """Adds a card to the player's hand."""
        self.hand.append(card)
        self.check_bust()
        if self.is_dealer == False:
            self.player_history.append((self.hand_value(), 'h'))

    def hand_value(self):
        """Calculates the hand value, taking into account the ace as 11 or 1."""
        value, aces = 0, 0
        for card in self.hand:
            if card.rank == 'Ace':
                value += 11
                aces += 1
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                value += int(card.rank)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def check_bust(self):
        """Check if the player has busted and update the is_busted status."""
        if self.hand_value() > 21:
            self.is_busted = True

    def stay(self):
        """Player decides to stay."""
        self.is_staying = True
        if self.is_dealer == False:
            self.player_history.append((self.hand_value(), 's'))

    def result(self, result):
        self.history.append(result)

    def history_to_json(self):
        """Converts the player's history to a json object."""
        return {
            'history': [(hand_value, action) if isinstance(hand_value, int) else hand_value for hand_value, action in self.player_history],
            'outcome': self.outcome  # 'win', 'loss', or 'tie'
        }    
    
    def display_hand(self):
        """Returns a formatted string of the player's hand."""
        return ', '.join([str(card) for card in self.hand])


    def bust(self):
        """Sets the player's bust status."""
        self.is_busted = True


    def __str__(self):
        """Returns a string representation of the player."""
        # hand_description = self.display_hand() if self.hand else "No cards"
        # return f"{self.name} has a balance of {currency(self.bankroll)} and holds: {hand_description}"


class Dealer(Player):
    """The AI player"""

    def __init__(self, pname="dealer", amount=0, is_dealer=True):
        super().__init__(pname, amount, is_dealer)
        self.is_dealer = True
        self.is_ai = False
     
    def is_dealer(self):
        return True

class AiPlayer(Player):
    """The AI player"""

    def __init__(self, pname = "AI", amount = 0, is_ai=True):
        super().__init__(pname, amount, is_ai)
        self.is_ai = True
        self.load_history()
        self.is_dealer = False

    # Loads history.json file to make decisions
    def load_history(self):
        with open('history/history.json', 'r') as f:
            self.history = json.load(f)

    def decide_move(self):
        """Decide the move based on the any player's history."""
        current_hand_value = self.hand_value()
        # Get the most common move for the current hand value for each game where the player won
        history = [move[1] for game in self.history if game['outcome'] == "win" for move in game['history'] if move[0] == current_hand_value]
        if not history:
            # If the player has never been in a situation where it wins with a current hand value, 
            # get the most common move for the current hand value for each game
            history = [move[1] for game in self.history for move in game['history'] if move[0] == current_hand_value]
            #If for any reason such entry doesn't exist, it will return a random choice
            if not history:
                return random.choice(['h', 's'])
        return max(set(history), key=history.count)

    def is_ai(self):
        return True
    
