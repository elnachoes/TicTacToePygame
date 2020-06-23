#this is a basic tictactoe game in pygame
#libraries 
import pygame
import time

#setup variables 
background = (0,0,0)
white_color = (255,255,255)
blue_color = (0,0,255)
red_color = (255,0,0)
position_location = [[(213,120),(639,120),(1065,120)],[(213,360),
(640,360),(1065,360)],[(213,600),(639,600),(1065,600)]]

#setup function and variables for the gamestate
def setup():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Tic Tac Toe!")
    print("welcome to Tic Tac Toe!")
    print("player_1")
    return {
        "running": True,
        "player": "player_1",
        "player_value": 1,
        "message": "",
        "font_color": white_color,
        "win": False,
        "tie": False,
        "screen": pygame.display.set_mode((1280,820)),
        "clock": pygame.time.Clock(),
        "position_stored": [[0 for x in range(3)] for y in range(3)]
    }

#draw function
def draw(game_state):
    screen = game_state["screen"]
    draw_game_board(game_state)
    position_stored = game_state["position_stored"]
    draw_text(game_state)
    draw_cirlces(game_state)
    pygame.display.flip()
    exit_game(game_state)

#draws player cirlces in correct positions
def draw_cirlces(game_state):
    screen = game_state["screen"]
    position_stored = game_state["position_stored"]
    player = game_state["player"]
    for x in range(3):
        for y in range(3):
            if position_stored[y][x] == 1:
                pygame.draw.circle(screen,red_color,(position_location[y][x]),50)
            elif position_stored[y][x] == 2:
                pygame.draw.circle(screen,blue_color,(position_location[y][x]),50)

#draws text stating player turns, wins, and ties
def draw_text(game_state):
    font_color(game_state)
    screen = game_state["screen"]
    text = game_state["message"]
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    message = font.render(text,False,game_state["font_color"])
    text_rect = message.get_rect(center = (639,760))
    screen.blit(message,text_rect)

#font color assigner
def font_color(game_state):
    win = game_state["win"]
    tie = game_state["tie"]
    player_value = game_state["player_value"]
    if win == True or tie == True:
        game_state["font_color"] = white_color
    else:
        if player_value == 1:
            game_state["font_color"] = red_color
        elif player_value == 2:
            game_state["font_color"] = blue_color

#def draw_title_Board(game_state):
    
#draws the game board
def draw_game_board(game_state):
    screen = game_state["screen"]
    screen.fill(background)
    #vertical lines
    pygame.draw.line(screen,white_color,(426,0),(426,720),2)
    pygame.draw.line(screen,white_color,(853,0),(853,720),2)
    #horizontal lines
    pygame.draw.line(screen,white_color,(0,240),(1280,240),2)
    pygame.draw.line(screen,white_color,(0,480),(1280,480),2)
    pygame.draw.line(screen,white_color,(0,720),(1280,720),2)
    #borderlines
    pygame.draw.line(screen,white_color,(0,0),(1280,0),2)
    pygame.draw.line(screen,white_color,(0,800),(1280,800),2)
    pygame.draw.line(screen,white_color,(0,0),(0,800),2)
    pygame.draw.line(screen,white_color,(1280,0),(1280,800),6)

#gets mouse location and assignes a player value to position storred
def handle_mouse(game_state):
    player_value = game_state["player_value"]
    mouse_position = pygame.mouse.get_pos()
    #game_state["message"] = ("player "+ str(player_value) + " turn")
    if mouse_position[1] <= 240:
        if mouse_position[0] <= 426:
            game_state["position_stored"][0][0] = player_value
        elif mouse_position[0] >= 426 and mouse_position[0] <= 853:
            game_state["position_stored"][0][1] = player_value
        elif mouse_position[0] >= 853:
            game_state["position_stored"][0][2] = player_value
    elif mouse_position[1] >= 240 and mouse_position[1] <= 480:
        if mouse_position[0] <= 426:
            game_state["position_stored"][1][0] = player_value
        elif mouse_position[0] >= 426 and mouse_position[0] <= 853:
            game_state["position_stored"][1][1] = player_value
        elif mouse_position[0] >= 853:
            game_state["position_stored"][1][2] = player_value
    elif mouse_position[1] >= 480:
        if mouse_position[0] <= 426:
            game_state["position_stored"][2][0] = player_value
        elif mouse_position[0] >= 426 and mouse_position[0] <= 853:
            game_state["position_stored"][2][1] = player_value
        elif mouse_position[0] >= 853:
            game_state["position_stored"][2][2] = player_value
    switch_turn(game_state)

#switches turns
def switch_turn(game_state):
    if game_state["player"] == "player_1":
        game_state["player"] = "player_2"
        game_state["player_value"] = 2
    else:
        game_state["player"] = "player_1"
        game_state["player_value"] = 1
    print(game_state["player"])

#determines a winner 
def win_determination(game_state):
    ps = game_state["position_stored"]
    pv = game_state["player_value"]
    player = game_state["player"]
    for x in range(3):
        if ps[0][x] == ps[1][x] == ps[2][x] == pv or ps[x] == [pv,pv,pv]:
            print(player + " wins!")
            game_state["message"] = ("player " + str(pv) + " wins!")
            game_state["win"] = True
    if ps[0][0] == ps[1][1] == ps[2][2] == pv \
        or ps[0][2] == ps[1][1] == ps[2][0] == pv:
        print(player + " wins!")
        game_state["message"] = ("player " +str(pv) + " wins!")
        game_state["win"] = True
    tie_detection(game_state)
    if game_state["tie"] == True:
        print("tie!")
        game_state["message"] = ("tie!")
        game_state["tie"] = True

#determines if the match was a tie
def tie_detection(game_state):
    position_stored = game_state["position_stored"]
    game_state["tie"] = True
    for x in position_stored:
        for y in x:
            if y == 0:
                game_state["tie"] = False

#exits main loop
def exit_game(game_state):
    if game_state["win"] == True:
        time.sleep(1)    
        game_state["running"] = False
    if game_state["tie"] == True:
        time.sleep(1)    
        game_state["running"] = False

#update function
def update(game_state):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse(game_state)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state["running"] = False
    player_value = game_state["player_value"]
    game_state["message"] = ("player "+ str(player_value) + " turn")
    win_determination(game_state)
    game_state["clock"].tick(60)

#main loop and setup
def main():
    game_state = setup()
    while game_state["running"]:
        update(game_state)
        draw(game_state)

#calling main loop
main()
