import json
import random

class Player:
    """Player class that handles both human and AI players."""

    def __init__(self, name, bankroll=10000, is_ai=False, is_dealer=False):
        self.name = name
        self.bankroll = bankroll
        self.is_ai = is_ai
        self.is_dealer = is_dealer
        self.hand = []
        self.is_staying = False  # Boolean to track if player is staying
        self.is_busted = False   # Boolean to track if player has busted
        self.is_dealer = False   # Boolean to track if player is the dealer
        self.history = []        # List to store the player's hand history

    def add_card(self, card):
        """Adds a card to the player's hand."""
        self.hand.append(card)
        self.check_bust()
        if self.is_ai == False:
            self.history.append((self.hand_value(), 'h'))

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
        if self.is_ai == False:
            self.history.append((self.hand_value(), 's'))

    def result(self, result):
        self.history.append(result)

    def history_to_json(self):
        return {
            'history': [(hand_value, action) if isinstance(hand_value, int) else hand_value for hand_value, action in self.history],
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
     
    def is_dealer(self):
        return True

class AiPlayer(Player):
    """The AI player"""

    def __init__(self, pname = "AI", amount = 0, is_ai=True):
        super().__init__(pname, amount, is_ai)
        self.is_ai = True
        self.load_history()
        # with open('history.json', 'r') as f:
        #     json.dump(self.history, f)

    def load_history(self):
        with open('history.json', 'r') as f:
            self.history = json.load(f)

    def decide_move(self):
        current_hand_value = self.hand_value()
        # print(self.history)

        # first_game_history = self.history[0]['history']

        # Print the history of all games
        print(len(self.history))
        
        history = [move[1] for game in self.history for move in game['history'] if move[0] == current_hand_value]
        if not history:
            return random.choice(['h', 's'])
        
        return max(set(history), key=history.count)

    def is_ai(self):
        return True
    
