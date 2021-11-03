#Run script and input hand followed by o or s to indicate if its suited or not.
#Input must be between 2 and 3 characters, pockets obviously need no suit indicator and can be simply entered as QQ or 66.
#enter fold to exit


handlist = ["AAp", "KKp", "QQp", "AKs", "JJp", "AQs", "KQs", "AJs", "KJs", "TTp", "AKo", "ATs", "QJs", "KTs", "QTs", "JTs", "99p", "AQo", "A9s", "KQo", "88p", "K9s", "T9s", "A8s", "Q9s", "J9s", "AJo", "A5s", "77p", "A7s", "KJo", "A4s", "A3s", "A6s", "QJo", "66p", "K8s", "T8s", "A2s", "98s", "J8s", "ATo", "Q8s", "K7s", "KTo", "55p", "JTo", "87s", "QTo", "44p", "33p", "22p", "K6s", "97s", "K5s", "76s", "T7s", "K4s", "K3s", "K2s", "Q7s", "86s", "65s", "J7s", "54s", "Q6s", "75s", "96s", "Q5s", "64s", "Q4s", "Q3s", "T9o", "T6s", "Q2s", "A9o", "53s", "85s", "J6s", "J9o", "K9o", "J5s", "Q9o", "43s", "74s", "J4s", "J3s", "95s", "J2s", "63s", "A8o", "52s", "T5s", "84s", "T4s", "T3s", "42s", "T2s", "98o", "T8o", "A5o", "A7o", "73s", "A4o", "32s", "94s", "93s", "J8o", "A3o", "62s", "92s", "K8o", "A6o", "87o", "Q8o", "83s", "A2o", "82s", "97o", "72s", "76o", "K7o", "65o", "T7o", "K6o", "86o", "54o", "K5o", "J7o", "75o", "Q7o", "K4o", "K3o", "96o", "K2o", "64o", "Q6o", "53o", "85o", "T6o", "Q5o", "43o", "Q4o", "Q3o", "74o", "Q2o", "J6o", "63o", "J5o", "95o", "52o", "J4o", "J3o", "42o", "J2o", "84o", "T5o", "T4o", "32o", "T3o", "73o", "T2o", "62o", "94o", "93o", "92o", "83o", "82o", "72o"]

ask_again = "deal"
foundhand = False
rowcount = len(handlist)
pockets = bool(False)

while ask_again != 'fold':
    foundhand = bool(False)
    hole_cards = input('What are your hole cards? ')

    if hole_cards == 'fold':
        break

    while len(hole_cards) < 2 or len(hole_cards) > 3 and hole_cards != 'fold':
        print("\nError: Please provide hand using number or letter value followed by 's' if suited or 'o' if offsuit. E.g. AKs, T5o, 98s\n" + "Enter fold to exit script")

        hole_cards = input('So, what are your hole cards? ')

        if hole_cards == 'fold':
            break

    cards = hole_cards[:2].upper()
    if len(hole_cards) == 3:
        suited = hole_cards[2:]
    else: suited = 'p'


    if suited == 'o':
        suit = 'offsuit'
    if suited == 'p':
        suit = 'pockets'
    if suited == 's':
        suit = 'suited'

    cardone = cards[0]
    cardtwo = cards[1]

    #print(cards+suited)

    if cards[0] == 'A':
        cardone = 'Ace'
        pocketname = 'Aces'
    if cards[1] == 'A':
        cardtwo = 'Ace'
    if cards[0] == 'K':
        cardone = 'King'
        pocketname = 'Kings'
    if cards[1] == 'K':
        cardtwo = 'King'
    if cards[0] == 'Q':
        cardone = 'Queen'
        pocketname = 'Queens'
    if cards[1] == 'Q':
        cardtwo = 'Queen'
    if cards[0] == 'J':
        cardone = 'Jack'
        pocketname = 'Jacks'
    if cards[1] == 'J':
        cardtwo = 'Jack'
    if cards[0] == 'T':
        cardone = 'Ten'
        pocketname = 'Tens'
    if cards[1] == 'T':
        cardtwo = 'Ten'
    if cards[0] == '9':
        pocketname = 'Nines'
    if cards[0] == '8':
        pocketname = 'Eights'
    if cards[0] == '7':
        pocketname = 'Sevens'
    if cards[0] == '6':
        pocketname = 'Sixes'
    if cards[0] == '5':
        pocketname = 'Fives'
    if cards[0] == '4':
        pocketname = 'Fours'
    if cards[0] == '3':
        pocketname = 'Threes'
    if cards[0] == '2':
        pocketname = 'Twos'

    if cardone == cardtwo:
        pockets = bool(True)

    if (cards + suited) in handlist:
        rank = int(handlist.index(cards + suited)) + 1
        foundhand = bool(True)
    if foundhand != (True) and (cards[::-1] + suited) in handlist:
        rank = int(handlist.index(cards[::-1] + suited)) + 1
        foundhand = bool(True)
    if foundhand != (True) and hole_cards != 'fold':
        print('Hand not found.')
    #print(rank)
    if foundhand == True and pockets == False:
        rankpercent = float(rank / rowcount * 100)
        rankround = round(rankpercent,2)

        print('The hand ' + cardone + ' ' + cardtwo + ' ' + suit + ' is rank ' + str(rank) + '/' + str(rowcount)  + ' and top ' + str(rankround) + '% of hands before the flop.')

    if foundhand == True and pockets == True:
        rankpercent = float(rank / rowcount * 100)
        rankround = round(rankpercent,2)

        print('Pocket ' + pocketname + ' are rank ' + str(rank) + '/' + str(rowcount)  + ' and top ' + str(rankround) + '% of hands before the flop.')

    cards = ''
    suited = ''
    suit = ''
    rank = int(0)
    rankpercent = int(0)
    rankround = int(0)
    cardone = ''
    cardtwo = ''
    pockets = False

    ask_again = hole_cards