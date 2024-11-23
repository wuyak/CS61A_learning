import random
from re import I
import readline
import sqlite3

class BlackjackGame:

    def __init__(self):
        self.points = {'J':10, 'Q':10, 'K':10, 'A':1}
        self.points.update({n:n for n in range(2, 11)})
        self.db = sqlite3.Connection('cards.db')
        self.sql = self.db.execute
        self.sql('drop table if exists cards')
        self.sql('create table cards (card, who);')

        self.player, self.dealer = "Player", "Dealer"
        self.player_wins, self.dealer_wins = 0, 0
        self.draws = 0
        self.min_cards = 10

        """ result key about print mesage and the winner """
        self.result_messages = {
                'player_bust' : lambda self: (f"{self.player} busts! {self.dealer} wins!", self.dealer),
                'dealer_bust' : lambda self: (f"{self.dealer} busts! {self.player} wins!", self.player),
                'player_win' : lambda self: (f"{self.player} wins!", self.player),
                'dealer_win' : lambda self: (f"{self.dealer} wins!", self.dealer),
                'draw': lambda self: ("It's a draw!", 'draw')
                }

        self.deck = self.create_new_deck()

    def create_new_deck(self):
        deck = list(self.points.keys()) * 4
        random.shuffle(deck)
        self.sql('delete from cards where who="Discard"')
        return deck

    def hand_score(self,hand):
        """ Total score for a hand. """
        total = sum(self.points[card] for card in hand)
        if total <= 11 and 'A' in hand:
            return total + 10
        return total

    def deal(self,card, who):
        """ Deal a card face up. """
        self.sql('insert into cards values (?, ?)', (card, who))
        self.db.commit()
        print(self.sql('select * from cards where who <> "Discard"').fetchall())

    def score(self, who):
        """ compute the hand score for the player or dealer. """
        cards = self.sql("select * from cards where who = ?", [who])
        card_values = [card for card, _ in cards.fetchall()]
        return self.hand_score(card_values)

    def show_score(self):
        """ print score and return the result. """
        score_player, score_dealer = self.score(self.player), self.score(self.dealer)
        print(f"{self.player}: {score_player} and {self.dealer}: {score_dealer}")
        return (score_player, score_dealer)

    def compare_score(self):
        (score_player, score_dealer) = self.show_score()
        if score_player > score_dealer:
            return 'player_win'
        if score_dealer > score_player:
            return 'dealer_win'
        return 'draw'

    def show_statistics(self):
        print(f"{self.player} wins: {self.player_wins},\n{self.dealer} wins: {self.dealer_wins},\ndraws: {self.draws}")

    def update_statistics(self, winner):
        if winner == self.player:
            self.player_wins += 1
        elif winner == self.dealer:
            self.dealer_wins += 1
        else:
            self.draws += 1

    def handle_game_result(self, result_type):
        """ read the result_messages dictionary to output and update statistics"""
        message, winner = self.result_messages[result_type](self)
        print(message)
        self.update_statistics(winner)

    def bust(self, who):
        """ check if the player or dealer went bust. """
        if self.score(who) > 21:
            self.show_score()
            return True
        return False

    def play_hand(self):
        """ play a hand of BlackjackGame """
        self.deal(self.deck.pop(), self.player)
        self.deal(self.deck.pop(), self.dealer)
        self.deal(self.deck.pop(), self.player)
        hidden = self.deck.pop()
        player_status = self.get_player_action()
        if player_status == "bust":
            self.handle_game_result('player_bust')
            return

        self.deal(hidden, self.dealer)
        while self.score(self.dealer) < 17:
            self.deal(self.deck.pop(), self.dealer)
            if self.bust(self.dealer):
                self.handle_game_result('dealer_bust')
                return

        result = self.compare_score()
        self.handle_game_result(result)

    def get_player_action(self):
        """ deal with all operation in player hand """
        while True:
            self.show_score()
            user_input = input("Continue get card? y/n").lower()
            if user_input == "cheat":
                discard_cards = self.sql('select card from cards where who=="Discard"')
                """
                The fetchall() method returns tuples like (6,) and (1,) to distinguish them
                from single values just like (6), (1). Therefore, even when dealing with single-element tuples,
                you need to use index[0] to access the actual value.
                """
                print("Discard cards:", [card[0] for card in discard_cards.fetchall()])
                print("Remaing cards: ", self.deck)
                continue
            if 'y' not in user_input:
                return "stand"
            self.deal(self.deck.pop(), self.player)
            if self.bust(self.player):
                print(self.player, 'went bust!')
                return 'bust'
            if self.score(self.player) == 21:
                break

    def play_game(self):
        try:
            while True:
                print(f"\nCards remaining: {len(self.deck)}")
                self.play_hand()
                self.sql('update cards set who = "Discard";')
                if len(self.deck) <= self.min_cards:
                    self.show_statistics()
                    user_input = input("Do you want to start a new game? y/n").lower()
                    if 'y' not in user_input:
                        print("\nThanks for playing!")
                        break
                    print('\nReshuffling the deck...')
                    self.deck = self.create_new_deck()
        except KeyboardInterrupt:
            self.show_statistics()
            print("\nThanks for playing!")
        finally:
            self.db.close()

if __name__ == "__main__":
    game = BlackjackGame()
    game.player = "Alice"
    game.dealer = "Jack"
    print("welcome to BlackjackGame")
    game.play_game()
