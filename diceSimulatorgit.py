import random
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Dice Roller")

# Label to display the dice roll
text_1 = Label(root, text='', font=("Times", 100))
text_1.pack()

# History label to display previous rolls
history_label = Label(root, text='Roll History:', font=("Times", 14))
history_label.pack()

# List to store roll history
roll_history = []


# Function to animate the dice roll
def animate_dice_roll():
    num_code = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    for _ in range(10):  # Number of animation frames (80 for 1 and so on)
        roll_result = f'{random.choice(num_code)}{random.choice(num_code)}'
        text_1.config(text=roll_result)
        root.update()
        root.after(100)  # Delay between frames for animation



def CLICK_HERE_TO_ROLL_THE_DICE(): # Function to roll the dice and update the display
    animate_dice_roll()
    num_code = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # ASCII code for numbers
    roll_result = f'{random.choice(num_code)}{random.choice(num_code)}'
    text_1.config(text=roll_result)


    roll_history.append(roll_result) #to check the history
    history_label.config(text=f'Roll History: {", ".join(roll_history[-5:])}')  # Display the last 5 rolls

    # Change background color randomly after each roll
    root.config(bg=random.choice(['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgray']))


# Function to reset the roll history
def reset_history():
    global roll_history
    roll_history = []
    history_label.config(text='Roll History:')


button_1 = Button(root, text="CLICK HERE TO ROLL THE DICE", command=CLICK_HERE_TO_ROLL_THE_DICE)
button_1.place(x=200, y=0)

# Reset button to clear history
reset_button = Button(root, text="Reset History", command=reset_history)
reset_button.place(x=260, y=50)

root.mainloop()
