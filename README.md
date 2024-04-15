[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kKc126dy)
![Header](../../actions/workflows/py-header.yml/badge.svg)
![Lint](../../actions/workflows/py-lint.yml/badge.svg)
![Format](../../actions/workflows/py-format.yml/badge.svg)

# Blackjack

The objectives of this exercise are:

* Write a game that is multiplayer and turn based
* Use a complicated rule set
* Learn to use namedtuples to represent data
* Learn to use object serialization to save data to a file
* Improving our programming practices

We shall all write the card game named [Blackjack](https://en.wikipedia.org/wiki/Blackjack). Blackjack is a casino banking game where the player competes against the house or casino to have the best hand of cards. Unlike many other familiar card games, the players do not compete against each other or help one another. The game is played using one or more decks of common playing cards, also known as a French decks.

In your [recommended reading](https://docs.google.com/document/d/184U-IQ0DrmlVlPMySjKaYxq2M-ScNvgX8NRa1Kkuk9Q/edit), the book [_Luck, logic, and white lies : the mathematics of games_](https://csu-fullerton.primo.exlibrisgroup.com/permalink/01CALS_FUL/10o4t9/alma991013418479202908) offers a brief and excellent introduction to the mathematics of Blackjack in Chapter 17. You are strongly encouraged to read this chapter.

Since there are so many variations, it is important that you pay close attention to the rules and requirements described in this assignment. Please do not adopt rules that you may use with your friends or what you may have experienced at a Casino.

In the game, the dealer represents the house/bank/casino. There must be at least one player. The dealer shuffles 8 decks of cards and cuts the deck. A _cut card_ is placed randomly between the 60th and 80th card from the bottom of the deck. All the cards are placed in a [_shoe_](https://en.wikipedia.org/wiki/Shoe_(cards)) which the dealer uses to deal cards one at a time. When the dealer reaches the _cut card_, then, when the game ends, the cards are shuffled, cut, a _cut card_ is placed, and the cards are returned to the _shoe_.

The dealer deals cards to the players from their left to their right. Each player receiving one card face up. The dealer deals themself a face up card and then deals another card to each player. Finally, the dealer deals one face down card to themself.

Once the cards are dealt, each player has a turn. Starting with the first player, the player must first decide if she would like to _double down_. 

Once those initial decisions are made, the player chooses to _hit_, take a card, or _stand_, end their turn. The player attempts to reach a sum as close as possible to 21. The sum is calculated by converting the _rank_ of a card to a numerical value. Number cards (2, 3, 4, 5, 6, 7, 8, 9) have a value equal to their rank. Court cards (Jack, Queen, King) have a value equal to 10. Aces can have a value of 1 or 11; whichever is most advantageous to the player. A special case is _blackjack_ or _a natural_ where a player or dealer has an Ace and a card that has a value of 10 such as a 10, Jack, Queen, or King. The suit of a card (Clubs, Hearts, Spades, Diamonds) does not matter in this game.

A player wins when their hand has a higher value than the dealer's yet is not greater than 21. Players that pass 21 are _busted_ which means they loose their bet regardless of what the dealer does.

When a player and the dealer have the same value for their respective hands, then this is a _push_. A _push_ means that no one wins and the player does not lose her wager.

The dealer is always last to play. The dealer begins by turning over the face down card and deciding to _hit_ or _stand_. Unlike the players, the dealer must _hit_ if their hand value is less than 17. If the value of their hand is 17 or greater, then the dealer _stands_. If all the players have already _busted_ the dealer _stands_ thus removing the chance that the dealer may _bust_ as well.

(There are not _splits_.) If the dealer's face up card has a value of 10 or higher, then the player may also buy _insurance_ as a side bet. Some versions of Blackjack allow a player to _surrender_, however our version will not have this rule.

The side bet that is available to a player is _doubling down_. This game does not allow _splits_, buying _insurance_, or _surrendering_.

The player may choose to _double down_ at the start of their turn. To _double down_, the player doubles her bet on her cards and takes one additional card before ending her turn. For example, if the player has an 4 of Diamonds and a King of Hearts, then she may double down believing that she only wants one additional card and that will be enough to beat the dealer. If she is dealt a 7, she has 21. Otherwise, any card less than an 8 will keep her in the game. Should the dealer lose then the player earns winnings on her initial wager and on her _double down_ bet. The _double down_ bet must be equal to the player's initial wager. A player must have the funds in her bank roll to _double down_.

All bets are _two-to-one_ payout. In other words, if a player wagers $5 and wins, then the casino pays the player $5 and the player keeps the original wager thus pocketing a total of $10.

In our game, the dealer shall be played by a game AI. Although not required, you may find it advantageous to have bots play as well to test the game and to make the game more interesting for single players. All players start with $10,000.00 in their bank balance. The minimum bet is $1 and the maximum bet is the player's bank balance. When a player goes broke (loses all of her money), then the player is offered $10,000.00 from an anonymous donor.

Most importantly, the player shall be able to exit the game and restart the game and have the same bank balance when the game is restarted. This means that players must use a unique identifier to start the game which can be a name, handle, email address, etc. The identifier is used to track the player's progress such that their bank balance from previous games can be reused.


If there is more than one player, the game is played as a [hotseat](https://en.wikipedia.org/wiki/Hotseat_(multiplayer_mode)) multiplayer game.

## Rules

* There is at least one players playing the game and at most four.
* To start the game, a player can enter the number 1 through 4 to establish how many players there are.
* All players start with $10,000.00 in their bank balance.
* The dealer is always a computer AI and has unlimited funds.
* The game is turn based.
* All players have a name, including the _computer AI_. Players' names may be used as unique identifiers or additional information can be gathered.
* Unique identifiers are used to serialize the game state to a file so that a player can have their bank balance upon return to the game.
* The game is played with 8 decks of cards. The cards are typical cards with the ranks Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King and the suits Clubs, Hearts, Spades, Diamonds. There are no jokers.
* The value of the cards is the rank of the card except for Ace, Jack, Queen, and King. An Ace's value is either 1 or 11 depending on what is most advantageous to the hand in question. Jacks, Queens, and Kings have a value of 10.
* Before playing, the cards must be shuffled and cut.
* A cut card is placed randomly between the 60th and 80th card from the bottom of the deck.
* The players play in the order their names are entered when the program starts. The dealer always goes last.
* Once each player has had a turn in ascending order, the turn returns to the first player. (The process is a circular queue.)
* The game is made up of many games. The players continue playing games of blackjack. At the end of every game, the game prompts the first player if they would like to play again. An answer of _yes_ means the dealer will deal cards out to the same players who played previously. With multiple players, should one choose to leave then the first player must answer _no_ to end the game and exit the program.
* At the start of every game, before cards are dealt, each player must place a wager. A wager can be at least $1 and at most their bank balance.
* A player may not wager more money than she has in her bank balance.
* The cards are dealt one by one, starting with the first player and ending on the dealer.
* The dealer's second card is kept hidden from the players; all other cards are dealt face up.
* At the beginning of every turn, the game displays what cards the current player is holding and what face up card the dealer has showing.
* Whenever a card is dealt, it is printed or shown to the players before taking any other action.
* When it is the dealer's turn, the dealer must turn over (print or show) the face down card before taking any other action.
* All bets pay out 2 to 1.
* When a players turn begins, they have the option to _double down_.
* A player may not _surrender_, _split_, or buy _insurance_.
* The player may _double down_ when her turn starts and never later.
* The player may _double down_ if and only if there is sufficient funds in her balance to double her wager.
* A player is prompted to _hit_ or _stand_ unless they are _busted_ or have _21_. If they have _busted_ or have _21_ then a message is shown stating that they have _busted_ or reached _21_.
* The dealer must _hit_ on a hand that is less than 17. The dealer must _stand_ on a hand that is 17 or greater.
* The dealer only _hits_ if there are players who are not _busted_.
* No one wins or loses when there is a _push_.
* A dealer does not place bets which means the dealer does not _double down_.


To summarize the order of game play operations:
1. If needed, cards are shuffled, cut, and a cut card is placed in a position between the 60th and 80th card from the bottom.
1. For each player, a wager is entered before the cards are dealt.
1. Cards are dealt one at a time starting with the first player, continuing through to the last player, and ending on the dealer. This is done twice such that each player and the dealer has two cards. The dealer's last card is kept face down until it is the dealer's turn.
1. For each player, begin their turn.
    1. For each hand, offer to _double down_. For each _double down_ wager, the player's wager is doubled.
    1. While the player's hand is less than 21 or is not busted, offer the player to _hit_ or _stand_. When the player _hits_ deal an additional card. If the player _stands_, then the player's turn concludes.
1. The dealer plays last. If there exists a player who is not busted, then the dealer must play their hand according to the rules. Otherwise, the dealer stands.
1. For each player, determine if the player has won, lost, or _pushed_. Update all the players' balances to reflect the outcome of the game.

## Requirements

The requirements of the program are that the game must play according to the rules given above. If there is any ambiguity of the rules, the the student should discuss the rules with the instructor to clarify the rules.

The only valid input are the number keys ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and the keys 'y' and 'n'. All input is lower case.
 
The game must be written in Python 3. Limit your game to use only what is available in the Python Standard Library. Do not use additional Python modules that are outside of the Python Standard Library.

To run the game, the command must be `./blackjack.py`. This means that the file `blackjack.py` must have a shebang and call the main game loop. This file contains only a call to the game's main loop which is defined in the `blackjackgame` package.

The game's logic must be defined in a package named `blackjackgame`. This means there must be a directory named `blackjackgame` which contains all the Python source code for the project. At a minimum, the following files must be included in the `piggame` package:
* `__init__.py`
* `cards.py`
* `game.py`
* `player.py`

The file `__init__.py` can be a very simple file which defines an `__all__` variable for the package. See the documentation about [Python modules](https://docs.python.org/3/tutorial/modules.html), specifically [Section 6.4.1. Importing * From a Package](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package).

The file `cards.py` defines the playing cards and deck class along with any other supporting classes and functions needed to realize the game. _The card class must be defined as a named tuple._

The file `game.py` defines the game loop and any other supporting classes and functions needed to realize the game. The game loop may be defined as a function or as a class.

The file `player.py` defines the human player class and the _computer AI_. Additional classes and functions related to the players may be included as well. The player class must be serializable to a [Python Pickle](https://docs.python.org/3/library/pickle.html) such that their bank balance can be recalled when the game restarts.

The source file that is the executable file shall be named `blackjack.py`, and it shall be executable with a shebang at the top of the file.

The user interface of the game is text. There are no graphics (2D, 3D, sprites, etc.) in this game. You may use Unicode characters in your program.

If you would like to use audio effects or a soundtrack, you may however the program may only use what's available in the Python Standard Library.

The _computer AI_ dealer must behave according to the rules specified.

Since this game is a terminal based game, use [sleep](https://docs.python.org/3/library/time.html?highlight=sleep#time.sleep) or other similar mechanism to slow down the game to make the text appear on the screen slowly. Give the player an opportunity to read the text. A typewriter effect can be achieved with some creative use `time.sleep` with values less than 1 second.

## Suggestions

Write a bot such that you can automate the gameplay. This will help you test the game without having to interact with the game. Make the bot scriptable or predictable so you can observe how your game behaves.

You may be interested in learning more about the mathematics of Blackjack so you can improve your bot or improve your own gameplay. In your [recommended reading](https://docs.google.com/document/d/184U-IQ0DrmlVlPMySjKaYxq2M-ScNvgX8NRa1Kkuk9Q/edit), the book [_Luck, logic, and white lies : the mathematics of games_](https://csu-fullerton.primo.exlibrisgroup.com/permalink/01CALS_FUL/10o4t9/alma991013418479202908) offers a brief and excellent introduction to the mathematics of Blackjack in Chapter 17. The class text on Blackjack is [_Beat The Dealer_](https://csu-fullerton.primo.exlibrisgroup.com/permalink/01CALS_FUL/10o4t9/alma991008534019702908). A more mathematically oriented book is available from the library as an ebook, [_Risk and Reward: The Science of Casino Blackjack_](https://csu-fullerton.primo.exlibrisgroup.com/permalink/01CALS_FUL/10o4t9/alma991013452793402908). A book that covers all casino games and can be found inexpensively as a used book is [_Darwin Ortiz on Casino Gambling_](https://www.amazon.com/Darwin-Ortiz-Casino-Gambling-Complete/dp/0818405252/).

If you want to discourage reckless gameplay, add the rule that a player must wait a period of time before their bank balance is replenished by the anonymous donor. This could mean that if four players are playing and one of the players goes bankrupt, they must wait _n_ rounds before being offered additional funds. Another possibility is to have the player forced to exit the game and wait _n_ hours or days before receiving additional funds.

Write tests for your project. A small investment in writing tests will improve the quality of your work as well as teach you a very valuable skill. Python has a framework aptly named [`unittest`](https://docs.python.org/3/library/unittest.html). The documentation is very good and it is easy to get started.

## Don't Forget

Please remember that:

* You need to put a header in every file per the [instructions](https://docs.google.com/document/d/1OgC3_82oZHpTvoemGXu84FAdnshve4BCvtwaXZEJ9FY/edit?usp=sharing) shared in Canvas.
* You need to follow [PEP-8](https://www.python.org/dev/peps/pep-0008/); use linters and style checkers such as `pycodestyle`, `pylint`, and `black`.
* You need to test your program. If it does not run correctly or if it unplayable then your project will receive poor marks.

# Rubric

This exercise is worth 15 points. Your program must not have any syntax errors before it is graded. Submissions that have a syntax error or throw an uncaught exception will be assigned a score of 0.

* Executable (1 point): Is a standalone program that executes with the command './blackjack.py'.
* Object Oriented Using a Python Module (5 points): The main function calls code defined in a blackjack module. Most if not all game code is in the module. The module contains objects which represent elements of the game. The files are named according to the requirements.
* Game Rules (5 points): Implementation of the game rules per the requirements given in the README, including but not limited to: hit or stand, doubledown, AI dealer, multiplayer.
* Data Persistance (2 points): The bank balance is saved to a pickle file and can be recalled upon subsequent program executions.
* Formatting & Linting (2 points)
