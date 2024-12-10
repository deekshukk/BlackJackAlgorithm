import random

# Create deck
def create_deck():
    ranks = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(str(rank), suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


# Calculate hand value
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card, _ in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            value += 11
            aces += 1
        else:
            value += int(card)
    
    # Adjust Aces if value exceeds 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

# Deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Display the current hand
def display_hand(hand, title):
    print(f"{title}: ", end="")
    for card, suit in hand:
        print(f"{card} of {suit}", end=", ")
    print()

# Game loop
def blackjack_game():
    # Initialize deck and hands
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Show initial hands
    display_hand(player_hand, "Player's Hand")
    print(f"Dealer's Hand: {dealer_hand[0][0]} of {dealer_hand[0][1]}, Hidden Card")
    
    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Your hand value: {player_value}")
        
        if player_value > 21:
            print("You busted! Dealer wins.")
            return
        
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
            display_hand(player_hand, "Player's Hand")
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")
    
    # Dealer's turn
    print("\nDealer's Turn:")
    display_hand(dealer_hand, "Dealer's Hand")
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        display_hand(dealer_hand, "Dealer's Hand")
    
    # Determine the outcome
    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(player_hand)
    
    print(f"\nYour hand value: {player_value}")
    print(f"Dealer's hand value: {dealer_value}")
    
    if dealer_value > 21:
        print("Dealer busted! You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    blackjack_game()



