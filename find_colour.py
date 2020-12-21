import time
import random
from tkinter import Tk, Canvas, HIDDEN, NORMAL

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

#creating rectangles
rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
shapes.append(rectangle)

#creating squares
square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
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
