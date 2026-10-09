import random

# make a blackjack deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", ]

# Hold the players hand and dealers hand:
dealersHand = []
playerHand = []
splitPlayerHand = []
# Hold dealer and player wins:
dealerWins = 0
playerWins = 0
# split:
splitYesNo = False

# Resets game and all values:
def gameReset():
    global splitYesNo
    playerHand[:] = []
    dealersHand[:] = []
    splitPlayerHand[:] = []
    splitYesNo = False
    deck[:] = [2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A",
            2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "A", ]

# Draws cards:
def drawCards(player):
    card = random.choice(deck)
    player.append(card)
    deck.remove(card)

# Does the math to calculate each player's score and dealer score
def calculateHand(hand):
    total = 0
    ace = 0
    for card in hand:
        if card == 'A':
            total += 11
            ace += 1
        elif card == 'K':
            total += 10
        elif card == 'Q':
            total += 10
        elif card == 'J':
            total += 10
        else:
            total += card
    # Checks if ace busts player:
    #print(ace)
    while total > 21:
        if ace > 0:
            ace -= 1
            total -= 10
        else:
            return total
    return total

# Deals with the AI:
def dealerAI():
    while calculateHand(dealersHand) < 17:
        newcard = random.choice(deck)
        dealersHand.append(newcard)
        deck.remove(newcard)
    if playerHand[0] == 'A':
        while calculateHand(dealersHand) < 19:
            newcard = random.choice(deck)
            dealersHand.append(newcard)
            deck.remove(newcard)

def hit():
    playerHand.append(random.choice(deck))
    if calculateHand(playerHand) > 21:
        return
    else:
        print('You draw a "', playerHand[-1], '" with a total of:', calculateHand(playerHand))

    betting = True
    while betting == True:
        playerInput = input('Would you like to "hit" or "stay"?')
        # if player hits
        if playerInput == 'hit':
            playerHand.append(random.choice(deck))
            if calculateHand(playerHand) > 21:
                betting = False


            else:
                print('You draw a "', playerHand[-1], '" with a total of:', calculateHand(playerHand))


        # If player stays
        if playerInput == 'stay':
            betting = False
    return

def stay():
    global playerWins
    global dealerWins
    dealerAI()
    if splitYesNo == True:
        print('TESTING FIRST')
        if calculateHand(dealersHand) > 21 >= calculateHand(playerHand):
            print('Dealer busted with:,', dealersHand, '\nYou WIN')
            playerWins += 1
            splitStay()

        elif 21 < calculateHand(playerHand) and 21 < calculateHand(dealersHand):
            print('Player had:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('Dealer had:', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print("Both player and dealer busted!\nIts a draw")
            splitStay()

        elif 22 > calculateHand(playerHand) > calculateHand(dealersHand):
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('You WIN')
            playerWins += 1
            splitStay()

        elif calculateHand(playerHand) == calculateHand(dealersHand):
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('Round was a draw')
            splitStay()

        elif calculateHand(playerHand) < calculateHand(dealersHand) <= 21:
            print('It was close but in the end you Lose with your hand of:', playerHand, '& a total of:',
                  calculateHand(playerHand))
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('You LOSE')
            dealerWins += 1
            splitStay()

        else:
            print('You drew a', playerHand[-1], 'with a new total of:', calculateHand(playerHand), '& Busted')
            print('You BUSTED with your hand of:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('You LOSE')
            dealerWins += 1
            splitStay()



    else:
        if calculateHand(dealersHand) > 21 >= calculateHand(playerHand):
            print('Dealer busted with:,', dealersHand, '\nYou WIN')
            playerWins += 1
            return
        elif 21 < calculateHand(playerHand) and 21 < calculateHand(dealersHand):
            print('Player had:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('Dealer had:', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print("Both player and dealer busted!\nIts a draw")
            return
        elif 22 > calculateHand(playerHand) > calculateHand(dealersHand):
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('You WIN')
            playerWins += 1
            return
        elif calculateHand(playerHand) == calculateHand(dealersHand):
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('Round was a draw')
            return
        elif calculateHand(playerHand) < calculateHand(dealersHand) <= 21:
            print('It was close but in the end you Lose with your hand of:', playerHand, '& a total of:', calculateHand(playerHand))
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('You LOSE')
            dealerWins += 1
            return

        else:
            print('You drew a', playerHand[-1], 'with a new total of:',calculateHand(playerHand),'& Busted')
            print('You BUSTED with your hand of:', playerHand, 'With a total of:', calculateHand(playerHand))
            print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
            print('You LOSE')
            dealerWins += 1
            return

def splitStay():
    global playerWins
    global dealerWins
    print('& for your split hand:')
    if calculateHand(dealersHand) > 21 >= calculateHand(splitPlayerHand):
        print('Dealer busted with:,', dealersHand, '\nYou WIN')
        playerWins += 1

    elif 21 < calculateHand(splitPlayerHand) and 21 < calculateHand(dealersHand):
        print('Player had:', splitPlayerHand, 'With a total of:', calculateHand(splitPlayerHand))
        print('Dealer had:', dealersHand, 'With a total of:', calculateHand(dealersHand))
        print("Both player and dealer busted!\nIts a draw")

    elif 22 > calculateHand(splitPlayerHand) > calculateHand(dealersHand):
        print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
        print('Your hand was:', splitPlayerHand, 'With a total of:', calculateHand(splitPlayerHand))
        print('You WIN')
        playerWins += 1

    elif calculateHand(splitPlayerHand) == calculateHand(dealersHand):
        print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
        print('Your hand was:', splitPlayerHand, 'With a total of:', calculateHand(splitPlayerHand))
        print('Round was a draw')

    elif calculateHand(splitPlayerHand) < calculateHand(dealersHand) <= 21:
        print('It was close but in the end you Lose with your hand of:', splitPlayerHand, '& a total of:',
              calculateHand(splitPlayerHand))
        print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
        print('You LOSE')
        dealerWins += 1

    else:
        print('You drew a', splitPlayerHand[-1], 'with a new total of:', calculateHand(splitPlayerHand), '& Busted')
        print('You BUSTED with your hand of:', splitPlayerHand, 'With a total of:', calculateHand(splitPlayerHand))
        print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
        print('You LOSE')
        dealerWins += 1



def split():
    splitPlayerHand.append(playerHand[0])
    splitPlayerHand.append(random.choice(deck))
    playerHand.remove(playerHand[1])
    playerHand.append(random.choice(deck))
    print('Your split hands are:', playerHand, '&', splitPlayerHand, 'respectivly')
    betting = True
    while betting == True:
        playerInput = input('Would you like to "hit" or "stay" for first hand?')
        # if player hits
        if playerInput == 'hit':
            playerHand.append(random.choice(deck))
            if calculateHand(playerHand) > 21:
                print('Your hand was:', playerHand, '\nWith a new total of:', calculateHand(playerHand))
                print('You BUSTED!')
                betting = False
            else:
                print('You draw a "', playerHand[-1], '" with a total of:', calculateHand(playerHand))
        if playerInput == 'stay':
            print('Locked in!')
            betting = False
    # split hand bets:
    betting2 = True
    while betting2 == True:
        playerInput = input('Would you like to "hit" or "stay" for second hand?')
        # if player hits
        if playerInput == 'hit':
            splitPlayerHand.append(random.choice(deck))
            if calculateHand(splitPlayerHand) > 21:
                print('Your split hand was:', splitPlayerHand, '\nWith a new total of:', calculateHand(splitPlayerHand))
                print('You BUSTED!')
                betting2 = False
            else:
                print('You draw a "', splitPlayerHand[-1], '" with a total of:', calculateHand(splitPlayerHand))
        if playerInput == 'stay':
            print('Locked in your second hand!')
            betting2 = False




# determines who has won the game

# Main order of operations(game loop and more):
def main():
    global splitYesNo
    gameOn = True
    while gameOn == True:
        # Player and dealer draws a card:
        for cards in range(2):
            drawCards(playerHand)
            drawCards(dealersHand)

        # If Player's pair of cards are matching you can split.
        if playerHand[0] == playerHand[1]:
            print('The dealer shows a', dealersHand[0], 'with one card face down\nYour hand is:', playerHand, '\nWith a total of:',calculateHand(playerHand), 'Because your pair is matching you may split!')
            choice = input('would you like to "hit" or "split" or "stay"?')
            if choice == 'hit':
                hit()
                stay()
            elif choice == 'split':
                splitYesNo = True
                split()
                stay()
            elif choice == 'stay':
                stay()

        else:
            print('The dealer shows a', dealersHand[0], 'with one card face down\nYour hand is:', playerHand, '\nWith a total of:',calculateHand(playerHand))
            choice = input('would you like to "hit" or "stay"?')
            if choice == 'hit':
                hit()
                stay()
            elif choice == 'split':
                print('You dont have a pair! Cant do that at his time!')
            elif choice == 'stay':
                stay()


        # Restarts game:
        gameAgain = input('Another game? "yes" or "no"?')
        if gameAgain == 'yes':
            gameReset()
            gameOn = True
        elif gameAgain == 'no':
            gameOn = False
        else:
            gameOn = False
        # testing to get out of gameOn loop


    print(f'The dealer had {dealerWins} wins & the player had {playerWins} wins. \ntest OVER**************************')

if __name__ == "__main__":
    main()





# Extra:
def gameLoop():
    betting = True
    if playerHand[0] == playerHand[1]:
        print('You can "split" your pair of', playerHand[0], "'s. \nJust type 'split'")
    while betting == True:
        playerInput = input('Would you like to "hit" or "stay"?')
        # if player hits
        if playerInput == 'hit':
            playerHand.append(random.choice(deck))
            if calculateHand(playerHand) > 21:
                print('Your hand was:', playerHand, '\nWith a new total of:', calculateHand(playerHand))
                print('You BUSTED!')
                betting = False
            else:
                print('You draw a "', playerHand[-1], '" with a total of:', calculateHand(playerHand))

        # If player stays
        if playerInput == 'stay':
            dealerAI()
            if calculateHand(dealersHand) > 21:
                print('Dealer busted with:,', dealersHand, '\nYou WIN')
                betting = False
            elif calculateHand(playerHand) > calculateHand(dealersHand):
                print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
                print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
                print('You WIN')
                betting = False
            elif calculateHand(playerHand) == calculateHand(dealersHand):
                print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
                print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
                print('Round was a draw')
            else:
                print('The dealer had: ', dealersHand, 'With a total of:', calculateHand(dealersHand))
                print('Your hand was:', playerHand, 'With a total of:', calculateHand(playerHand))
                print('You LOSE')
                betting = False

        # If player wants to split:
        if playerInput == 'split':
            if playerHand[0] == playerHand[1]:
                split()
            else:
                print("You can't split right now!")
        # Testing in background for admin
        if playerInput == 'print':
            print(deck)
