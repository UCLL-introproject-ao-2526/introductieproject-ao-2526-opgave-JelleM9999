# black jack in python wth pygame!
import copy
import random
import pygame

pygame.init()
# game variables

# Kaarten moeten nu als tuples worden opgeslagen voor zowel de waarde and het symbool
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['♠', '♥', '♦', '♣']

one_deck = []
for suit in card_suits:
    for value in card_values:
        one_deck.append((value, suit))

decks = 4
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack!')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)
suit_font = pygame.font.SysFont('segoeuisymbol', 36)
value_font = pygame.font.SysFont('freesansbold.ttf', 46)
title_font = pygame.font.Font('freesansbold.ttf', 72)
tiny_font = pygame.font.Font('freesansbold.ttf', 15)
active = False
# win, loss, draw/push
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['', 'PLAYER BUSTED o_O', 'Player WINS! :)', 'DEALER WINS :(', 'TIE GAME...']

# kleur variabelen voor achtergrond
BG_COLOR = (53, 101, 77)    # casino groen
BORDER_COLOR = (30, 60, 45) # iets donkerder groen voor de rand

# bijhouden of het welkomscherm al gedaan is of neit
game_started = False


# functie om het welkomstscherm te tekenen
def draw_welcome():
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, BORDER_COLOR, [10, 10, WIDTH - 20, HEIGHT - 20], 8, 10)

    # grote titel vooraan
    screen.blit(title_font.render('BLACKJACK', True, 'gold'), (60, 280))

    # kaart-symbolen als decoratie op het scherm
    screen.blit(suit_font.render('♠  ♥  ♦  ♣', True, 'white'), (200, 380))

    # instructie onderaan wat je moet doen 
    screen.blit(smaller_font.render('Druk SPATIE om te starten', True, 'white'), (60, 480))
    screen.blit(smaller_font.render('of klik ergens', True, (180, 220, 180)), (175, 530))
    screen.blit(tiny_font.render('Made by Jelle for OPO "Introduction Project', True, (180, 220, 180)), (25, 25))



# deal cards by selecting randomly from deck, and make function for one card at a time
def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card - 1])
    current_deck.pop(card - 1)
    return current_hand, current_deck


# draw scores for player and dealer on screen
def draw_scores(player, dealer):
    screen.blit(font.render(f'Score[{player}]', True, 'white'), (350, 400))
    if reveal_dealer:
        screen.blit(font.render(f'Score[{dealer}]', True, 'white'), (350, 100))


# draw cards visually onto screen
def draw_cards(player, dealer, reveal):
    for i in range(len(player)):

        # de kaartnaam en suit uit de tuple halen voor de juiste kleur en weergave
        card_value = player[i][0]
        card_suit = player[i][1]

        # harten en ruiten zijn rood,schoppen en klaveren zijn zwart
        if card_suit in ['♥', '♦']:
            text_color = 'red'
        else:
            text_color = 'black'

        pygame.draw.rect(screen, 'white', [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
        
        # de kaartwaarde en het symbool op de kaart tekenen, met de juiste kleur en symbool dus linksboven en rechtsonder
        screen.blit(value_font.render(card_value, True, text_color), (80 + 70 * i, 470+ 5 * i))
        screen.blit(suit_font.render(card_suit, True, text_color), (80 + 70 * i, 490 + 5 * i))
        screen.blit(suit_font.render(card_suit, True, text_color), (150 + 70 * i, 600 + 5 * i))
        screen.blit(value_font.render(card_value, True, text_color), (150 + 70 * i, 645 + 5 * i))
        pygame.draw.rect(screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

    for i in range(len(dealer)):
        card_value = dealer[i][0]
        card_suit = dealer[i][1]

        if card_suit in ['♥', '♦']:
            text_color = 'red'
        else:
            text_color = 'black'

        pygame.draw.rect(screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
        if i != 0 or reveal:
            screen.blit(value_font.render(card_value, True, text_color), (80 + 70 * i, 165 + 5 * i))
            screen.blit(suit_font.render(card_suit, True, text_color), (80 + 70 * i, 185 + 5 * i))
            screen.blit(suit_font.render(card_suit, True, text_color), (150 + 70 * i, 300 + 5 * i))
            screen.blit(value_font.render(card_value, True, text_color), (150 + 70 * i, 325 + 5 * i))
        else:
            # verborgen kaart van de dealer dieie nog niet zichtbaar is, dus gewoon vraagtekens weergeven
            screen.blit(value_font.render('???', True, 'black'), (80 + 70 * i, 165 + 5 * i))
            screen.blit(value_font.render('???', True, 'black'), (80 + 70 * i, 335 + 5 * i))
        pygame.draw.rect(screen, 'blue', [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)



# de calculate_score functie leest nu de kaartnaam uit de tuple via hand[i][0]
def calculate_score(hand):
    hand_score = 0
    aces_count = 0

    # eerst moeten het aantal azen geteld wordenn
    for i in range(len(hand)):
        if hand[i][0] == 'A':
            aces_count += 1

    for i in range(len(hand)):
        value = hand[i][0]  # de kaartnaam uit de tuple halen

        # voor 2 t/m 9: gewoon het getal optellen
        if value in ['2', '3', '4', '5', '6', '7', '8', '9']:
            hand_score += int(value)
        # voor 10 en figuurkaarten: 10 punten
        elif value in ['10', 'J', 'Q', 'K']:
            hand_score += 10
        # voor aas: begin met 11
        elif value == 'A':
            hand_score += 11

    # als het te hoog is : dan moet elke aas teruggezet worden van 11 naar 1
    if hand_score > 21 and aces_count > 0:
        for i in range(aces_count):
            if hand_score > 21:
                hand_score -= 10

    return hand_score


# draw game conditions and buttons
def draw_game(act, record, result):
    button_list = []
    # initially on startup (not active) only option is to deal new hand
    if not act:
        deal = pygame.draw.rect(screen, 'white', [150, 20, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [150, 20, 300, 100], 3, 5)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, (165, 50))
        button_list.append(deal)
    # once game started, shot hit and stand buttons and win/loss records
    else:
        hit = pygame.draw.rect(screen, 'white', [30, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [30, 700, 300, 100], 3, 5)
        hit_text = font.render('HIT ME', True, 'black')
        screen.blit(hit_text, (55, 735))
        button_list.append(hit)
        stand = pygame.draw.rect(screen, 'white', [270, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [270, 700, 300, 100], 3, 5)
        stand_text = font.render('STAND', True, 'black')
        screen.blit(stand_text, (355, 735))
        button_list.append(stand)
        score_text = smaller_font.render(f'Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}', True, 'white')
        screen.blit(score_text, (15, 840))
    # if there is an outcome for the hand that was played, display a restart button and tell user what happened
    if result != 0:
        screen.blit(font.render(results[result], True, 'white'), (15, 25))
        deal = pygame.draw.rect(screen, 'white', [150, 220, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [150, 220, 300, 100], 3, 5)
        pygame.draw.rect(screen, 'black', [153, 223, 294, 94], 3, 5)
        deal_text = font.render('NEW HAND', True, 'black')
        screen.blit(deal_text, (165, 250))
        button_list.append(deal)
    return button_list


# check endgame conditions function
def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    # check end game scenarios is player has stood, busted or blackjacked
    # result 1- player bust, 2-win, 3-loss, 4-push
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            result = 2
        elif play_score < deal_score <= 21:
            result = 3
        else:
            result = 4
        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False
    return result, totals, add


# main game loop
run = True
while run:
    # run game at our framerate and fill screen with bg color
    timer.tick(fps)

    # welkomstscherm afhandelen
    if not game_started:
        draw_welcome()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # spatie of muisklik om te starten
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_started = True
            if event.type == pygame.MOUSEBUTTONUP:
                game_started = True
        pygame.display.flip()
        continue  # sla de rest van de loop over totdat het spel gestart is

    # Casino groene achtergrond toevoegen
    screen.fill(BG_COLOR)

    # Decoratieve rand toevoegen rond het scherm
    pygame.draw.rect(screen, BORDER_COLOR, [10, 10, WIDTH - 20, HEIGHT - 20], 8, 10)

    # Mooie gouden titel als het spel nog nit gestart is tonen
    if not active:
        screen.blit(font.render('BLACKJACK', True, 'gold'), (165, 430))
        
    # initial deal to player and dealer
    if initial_deal:
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        initial_deal = False
    # once game is activated, and dealt, calculate scores and display cards
    if active:
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)
    buttons = draw_game(active, records, outcome)

    # event handling, if quit pressed, then exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    reveal_dealer = False
                    outcome = 0
                    add_score = True
            else:
                # if player can hit, allow them to draw a card
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                # allow player to end turn (stand)
                elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
                elif len(buttons) == 3:
                    if buttons[2].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        reveal_dealer = False
                        outcome = 0
                        add_score = True
                        dealer_score = 0
                        player_score = 0


    # if player busts, automatically end turn - treat like a stand
    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

    pygame.display.flip()
pygame.quit()
