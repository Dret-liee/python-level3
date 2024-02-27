from tkinter import *
from tkinter import messagebox
import random


win = Tk()
win.title('start program')
win.config(bg= '#B0FAA6')


# here i wrote a code that the win completely be in the center when someone run it 
screen_w = win.winfo_screenwidth()
screen_h = win.winfo_screenheight()
cx = screen_w // 2
cy = screen_h // 2
geometry_x = 500
geometry_y = 350

win.geometry(f'{geometry_x}x{geometry_y}+{cx - geometry_x //2}+{cy - geometry_y //2}')



time = 30
score = 0 
numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']

random_number = random.choice(numbers)


# ============================ Function ============================

def start():
    

    if int_var.get() == 1:
        win.destroy()
        
        win_color = Tk()
        win_color.title('color')
        win_color.config(bg= '#B09FB6')

        # here i wrote a code that the win completely be in the center when someone run it 
        screen_w = win_color.winfo_screenwidth()
        screen_h = win_color.winfo_screenheight()
        cx = screen_w // 2
        cy = screen_h // 2
        geometry_x = 500
        geometry_y = 350
        win_color.geometry(f'{geometry_x}x{geometry_y}+{cx - geometry_x //2}+{cy - geometry_y //2}')



        def start_color():
            if int_var_color.get() == 1:
                win_color.config(bg= 'green')
            
            if int_var_color.get() == 2:
                win_color.config(bg= 'red')
            
            if int_var_color.get() == 3:
                win_color.config(bg= 'blue')
            
            if int_var_color.get() == 4:
                win_color.config(bg= 'yellow')

            if int_var_color.get() == 5:
                win_color.config(bg= 'orange')


        def exit_program_color():
            result = messagebox.askquestion('Exit', 'Are you sure you want to exit?')
            if result == 'yes':
                win_color.destroy()



        # ============================ Widget win_color ============================

        # radio button section
        int_var_color = IntVar()
        int_var_color.set(0)

        options = {'green': 1, 'red': 2, 'blue': 3, 'yellow': 4, 'orange': 5}
        Y = 20
        for key,value in options.items():
            btn_radio_color = Radiobutton(win_color, text= key, value= value, variable= int_var_color, width= 5).place(x= 220, y= Y)
            Y += 50
        
        


        # button section
        btn_start = Button(win_color, text= 'Start', font= 'arial 16 bold', width= 5, command= start_color, bg= '#45C4BC')
        btn_start.place(x= 130, y= 250)

        btn_exit = Button(win_color, text= 'Exit', font= 'arial 16 bold', width= 5, command= exit_program_color, bg= '#EC3E48')
        btn_exit.place(x= 290, y= 250)




    if int_var.get() == 2:
        
        win.destroy()

        win_game = Tk()
        win_game.title('game')
        win_game.config(bg= '#FAF1B2')

        # here i wrote a code that the win completely be in the center when someone run it 
        screen_w = win_game.winfo_screenwidth()
        screen_h = win_game.winfo_screenheight()
        cx = screen_w // 2
        cy = screen_h // 2
        geometry_x = 500
        geometry_y = 350
        win_game.geometry(f'{geometry_x}x{geometry_y}+{cx - geometry_x //2}+{cy - geometry_y //2}')

        # ============================ Function ============================

        def exit_program_game():
            result = messagebox.askquestion('Exit', 'Are you sure you want to exit?')
            if result == 'yes':
                win_game.destroy()

        def start_game():
            global time
        

            if time > 0:
                btn_start.config(state= DISABLED)
                btn_num1.config(state= NORMAL)
                btn_num2.config(state= NORMAL)
                btn_num3.config(state= NORMAL)
                lbl_time1.config(text= time)
                time -= 1
                lbl_time1.after(1000, start_game)

                if time == 0:
                    result = messagebox.showinfo('your time is ended', f'you earned {score} point in 30 second \nGood luck')
                    if result == 'ok':
                        win_game.destroy()

        def btn_1():
            global score
            global random_number

            if random_number ==  '1+1-1' or random_number == '1-1+1' or random_number == '3+1-3' or random_number == '3-3+1' or random_number == '2+2-3':
                score += 1
                lbl_score.config(text= score)
                numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
                            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
                            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']
                
                random_number = random.choice(numbers)
                lbl_number.config(text= random_number)
            
            if random_number != '1+1-1' or random_number != '1-1+1' or random_number != '3+1-3' or random_number != '3-3+1' or random_number != '2+2-3':
                
                lbl_score.config(text= score)
                numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
                            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
                            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']
                
                random_number = random.choice(numbers)
                lbl_number.config(text= random_number)

        def btn_2():
            global score
            global random_number

            if random_number == '2+1-1' or random_number == '1+2-1' or random_number == '1-1+2' or random_number == '2+2-2' or random_number == '3-2+1':
                score += 1
                lbl_score.config(text= score)
                numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
                            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
                            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']
                
                random_number = random.choice(numbers)
                lbl_number.config(text= random_number)
            
            if random_number != '2+1-1' or random_number != '1+2-1' or random_number != '1-1+2' or random_number != '2+2-2' or random_number != '3-2+1':
                
                lbl_score.config(text= score)
                numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
                            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
                            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']
                
                random_number = random.choice(numbers)
                lbl_number.config(text= random_number)
            

        def btn_3():
            global score
            global random_number

            if random_number == '1+1+1' or random_number == '2-1+2' or random_number == '2+3-2' or random_number == '3-3+3' or random_number == '3-2+2':
                score += 1
                lbl_score.config(text= score)
                numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
                            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
                            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']
                
                random_number = random.choice(numbers)
                lbl_number.config(text= random_number)

            if random_number != '1+1+1' or random_number != '2-1+2' or random_number != '2+3-2' or random_number != '3-3+3' or random_number !='3-2+2':
                
                lbl_score.config(text= score)
                numbers = ['1+1+1', '2-1+2', '2+3-2', '3-3+3', '3-2+2',
                            '2+1-1', '1+2-1', '1-1+2', '2+2-2', '3-2+1',
                            '1+1-1', '1-1+1', '3+1-3', '3-3+1', '2+2-3']
                
                random_number = random.choice(numbers)
                lbl_number.config(text= random_number)

            




        # ============================ Widget win_game ============================
                
        # label section
        lbl_info_score = Label(win_game, text= 'Score:', font= 'arial 18 bold', bg= '#FAF1B2')
        lbl_info_score.place(x= 10, y= 10)

        lbl_info_time = Label(win_game, text= 'Time:', font= 'arial 18 bold', bg= '#FAF1B2' )
        lbl_info_time.place(x= 380, y= 10)

        lbl_score = Label(win_game, bg= 'black', fg= 'yellow', font= '16', text= score)
        lbl_score.place(x= 100, y= 15)
    
        lbl_time1 = Label(win_game, bg= 'black', fg= 'yellow', font= '16', text= time )
        lbl_time1.place(x= 460, y= 15)
        
        lbl_number = Label(win_game, bg= '#6E7AB3', text= random_number, font= 'Bold', width= 10)
        lbl_number.place(x= 190, y= 70)


        # button section
        btn_num1 = Button(win_game, text= 1, font= 'arial 14 bold', state= DISABLED, command= btn_1, width= 10)
        btn_num1.place(x= 180, y= 110)

        btn_num2 = Button(win_game, text= 2, font= 'arial 14 bold', state= DISABLED, command= btn_2, width= 10)
        btn_num2.place(x= 180, y= 160)

        btn_num3 = Button(win_game, text= 3, font= 'arial 14 bold', state= DISABLED, command= btn_3, width= 10)
        btn_num3.place(x= 180, y= 210)

        btn_start = Button(win_game, text= 'Start', font= 'arial 16 bold', width= 5, command= start_game, bg= '#45C4BC')
        btn_start.place(x= 130, y= 270)

        btn_exit = Button(win_game, text= 'Exit', font= 'arial 16 bold', width= 5, command= exit_program_game, bg= '#EC3E48')
        btn_exit.place(x= 290, y= 270)

        
def exit_program():
    result = messagebox.askquestion('Exit', 'Are you sure you want to exit?')
    if result == 'yes':
        win.destroy()


def help_program():
    pass


# ============================ Widget win ============================

# label section
lbl_info = Label(win, text= 'Select an option and press start', font= 'Times-New-Roman 20 bold', bg= '#B0FAA6')
lbl_info.place(x= 30, y= 30)

# button section
btn_start = Button(win, text= 'Start', font= 'arial 18 bold', width= 5, command= start, bg= '#45C4BC')
btn_start.place(x= 120, y= 210)

btn_exit = Button(win, text= 'Exit', font= 'arial 18 bold', width= 5, command= exit_program, bg= '#EC3E48')
btn_exit.place(x= 280, y= 210)

btn_help = Button(win, text= 'Help', font= 'arial 18 bold', width= 10, command= help_program, bg= '#E0CA6A')
btn_help.place(x= 165, y= 280)

# radio button section
int_var = IntVar()

options = {'color': 1, 'game': 2}

X = 150
for key,value in options.items():
    btn_radio = Radiobutton(win, text= key, value= value, variable= int_var).place(x= X, y= 100)
    X += 120





win.mainloop()