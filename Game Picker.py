from graphics import *
from random import *
def draw_box(p1, p2, window):
    a=p1.getX()
    b=p1.getY()
    c=p2.getX()
    d=p2.getY()
    temp_name = Rectangle(Point(a, b), Point(c, d))
    temp_name.draw(window)
def draw_image(p1, image_name, window):
    a=p1.getX()
    b=p1.getY()
    temp_name = Image(Point(a, b),image_name)
    temp_name.draw(window)
def get_rand_genre_game(a):
    genre_list = a 
    genre = choice(genre_list)
    file = ('Games/'+ str(genre) + '.txt')
    game_options = open(file)
    games = game_options.readlines()
    game_options.close() 
    game = str(choice(games))
    test = game.split(';')
    return test
def rand_genre_game(ga):


    try:   
        win = GraphWin(ga[0], 500, 200)    
        rand_flag = True
        while rand_flag == True:
            game = get_rand_genre_game(ga)
    
            gamec = Text(Point(250, 60), 'You will be playing: ')
            gamec.draw(win)
        
            gamec.setText('You will be playing: ' + game[0])            
            yesbox = Rectangle(Point(100, 100), Point(200, 150))
            yesbox.draw(win)
            yestext = Text(Point(150, 125), 'Retry')
            yestext.draw(win)
            notext = Text(Point(350, 125), 'start\ngame')
            notext.draw(win)
            nobox = Rectangle(Point(300, 100), Point(400, 150))
            nobox.draw(win)
            query = get_click_sub(win)
            if query == 0:
                rand_flag = False
            else:
                rflag = True
                while rflag:
                    game = get_rand_genre_game(ga)
                    gamec.setText('You will be playing: ' + game[0])
                    query = get_click_sub(win)
                    if query == 0:
                        rflag = False
                        rand_flag = False
      
        a = 'os.system(' + game[1] + ')'
        win.close()
        exec(a)
        return a
    except GraphicsError:
        pass
def get_click_sub(win):
    e = False
    while e == False:
        click = win.getMouse()
        #column 1 choices
        if in_box(Point(100, 100), Point(250, 150), click) == True:
            e=True
            result = 1         
        elif in_box(Point(300, 100), Point(400, 150), click) == True:
            e=True
            result = 0
    return result
def in_box(point1, point2, click):
    xu = click.getX()
    yu = click.getY()
    if (point1.getX() <= xu <= point2.getX()) and (point1.getY() <= yu <= point2.getY()):
        res = True
    else:
        res = False
    return res
def get_click_main(win):
    e = False
    while e == False:
        click = win.getMouse()
        #column 1 choices
        if in_box(Point(50, 50), Point(250, 100), click) == True:
            e=True
            result = 0         
        elif in_box(Point(50, 110), Point(250, 160), click) == True:
            e=True
            result = 1
        elif in_box(Point(50, 170), Point(250, 220), click) == True:
            e=True
            result = 2        
        elif in_box(Point(50, 230), Point(250, 280), click) == True:
            e=True
            result = 3        
        elif in_box(Point(50, 290), Point(250, 340), click) == True:
            e=True
            result = 4
        elif in_box(Point(50, 350), Point(250, 400), click) == True:
            e=True
            result = 5                                
        elif in_box(Point(50, 410), Point(250, 460), click) == True:
            e=True
            result = 6         
        elif in_box(Point(50, 470), Point(250, 520), click) == True:
            e=True
            result = 7
        elif in_box(Point(50, 530), Point(250, 580), click) == True:
            e=True
            result = 8
        
        #column 2 choices
        elif in_box(Point(350, 50), Point(550, 100), click) == True:
            e=True
            result = 9        
        elif in_box(Point(350, 110), Point(550, 160), click) == True:
            e=True
            result = 10
        elif in_box(Point(350, 170), Point(550, 220), click) == True:
            e=True
            result = 11  
        elif in_box(Point(350, 230), Point(550, 280), click) == True:
            e=True
            result = 12         
        elif in_box(Point(350, 290), Point(550, 340), click) == True:
            e=True
            result = 13
        elif in_box(Point(350, 350), Point(550, 400), click) == True:
            e=True
            result = 14       
        elif in_box(Point(350, 410), Point(550, 460), click) == True:
            e=True
            result = 15       
        elif in_box(Point(350, 470), Point(550, 520), click) == True:
            e=True
            result = 16
        elif in_box(Point(350, 530), Point(550, 580), click) == True:
            e=True
            result = 17         
    return result
def game_picker_menu():
    try:
        win = GraphWin('Game Picker', 600, 630)
        back = draw_image(Point(425, 315), 'resources/backg1.png', win)
        #column 1 box drawings
        
        rpgbox = draw_box(Point(50, 50), Point(250, 100), win)
        rpg_cover = draw_image(Point(150, 75), 'resources/RPG.png', win)
        
        jrpgbox = draw_box(Point(50, 110), Point(250, 160), win)
        jrpg_cover = draw_image(Point(150, 135), 'resources/JRPG.png', win)
        
        action_adventure = draw_box(Point(50, 170), Point(250, 220), win)
        action_adventure_cover = draw_image(Point(150, 195), 'resources/aa.png', win)
        
        adventure = draw_box(Point(50, 230), Point(250, 280), win)
        adventure_cover = draw_image(Point(150, 255), 'resources/a.png', win)
        
        bullet_hell = draw_box(Point(50, 290), Point(250, 340), win)
        bullet_hell_cover = draw_image(Point(150, 315), 'resources/BH.png', win)
        
        classics = draw_box(Point(50, 350), Point(250, 400), win)
        classics_cover = draw_image(Point(150, 375), 'resources/class.png', win)
        
        fighter = draw_box(Point(50, 410), Point(250, 460), win)
        fighter_cover = draw_image(Point(150, 435), 'resources/fight.png', win)

        fpp = draw_box(Point(50, 470), Point(250, 520), win)
        fpp_cover = draw_image(Point(150, 495), 'resources/fpp.png', win)

        vn = draw_box(Point(50, 530), Point(250, 580), win)
        vn_cover = draw_image(Point(150, 555), 'resources/VN.png', win)


        #column 2 box drawings

        fps = draw_box(Point(350, 50), Point(550, 100), win) 
        fps_cover = draw_image(Point(450, 75), 'resources/fps.png', win)
        
        horror = draw_box(Point(350, 110), Point(550, 160), win)
        horror_cover = draw_image(Point(450, 135), 'resources/Horror.png', win)
        
        racing = draw_box(Point(350, 170), Point(550, 220), win)
        racing_cover = draw_image(Point(450, 195), 'resources/race.png', win)
        
        side_scroller = draw_box(Point(350, 230), Point(550, 280), win)
        side_scroller_cover = draw_image(Point(450, 255), 'resources/plat.png', win)
        
        stealth = draw_box(Point(350, 290), Point(550, 340), win)
        stealth_cover = draw_image(Point(450, 315), 'resources/stealth.png', win)
        
        strategy = draw_box(Point(350, 350), Point(550, 400), win)
        strategy_cover = draw_image(Point(450, 375), 'resources/strat.png', win)
        
        survival = draw_box(Point(350, 410), Point(550, 460), win)
        survival_cover = draw_image(Point(450, 435), 'resources/sur.png', win)
        
        tps = draw_box(Point(350, 470), Point(550, 520), win)
        tps_cover = draw_image(Point(450, 495), 'resources/tps.png', win)
        
        random = draw_box(Point(350, 530), Point(550, 580), win)
        random_cover = draw_image(Point(450, 555), 'resources/random.png', win)
    
        selection = get_click_main(win)
        
        if selection == 0:
            win.close()
            gs=['RPG']
            rand_genre_game(gs)
        elif selection == 1:
            win.close()
            gs=['JRPG']
            rand_genre_game(gs)
        elif selection == 2:
            win.close()
            gs=['Action Adventure']
            rand_genre_game(gs)
        elif selection == 3:
            win.close()
            gs=['Adventure']
            rand_genre_game(gs)
        elif selection == 4:
            win.close()
            gs = ['Bullet Hell']
            rand_genre_game(gs)
        elif selection == 5:
            win.close()
            gs = ['Classics']
            rand_genre_game(gs)
        elif selection == 6:
            win.close()
            gs=['Fighter']
            rand_genre_game(gs)
        elif selection == 7:
            win.close()
            gs=['FPP']
            rand_genre_game(gs)
        elif selection == 8:
            win.close()
            gs = ['VN']
            rand_genre_game(gs)
        elif selection == 9:
            win.close()
            gs = ['FPS']
            rand_genre_game(gs)
        elif selection == 10:
            win.close()
            gs = ['Horror']
            rand_genre_game(gs)
        elif selection == 11:
            win.close()
            gs = ['Racing']
            rand_genre_game(gs)
        elif selection == 12:
            win.close()
            gs = ['Side Scroller']
            rand_genre_game(gs)
        elif selection == 13:
            win.close()
            gs = ['Stealth']
            rand_genre_game(gs)
        elif selection == 14:
            win.close()
            gs = ['Strategy']
            rand_genre_game(gs)
        elif selection == 15:
            win.close()
            gs = ['Survival']
            rand_genre_game(gs)
        elif selection == 16:
            win.close()
            gs = ['TPS']
            rand_genre_game(gs)
        elif selection == 17:
            win.close()
            gs = ['Random']    
            rand_genre_game(gs)
    except GraphicsError:
        pass
game_picker_menu()