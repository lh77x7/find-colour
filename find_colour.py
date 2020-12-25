import time
import random
from tkinter import Tk, Canvas, HIDDEN, NORMAL

def next_shape():
    global shape
    global previous_color
    global current_color

    previous_color = current_color

    c.delete(shape)
    if len(shapes) > 0:
        shape = shapes.pop()
        c.itemconfigure(shape, state=NORMAL)
        current_color = c.itemcget(shape, 'fill')
        root.after(1000, next_shape)
    else:
        c.unbind('q')
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text(200, 200, text='Winner: Player 1')
        elif player2_score > player1_score:
            c.create_text(200, 200, text='Winner: Player 2')
        else:
            c.create_text(200, 200, text='Draw')
        c.pack()

def find_colour(event):
    global shape
    global player1_score
    global player2_score
    valid = False

    c.delete(shape)

    if previous_color == current_color:
        valid = True

    if valid:
        if event.char == 'q':
            player1_score = player1_score + 1
        else:
            player2_score = player2_score + 1
        shape = c.create_text(200, 200, text='FOUND IT! Your score 1 point!')
    else:
        if event.char == 'q':
            player1_score = player1_score - 1
        else:
            player2_score = player2_score - 1
        shape = c.create_text(200, 200, text='WRONG! You lost 1 point!')
    c.pack()
    root.update_idletasks()
    time.sleep(1)


root = Tk()
root.title('Find colour')
c = Canvas(root, width=400, height=400)

shapes = []

#creating circles
circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='yellow', fill='yellow', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='violet', fill='violet', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='purple', fill='purple', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='gold', fill='gold', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='darkcyan', fill='darkcyan', state=HIDDEN)
shapes.append(circle)

#creating rectangles
rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='yellow', fill='yellow', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='violet', fill='violet', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='purple', fill='purple', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='gold', fill='gold', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='darkcyan', fill='darkcyan', state=HIDDEN)
shapes.append(rectangle)

#creating squares
square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='yellow', fill='yellow', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='violet', fill='violet', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='purple', fill='purple', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='gold', fill='gold', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='darkcyan', fill='darkcyan', state=HIDDEN)
c.pack()

random.shuffle(shapes)

shape = None

previous_color = ''
current_color = ''
player1_score = 0
player2_score = 0

root.after(3000, next_shape)
c.bind('q', find_colour)
c.bind('p', find_colour)
c.focus_set()

root.mainloop()
