### Todo:
# Change own hand when we're running out of cards at the end of the game

import random
from re import L
from sys import float_repr_style, exit

class hanabi():
    def __init__(self, num_players):
        # Define basic variables
        #self.num_players = int(input('How many players? '))
        self.info_num = 7
        self.lives_num = 3
        self.turn_count = 0
        self.end_game_count = 500
        self.player_turn = 0
        self.num_players = num_players
        self.playing_with_multi = True

        ## Deal Decks ##
        print('Dealing...')
        
        # Main deck
        self.colours = ['Red', 'Green', 'Blue', 'White', 'Yellow', 'Multi']
        self.numbers = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        self.deck = [[c, n] for c in self.colours for n in self.numbers]

        # Empty Discard and Played decks
        self.discard_decks = {c: [] for c in self.colours}
        self.played_decks = {c: 0 for c in self.colours}

        # Players hands
        self.players_hands = []
        for self.player_turn in range(self.num_players):
            self.players_hands.append([])
            for j in range(5):
                self.deal_card()
        self.player_turn = 0

        return 
        # Start the game
        #self.take_turn()

    ## Main Turn based Progression: ##
    def take_turn(self):
        if self.turn_count >= self.end_game_count:
                print('Gameover, final score:', self.played_decks)
                return
        else:
            print(f'Pass to Player {self.player_turn + 1} then press enter.')
            input()
            for i in range(80):
                print('')
            #print('Your hand:', self.players_hands[self.player_turn])
            print(f'Turn #{self.turn_count}     Player {self.player_turn+1}\'s turn.')
            print(f'Info left: {self.info_num}      Lives left: {self.lives_num}')
            print(f'Played cards: {self.played_decks}')
            print(f'Discarded cards: {self.discard_decks}\n')
            
            shown_hands = list(enumerate(self.players_hands))
            del shown_hands[self.player_turn]
            for i in shown_hands:
                print('Player ', i[0]+1,'s hand is: ', i[1])
            print('')


            if self.info_num == 0:
                choice = input('Play (0), or Discard (1)? You have no Info left. ')
            else:
                choice = int(input('Play (0), Discard (1), or Give Info (2)? '))
                display_text = ['\nChosen to Play...', '\nChosen to Discard...', '\nChosen to Give Info...']
                action = [self.play, self.discard. self.info]
                print(display_text[choice])
                action[choice]()
  
        self.turn_count =+ 1
        self.player_turn = (self.player_turn + 1)%self.num_players 
        print('\n\nEnd of turn. Please press enter.')
        input()
        print('\n'*80)
        self.take_turn()
        return

    def play(self):
        chosen_card = self.choose_card()
        win = FALSE
        if self.played_decks[chosen_card[0]]==(chosen_card[1]-1):
            print('Card: ', chosen_card, 'played successfully!')
            played = TRUE
            if self.win():
                win = TRUE
                print('Congratulations you have won! Turn number: ', self.turn_count)
                self.end_game_count = self.turn_count
            else:
                self.played_decks[chosen_card[0]] = chosen_card[1]
                self.players_hands[self.player_turn].remove(chosen_card)
                self.deal_card()
                print('New played piles: ', self.played_decks)
                #print('Your new hand: ', self.players_hands[self.player_turn])
        else:
            self.lives_num -=  1
            print('Card: ', chosen_card, 'failed to play!')
            played = FALSE
            if self.lives_num == 0:
                self.end_game_count = self.turn_count
            else:
                print('Lives remaining:', self.lives_num)
        return  (win, played)

    def discard(self):
        chosen_card = self.choose_card()
        self.discard_decks[chosen_card[0]].append(chosen_card[1])
        self.players_hands[self.player_turn].remove(chosen_card)
        self.deal_card()
        self.info_num += 1
        print('New Info left: ', self.info_num)
        print('New discard piles: ', self.discard_decks)
        #print('Your new hand: ', self.players_hands[self.player_turn])
        return

    def info(self):
        chosen_player = int(input('Choose a player: '))-1
        print('Reminder of Player ', chosen_player +1,'s hand:', self.players_hands[chosen_player])
        colour_number = int(input('Give Colour (0) or Number (1) info: '))
        if colour_number == 0:
            chosen_colour = input('Type the colour you want to reveal and press enter: ')
            reveal = []
            for i in range(len(self.players_hands[chosen_player])):
                if self.players_hands[chosen_player][i][0] in [chosen_colour, 'multi'] :
                    reveal.append(i+1)
            #Or new code
            #reveal = [i+1 if self.players_hands[chosen_player][i][0] in [chosen_colour, 'multi'] for i in range(len(self.players_hands[chosen_player]))]
            print(f'Cards: {reveal} are {chosen_colour}')
        if colour_number == 1:
            chosen_number = int(input('Type the number you want to reveal and press enter: '))
            reveal = []
            for i in range(len(self.players_hands[chosen_player])):
                if self.players_hands[chosen_player][i][1] == chosen_number:
                    reveal.append(i+1)
            #Or new code
            #reveal = [i+1 if self.players_hands[chosen_player][i][0] == chosen_number for i in range(len(self.players_hands[chosen_player]))]
            print(f'Tell Player {chosen_player + 1} that Cards: {reveal} are {chosen_number}')
        self.info_num -= 1
        return

    def win(self):
        # Checks if there's a 5 on top of all of the played decks
        return all([i != 5 for i in self.played_decks.items()])

    def choose_card(self):
        return self.players_hands[self.player_turn][int(input('Choose card from your hand: '))-1]

    def deal_card(self):
        # pop(index) method removes a random card from the deck and stores it in dealt_card
        dealt_card = self.deck.pop(random.randrange(len(self.deck)))
        self.players_hands[self.player_turn].append(dealt_card)
        return

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

class gui(tk.Tk, hanabi):
    def __init__(self):
        #super().__init__()
        self.colours = ['Red', 'Green', 'Blue', 'White', 'Yellow', 'Multi']
        self.pure_colours = ['Red', 'Green', 'Blue', 'White', 'Yellow']
        self.spelled_numbers = ['One', 'Two', 'Three', 'Four', 'Five']

        self.menu = tk.Tk()
        self.menu.title('Hanabi')
        self.menu.protocol("WM_DELETE_WINDOW", self.menu.destroy)

        # Set up temporary window to get the number of players
        self.menu.geometry('300x150')
        self.menu.label = tk.Label(self.menu, text='Select how many players and press "Continue"?')
        self.menu.label.pack()

        # Scale to set player number
        self.scalevar = tk.StringVar()
        self.menu.scale= tk.Scale(self.menu, from_=2, to=5, orient=tk.HORIZONTAL, variable=self.scalevar)
        self.menu.scale.pack()

        # Button to set player number to the scale and continue
        cont = tk.IntVar()
        self.menu.button = tk.Button(self.menu, text='Continue', command=lambda: cont.set(1))
        self.menu.button.pack()
        self.menu.button.wait_variable(cont)
        self.deal()

        self.menu.mainloop()

    def deal(self):
        self.Hanabi = hanabi(int(self.scalevar.get()))
        self.menu.withdraw()

        # Open a window (inc. dealing a hand) for each player
        self.PlayerWindows = [self.open_player_window(i) for i in range(self.Hanabi.num_players)]

    def colour_label(self, frame, c, d):
                if c == 'Multi':
                    return tk.Label(frame, text=f' {c}:    {d} ', borderwidth=2, relief="groove", width=15, height=5)
                elif c in ['Red', 'Green', 'Blue']:
                    fg_colour = 'white'
                else:
                    fg_colour = 'black'
                return tk.Label(frame, text=f' {c}:    {d} ', bg=c.lower(), fg=fg_colour, borderwidth=2, relief="groove", width=15, height=5)

    def colour_piles(self, frame, play_or_discard):
        labels_dict = {}
        if play_or_discard == 'play':
            decks = self.Hanabi.played_decks.items()
        else:
            decks = self.Hanabi.discard_decks.items()
        for c, d in decks:
            labels_dict[c] = self.colour_label(frame, c, d)
            if c == ['Red']:
                labels_dict[c].pack(side = LEFT, pady=(0, 5) ,padx=(5, 0))
            else:
                labels_dict[c].pack(side = LEFT, pady=(0, 5))
        return labels_dict

    def open_player_window(self, player_num):
        # Create window for this player
        window = tk.Toplevel(self.menu)
        window.protocol("WM_DELETE_WINDOW", exit)
        window.title('Player ' + str(player_num+1) + "'s Window")
        window.player_num = player_num       
        window.geometry('1500x1000')

        # Set up log
        window.log = tk.scrolledtext.ScrolledText(window, width = 50, height = 50)# text = 'You may add notes here...')
        window.log.configure(state='disabled')
        window.log.pack(side=RIGHT)

        # Set up frame for own hand
        window.own_hand_frame = tk.Frame(window, borderwidth=2, relief="groove")
        window.own_hand_frame.pack(side=TOP)
        window.label = self.packed_label(window.own_hand_frame, TOP, text = 'Your Own Hand')
        for i in range(5):
            cardnum = str(i+1)
            window.cardlabel = self.packed_label(window.own_hand_frame, LEFT, bg = 'White', relief = "groove", borderwidth = 2, text = 'Card #' + cardnum, width=10, height=5)

        ## DISPLAY OTHER PLAYERS HANDS ##
        # Set up frame for the hands
        window.playershandsframe =ttk.Frame(window)#, borderwidth=2, relief="groove")
        window.playershandsframe.pack(side=TOP)
        # Set up frame for each hand
        window.playershandsframes = []
        k = 1
        for i in range(self.Hanabi.num_players-1):
            if k == player_num+1:
                k += 1
            window.frame = tk.Frame(window.playershandsframe, borderwidth=2, relief="groove")
            window.frame.pack(side=LEFT)
            name = 'Player ' + str(k) + "'s Hand"
            window.label = self.packed_label(window.frame, TOP, text = name)
            window.playershandsframes.append([k, window.frame])
            k += 1

        # Populate each hand
        other_players_hands = self.Hanabi.players_hands[:]
        del other_players_hands[player_num]
        for handnum in range(len(other_players_hands)):
            for cardnum in range(5):
                colour = str(other_players_hands[handnum][cardnum][0])
                number = str(other_players_hands[handnum][cardnum][1])
                if colour == 'Blue' or colour == 'Red' or colour == 'Green':
                    window.cardlabel = self.packed_label(window.playershandsframes[handnum][1], LEFT, fg = 'White', bg = colour, relief = "groove", borderwidth = 2, text = colour + ' ' + number, width=10, height=5)
                if colour == 'Yellow' or colour == 'White':
                    window.cardlabel = self.packed_label(window.playershandsframes[handnum][1], LEFT, bg = colour, relief = "groove", borderwidth = 2, text = colour + ' ' + number, width=10, height=5)
                if colour == 'Multi':                    
                    window.cardlabel = self.packed_label(window.playershandsframes[handnum][1], LEFT, relief = "groove", borderwidth = 2, text = colour + ' ' + number, width=10, height=5)
        
        # Display discard and play piles:
        window.discard_frame = tk.Frame(window, borderwidth=2, relief="groove")
        window.discard_frame.pack(side=TOP, pady=(10, 0))
        window.discardpileslabel = self.packed_label(window.discard_frame, TOP, text='Discard Piles')
        window.discardpileslabels = self.colour_piles(window.discard_frame, 'discard')

        window.play_frame = tk.Frame(window, borderwidth=2, relief="groove")
        window.play_frame.pack(side=TOP, pady=(10, 0))
        window.playpileslabel = self.packed_label(window.play_frame, TOP, text='Play Piles')
        window.playpileslabels = self.colour_piles(window.play_frame, 'play')
        
        window.actionsframe = ttk.Frame(window)#, borderwidth=2, relief='groove')
        window.actionsframe.pack(side=TOP, pady=(10, 0))

        if window.player_num == 0:
            window.actionslabel = self.packed_label(window.actionsframe, TOP, text='Choose your Action:')
            window.playaction = tk.Button(window.actionsframe, text='\n Play a Card \n', width=20, command = lambda: self.guiplay(window, player_num))
            window.playaction.pack(side=LEFT, padx=(5, 0), pady=(0, 5))
            window.discardaction = tk.Button(window.actionsframe, text='\nDiscard a Card\n', width=20, command = lambda: self.guidiscard(window, player_num))
            window.discardaction.pack(side=LEFT, pady=(0, 5))
            if self.Hanabi.info_num != 0:
                window.infoaction = tk.Button(window.actionsframe, text='\nGive Information\n', width=20, command = lambda: self.guiinfo(window, player_num))
                #window.infoaction['command'] = self.guigiveinfo(player_num)
                window.infoaction.pack(side=LEFT, pady=(0, 5))
            else:
                window.infoaction = self.packed_label(window.actionsframe, LEFT, pady=(0,5), text = "\nNo Pieces of Information Remaining\n You must Play or Discard \n", width=20)
        else:
            window.waitmessage = self.packed_label(window.actionsframe, TOP, pady=(0,10), text='\n\n Not your turn - talk to the others! :) \n\n', width =100, relief = 'groove')

        # Display Info, lives and deck
        window.deck_label = self.packed_label(window, BOTTOM, pady=10, text = 'Cards Remaining in Deck: \n \n' + str(len(self.Hanabi.deck)), bg = 'White', relief = "groove", borderwidth = 2, width=30, height=5)
        window.infolivesframe = tk.Frame(window, borderwidth=2, relief="groove")
        window.infolivesframe.pack(side=BOTTOM)
        window.info = self.packed_label(window.infolivesframe, LEFT, padx=30, text = 'Pieces of Information Remaining: ' + str(self.Hanabi.info_num+1) + '\n')
        window.info.pack(side= LEFT, padx = 30)        
        window.lives = self.packed_label(window.infolivesframe, LEFT, padx=30, pady=10, text = 'Lives Remaining: ' + str(self.Hanabi.lives_num+1)+ '\n')

        # Give space for notes
        window.textbox = tk.scrolledtext.ScrolledText(window, width = 40, height = 5)# text = 'You may add notes here...')
        window.textbox.pack(side=BOTTOM, pady = 10)

        return window

    def guidiscard(self, window, player_num):
        # Remove the action buttons
        for widget in window.actionsframe.winfo_children():
            widget.destroy()

        # Choose the card, returns and integer between 0 and 4
        colour, number, place_in_hand = self.choose_card(window, player_num)

        # Update variables
        self.Hanabi.discard_decks[colour].append(number)
        if self.Hanabi.info_num != 8:
            self.Hanabi.info_num+=1

        window.message = self.packed_label(window.actionsframe, TOP, pady=(0,10), text='\n\n You Discarded a ' + colour + ' ' + str(number) + '... \n\n Press "End your Turn" to Update the Display \n\n', width =100, relief = 'groove')
        
        # Update log
        for pwindow in self.PlayerWindows:
            pwindow.log.configure(state='normal')
            pwindow.log.insert(tk.INSERT, 'Turn ' + str(self.Hanabi.turn_count+1) + ': \n Player ' + str(player_num) + ' Discarded a ' + colour + ' ' + str(number)+'.\n\n')
            pwindow.log.configure(state='disabled')
        
        self.redeal_card(place_in_hand, player_num)


        window.end_turn = tk.Button(window.actionsframe, text='\n End your Turn \n', width=20, command = lambda: self.refresh_display(self.PlayerWindows, player_num))
        window.end_turn.pack(side=TOP, pady = 10)

        return

    def setvar(self,value,cont):
                cont.set(1)
                self.v = value
                print(self.v) #remove this when done
                return 
    
    def guiinfo(self, window, player_num):
        # Remove the action buttons
        for widget in window.actionsframe.winfo_children():
            widget.destroy()
        
        # Choose player to give info to
        if self.Hanabi.num_players != 1:
            window.label = self.packed_label(window.actionsframe, TOP, text = 'Please Choose which Player to Give Information to')
            cont = tk.IntVar()
            window.buttonsframe =tk.Frame(window.actionsframe)
            window.buttonsframe.pack(side=TOP)
            for i in range(self.Hanabi.num_players):
                if i != player_num:
                    window.button = tk.Button(window.buttonsframe, text='Player ' + str(i+1), command=lambda i=i: self.setvar(i, cont), width = 15)
                    window.button.pack(side=LEFT)
                    
            window.wait_variable(cont)
            playerinfo = int(self.v)
            for widget in window.actionsframe.winfo_children():
                widget.destroy()
        
        # Choose Colour or Number
        window.label = tk.Label(window.actionsframe, text = 'Please Choose which Type of Information to Give')
        window.label.pack(side=TOP)
        cont = tk.IntVar()
        window.buttonsframe = tk.Frame(window.actionsframe)
        window.buttonsframe.pack(side=TOP)
        window.button = tk.Button(window.buttonsframe, text='Colour', command=lambda: self.setvar('colour', cont), width=30)
        window.button.pack(side=LEFT)
        window.button = tk.Button(window.buttonsframe, text='Number', command=lambda: self.setvar('number', cont), width=30)
        window.button.pack(side=LEFT)
        window.wait_variable(cont)
        for widget in window.actionsframe.winfo_children():
            widget.destroy()
        colourornumber = str(self.v)

        # Choose which colour or number       
        if colourornumber == 'colour':
            window.label = self.packed_label(window.actionsframe, TOP, text = 'Please Choose a Colour to Give Information On')
            window.buttonsframe = tk.Frame(window.actionsframe)
            window.buttonsframe.pack(side=TOP)
            for c in self.pure_colours:
                window.button = tk.Button(window.buttonsframe, text=f'{c}(s)', command=lambda c=c: self.setvar(c, cont), width = 15)
                window.button.pack(side=LEFT)
        else:
            window.label = self.packed_label(window.actionsframe, TOP, text = 'Please Choose a Number to Give Information On')
            window.buttonsframe = tk.Frame(window.actionsframe)
            window.buttonsframe.pack(side=TOP)
            for i, spelled_num in enumerate(self.spelled_numbers):
                window.button = tk.Button(window.buttonsframe, text=f'{spelled_num}(s)', command=lambda i=i: self.setvar(i+1, cont), width = 15)
                window.button.pack(side=LEFT)
        
        # Wait for the players choice and then log it
        window.wait_variable(cont)
        if colourornumber == 'colour':
            info = str(self.v)
        else:
            info = int(self.v)
        
        # Give the information to every player
        message = f'Player {str(player_num+1)} tells you that your Cards {str(self.findcards(info,playerinfo))} are {str(info)}'
        for pwindow in self.PlayerWindows:
            for widget in pwindow.actionsframe.winfo_children():
                widget.destroy()
            pwindow.label = self.packed_label(pwindow.actionsframe, TOP, text = message)

            # Update log whilst we're here        
            pwindow.log.configure(state='normal')
            pwindow.log.insert(tk.INSERT, f"Turn {str(self.Hanabi.turn_count+1)}:\n Player {str(player_num+1)} told Player {str(playerinfo+1)} where his {str(info)}'s were.\n\n")
            pwindow.log.configure(state='disabled')
        # Remove the information from the player who gave the information
        for widget in window.actionsframe.winfo_children():
            widget.destroy()

        # Use up a piece pf information
        self.Hanabi.info_num+=-1

        # Warn the player not to end turn until the info has been seen
        window.message = self.packed_label(window.actionsframe, TOP, pady=(0,10), text='\n\n Information Given! \n\n Players must Look at their Table Before you End your Turn... \n\n Then Press "End your Turn" to Update the Display \n\n', width =100, relief = 'groove')
        
        # End turn button
        window.end_turn = tk.Button(window.actionsframe, text='\n End your Turn \n', width=20, command = lambda: self.refresh_display(self.PlayerWindows, player_num))
        window.end_turn.pack(side=TOP, pady = 10)
        return
    
    def findcards(self, info, hand):
        if type(info) is str and self.Hanabi.playing_with_multi:
            return [i+1 for i, x in enumerate(self.Hanabi.players_hands[hand]) if info in x or 'Multi' in x]
        else:
            return [i+1 for i, x in enumerate(self.Hanabi.players_hands[hand]) if info in x]

    def choose_card(self, window, player_num):
        # Tell player to choose a card
        window.label = tk.Label(window.actionsframe, text = 'Please Choose a Card')
        window.label.pack(side=TOP)

        # Scale to choose card
        window.scalevar = tk.StringVar()
        window.scale= tk.Scale(window.actionsframe, from_=1, to=5, orient=tk.HORIZONTAL, variable=window.scalevar)
        window.scale.pack()

        # Button to confirm
        cont = tk.IntVar()
        window.button = tk.Button(window.actionsframe, text='Confirm', command=lambda: cont.set(1))
        window.button.pack()
        window.button.wait_variable(cont)

        chosen_number = int(window.scalevar.get())-1
        colour, number = self.Hanabi.players_hands[player_num][chosen_number]

        window.label.destroy()
        window.scale.destroy()
        window.button.destroy()

        return colour, number, chosen_number
        
    def guiplay(self, window, player_num):
        # Remove the action buttons
        for widget in window.actionsframe.winfo_children():
            widget.destroy()

        # Choose the card, returns and integer between 0 and 4
        colour, number, place_in_hand = self.choose_card(window, player_num)

        if number == self.Hanabi.played_decks[colour]+1:
            self.Hanabi.played_decks[colour]+=1
            if all(value == 5 for value in self.Hanabi.played_decks.values()):
                self.guiwin()
            else:
                window.message = self.packed_label(window.actionsframe, TOP, pady=(0,10), text=f'\n\n A {colour} {number} successfully played! :) \n\n Press "End your turn" to update the display \n\n', width =100, relief = 'groove')
                if number == 5:
                    self.Hanabi.info_num+=1
                # Update log
                for pwindow in self.PlayerWindows:
                    pwindow.log.configure(state='normal')
                    pwindow.log.insert(tk.INSERT, f'Turn {self.Hanabi.turn_count+1}: \n Player {player_num} successfully played a {colour} {number}.\n\n')
                    pwindow.log.configure(state='disabled')

        else:         
            self.Hanabi.lives_num+=-1
            if self.Hanabi.lives_num == 0:
                self.guilose()
            else:
                window.message = self.packed_label(window.actionsframe, TOP, pady=(0,10), text=f'\n\n Failed to Play a {colour} {str(number)}... :( \n\n Press "End your turn" to update the display \n\n', width =100, relief = 'groove')
                self.Hanabi.discard_decks[colour].append(number)
                # Update log
                for pwindow in self.PlayerWindows:
                    pwindow.log.configure(state='normal')
                    pwindow.log.insert(tk.INSERT, f'Turn {self.Hanabi.turn_count+1}: \n Player {player_num} failed to play a {colour}  {number}.\n\n')
                    pwindow.log.configure(state='disabled')
        
        self.redeal_card(place_in_hand, player_num)

        window.end_turn = tk.Button(window.actionsframe, text='\n End your Turn \n', width=20, command = lambda: self.refresh_display(self.PlayerWindows, player_num))
        window.end_turn.pack(side=TOP, pady = 10)

        return
    
    def redeal_card(self, card, hand_num):
        # pop(index) method removes a random card from the deck and stores it in dealt_card
        del self.Hanabi.players_hands[hand_num][card]
        dealt_card = self.Hanabi.deck.pop(random.randrange(len(self.Hanabi.deck)))
        self.Hanabi.players_hands[hand_num].append(dealt_card)
        return
    
    def refresh_display(self, windows_reset, last_player):
        next_player = (last_player+1) % self.Hanabi.num_players
        self.Hanabi.turn_count+=1
        for window in windows_reset:
                    # Re-size window
            #window.geometry('1500x500')

            # Set up frame for each other hand
            for [player_hand_num, players_hand_frame] in window.playershandsframes:
                # Clear widgets from each hands frames
                for widget in players_hand_frame.winfo_children():
                    widget.destroy()
                
                # Name this frame
                name = f"Player {player_hand_num}'s Hand"
                window.label = self.packed_label(players_hand_frame, TOP, text = name)
                
                # Re-deal the hands
                handnum = player_hand_num-1
                for cardnum in range(5):
                    colour = str(self.Hanabi.players_hands[handnum][cardnum][0])
                    number = str(self.Hanabi.players_hands[handnum][cardnum][1])

                    if colour == 'Blue' or colour == 'Red' or colour == 'Green':
                        window.cardlabel = self.packed_label(players_hand_frame, LEFT, fg = 'White', bg = colour, relief = "groove", borderwidth = 2, text = colour + ' ' + number, width=10, height=5)
                    if colour == 'Yellow' or colour == 'White':
                        window.cardlabel = self.packed_label(players_hand_frame, LEFT, bg = colour, relief = "groove", borderwidth = 2, text = colour + ' ' + number, width=10, height=5)
                    if colour == 'Multi':                    
                        window.cardlabel = self.packed_label(players_hand_frame, LEFT, relief = "groove", borderwidth = 2, text = colour + ' ' + number, width=10, height=5)
            
            ## Update discard and play piles ##
            for widget in window.discard_frame.winfo_children():
                widget.destroy()
            window.discardpileslabel = self.packed_label(window.discard_frame, TOP, text='Discard Piles')
            window.discardpileslabels = self.colour_piles(window.discard_frame, 'discard')

            for widget in window.play_frame.winfo_children():
                widget.destroy()
            window.playpileslabel = tk.Label(window.play_frame, text='Play Piles')
            window.playpileslabel.pack(side=TOP)
            window.playpileslabels = self.colour_piles(window.play_frame, 'play')

            ## Display appropriate buttons / play area
            for widget in window.actionsframe.winfo_children():
                widget.destroy()

            
            # If now my turn
            if window.player_num == next_player:
                window.actionslabel = ttk.Label(window.actionsframe, text='Choose your Action:')
                window.actionslabel.pack(side=TOP)
                window.playaction = tk.Button(window.actionsframe, text='\n Play a Card \n', width=20, command = lambda: self.guiplay(windows_reset[next_player], next_player))
                window.playaction.pack(side=LEFT, padx=(5, 0), pady=(0, 5))
                window.discardaction = tk.Button(window.actionsframe, text='\nDiscard a Card\n', width=20, command = lambda: self.guidiscard(windows_reset[next_player], next_player))
                window.discardaction.pack(side=LEFT, pady=(0, 5))
                if self.Hanabi.info_num >= 0:
                    window.infoaction = tk.Button(window.actionsframe, text='\nGive Information\n', width=20, command = lambda: self.guiinfo(windows_reset[next_player], next_player))
                    window.infoaction.pack(side=LEFT, pady=(0, 5))
                else:
                    window.infoaction = tk.Label(window.actionsframe, text = "\nNo Pieces of Information Remaining\n You must Play or Discard \n", width=40)
                    window.infoaction.pack(side=LEFT, pady=(0, 5))
            else:
                window.waitmessage = tk.Label(window.actionsframe, text='\n\n Not your turn - talk to the others! :) \n\n', width =100, relief = 'groove')
                window.waitmessage.pack(side = TOP, pady=(0,10))

            # Display info, lives and deck
            window.deck_label.destroy()
            window.deck_label = self.packed_label(window, BOTTOM, pady=10, text = f'Cards Remaining in Deck: \n \n {str(len(self.Hanabi.deck))}', bg = 'White', relief = "groove", borderwidth = 2, width=30, height=5)
            window.info.destroy()
            window.info = self.packed_label(window.infolivesframe, BOTTOM, text = f'Pieces of Information Remaining: {self.Hanabi.info_num+1}')
            window.lives.destroy()      
            window.lives = self.packed_label(window.infolivesframe, LEFT, text = f'Lives Remaining: {self.Hanabi.lives_num+1}')

        return
        
    def opens_player_window(self):           
        self.button = tk.Button(self, text='Click to Start', borderwidth=2, relief="groove")
        self.button['command'] = self.start()
        self.button.pack(side=TOP)
        return

    def set_player_num(self, i):
        hanabi.num_players = i
        #self.destroy()
        return

    def packed_label(self, frame, side, padx=0, pady=0, **kwargs):
        #Wrapping function for creation of Label object that includes packing built in
        #Should turn this into a child class of Tk.Label at some point
        label = tk.Label(frame, **kwargs)
        label.pack(side=side, padx=padx, pady=pady)
        return label         


#class PackedLabel(tk.Label):
#    def __init__(se)


#hanabi()
if __name__ == "__main__":
    game = gui()
    #game.mainloop()
