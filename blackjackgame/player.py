class Player:
    """Player class that handles both human and AI players."""

    def __init__(self, name, bankroll=10000, is_ai=False):
        self.name = name
        self.bankroll = bankroll
        self.is_ai = is_ai
        self.hand = []
        self.is_staying = False  # Boolean to track if player is staying
        self.is_busted = False   # Boolean to track if player has busted

    def add_card(self, card):
        """Adds a card to the player's hand."""
        self.hand.append(card)
        self.check_bust()

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

    def display_hand(self):
        """Returns a formatted string of the player's hand."""
        return ', '.join([str(card) for card in self.hand])


    def bust(self):
        """Sets the player's bust status."""
        self.is_busted = True


    def __str__(self):
        """Returns a string representation of the player."""
        hand_description = self.display_hand() if self.hand else "No cards"
        return f"{self.name} has a balance of {currency(self.bankroll)} and holds: {hand_description}"
