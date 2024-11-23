import random
import readline
import sqlite3

points = {'J':10, 'Q':10, 'K':10, 'A':1}
points.update({n:n for n in range(2, 11)})

def hand_score(hand):
    """ Total score for a hand. """
    total = sum(points[card] for card in hand)
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

db = sqlite3.Connection('cards.db')
sql = db.execute
sql('drop table if exists cards')
sql('create table cards (card, who);')

def deal(card, who):
    """ Deal a card face up. """
    sql('insert into cards values (?, ?)', (card, who))
    db.commit()
    print(sql('select * from cards where who <> "Discard"').fetchall())

def score(who):
    """ compute the hand score for the player or dealer. """
    cards = sql('select * from cards where who = ?', [who])
    return hand_score([card for card, who in cards.fetchall()])

def bust(who):
    """check if the player or dealer went bust."""
    return score(who) > 21

player, dealer = "Player", "Dealer"

def play_hand(deck):
    """ play a hand of blackjack """
    deal(deck.pop(), player)
    deal(deck.pop(), dealer)
    deal(deck.pop(), player)
    hidden = deck.pop()

    player_status = get_player_action(deck)
    if player_status == 'bust':
        return

    deal(hidden, dealer)
    while score(dealer) < 17:
        deal(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, 'went bust!')
            return

    print(player, score(player), "and", dealer, score(dealer))

def get_player_action(deck):
    """处理玩家回合的所有操作"""
    while True:
        user_input = input("Hit? ").lower()
        if user_input == "cheat":
            discard_cards = sql('select card from cards where who="Discard"')
            print("Discard cards:", [card[0] for card in discard_cards.fetchall()])
            continue
        if 'y' not in user_input:
            return "stand"
        deal(deck.pop(), player)
        if bust(player):
            print(player, "went bust!")
            return "bust"

def new_start():
    deck = list(points.keys()) * 4
    random.shuffle(deck)
    sql('delete from cards where who="Discard"')
    return deck

deck = new_start()

while True:
    if len(deck) <= 10:
        print('\nReshuffling the deck...')
        new_start()

    print('\ndealing...')
    play_hand(deck)
    sql('update cards set who="Discard";')
