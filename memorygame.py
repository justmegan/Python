#Name   : Mega Putri Aulia
#Neptun : UH92T4

from tkinter import *
from tkinter import messagebox
import random
import time

#Centering the window
def center_window(root, width=500, height=570):
    #Screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #Positioning x and y
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Mengatur ukuran dan posisi jendela
    root.geometry(f"{width}x{height}+{x}+{y}")

root = Tk()
root.title('Python Assignment - Memory Game!')

#Centering the window
center_window(root)

# Opening screen
start_frame = Frame(root)
start_frame.pack(fill="both", expand=True)

#Center frame for positioning
center_frame = Frame(start_frame)
center_frame.pack(expand=True)

# Welcome text in start_frame    
welcome_label = Label(center_frame, text="Welcome to Memory Game", font=("Helvetica", 20))
welcome_label.pack(pady=5)


# Starting the game function
def start_game():
    global start_time
    # Hiding the start frame
    start_frame.pack_forget()
    #Displaying the info label2 when the game starts
    instruction_frame.pack()
    # Showing the game and timer frames
    game_frame.pack(pady=45)
    timer_frame.pack()
    # Recording the starting time
    start_time = time.time()
    # Updating the timer
    update_timer()


# Button to start the game
ready_button = Button(center_frame, text="Are you ready?", font=("Helvetica", 14), command=start_game)
ready_button.pack(pady=5)

info_label = Label(center_frame, text="Click on the above box to start.", font=("Helvetica", 8))
info_label.pack(pady=2)


# Frame for game content, hidden initially
instruction_frame = Frame(root)
game_frame = Frame(root)
timer_frame = Frame(root)

# Displaying the instruction
instruction_label = Label(instruction_frame, text="Click on the boxes to reveal the numbers and find their pairs!", font=("Helvetica",10))
instruction_label.pack()

# Timer variables
start_time = None
game_over = False

# Creating matches 
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# Shuffling the matches
random.shuffle(matches)

# Variables for game logic
count = 0
answer_list = []
answer_dict = {}
matches_found = 0

# Function to update the timer
def update_timer():
    if not game_over:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        timer_label.config(text=f"Time: {int(minutes):02d}:{int(seconds):02d}")
        # Schedule the function to run after 1 second
        root.after(1000, update_timer)


# Displaying the time spent in timer_frame
timer_label = Label(timer_frame, text="Time: 00:00", font=("Helvetica", 12))
timer_label.pack()

# Function to check if the game is won
def win():
    global matches_found, game_over
    # Checking if all pairs have been found
    if matches_found == len(matches) // 2:
        game_over = True
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        instruction_frame.pack_forget()
        our_label.config(text=f"Yeay, you've finished in {int(minutes)} minutes and {int(seconds)} seconds!", font=("Helvetica", 14), fg="blue")


# Displaying messages like Match or Doesn't match
our_label = Label(root, text="")
our_label.pack(pady=20)

# Function for clicking buttons
def button_click(b, number):
    global count, answer_list, answer_dict, matches_found

    if b["text"] == ' ' and count < 2:
        b["text"] = matches[number]
        # Adding number to answer list
        answer_list.append(number)
        # Adding button and number to answer dictionary
        answer_dict[b] = matches[number]
        # Incrementing our counter
        count += 1

    # Starting to determine correctness
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            our_label.config(text="MATCH!", fg="green")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            matches_found += 1
            win()
        else:
            our_label.config(text="Doesn't match. Try again!", fg="red")
            count = 0
            answer_list = []
            # Pop up box
            messagebox.showinfo("Incorrect", "Incorrect!")
            # Resetting buttons
            for key in answer_dict:
                key["text"] = " "
            answer_dict = {}

# Defining the buttons for the grid in game_frame
buttons = []
for i in range(12):
    button = Button(game_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda i=i: button_click(buttons[i], i))
    buttons.append(button)

# Gridding the buttons in a 3x4 layout
buttons[0].grid(row=0, column=0)
buttons[1].grid(row=0, column=1)
buttons[2].grid(row=0, column=2)
buttons[3].grid(row=0, column=3)

buttons[4].grid(row=1, column=0)
buttons[5].grid(row=1, column=1)
buttons[6].grid(row=1, column=2)
buttons[7].grid(row=1, column=3)

buttons[8].grid(row=2, column=0)
buttons[9].grid(row=2, column=1)
buttons[10].grid(row=2, column=2)
buttons[11].grid(row=2, column=3)


root.mainloop()
