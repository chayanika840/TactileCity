from tkinter import *
from user import *
from parking import *

from PIL import Image, ImageTk


def park1():
        occupied = Toplevel()
        occupied.title("Parking spot")
        occupied.geometry("1800x1015")
        occupied.resizable(False, False)

        img_occupied = Image.open("occupied.jpg")
        render_occupied = ImageTk.PhotoImage(img_occupied)


        img_park1 = Label(occupied, image = render_occupied)
        img_park1.place(x=0, y=0)

        occupied.pack()

        occupied.mainloop()

def park2():
        occupied = Toplevel()
        occupied.title("Parking spot")
        occupied.geometry("1800x1015")
        occupied.resizable(False, False)

        img_occupied = Image.open("vacant.jpg")
        render_occupied = ImageTk.PhotoImage(img_occupied)


        img_park1 = Label(occupied, image = render_occupied)
        img_park1.place(x=0, y=0)

        occupied.pack()

        occupied.mainloop()


def main():
    window = Tk()
    window.title("TacktileCity")
    window.geometry("1116x722")
    window.resizable(False, False)


    
    img_vacant = Image.open("vacant.jpg")
    render_vacant = ImageTk.PhotoImage(img_vacant)

    img_map = Image.open("sample_map.png")

    render = ImageTk.PhotoImage(img_map)

    # background = Label(window, image=render)
    # background.image = render
    # background.pack(fill=BOTH, expand=1)

    canvas = Canvas(window, width=1116, height=722)
    canvas.pack()
    canvas.create_image(558, 361, image=render)

   # img = Label(window, image = render)

    #img.place(x=0,y=0)
    
    
    frame_map = Frame(window)
    #frame_map['bg'] = frame_map.master['bg']

    

    # button_park1 = Button(frame_map, text = "P", command=park1, width = 100, height = 100)
    # button_park1.pack(side=RIGHT)

    #frame_map.pack()

    quit_button1 = Button(window, text = "P", command = park1, anchor = 'w',
                    width = 1, height=1, activebackground = "#33B5E5")
    quit_button_window = canvas.create_window(570, 110, anchor='nw', window=quit_button1)

    quit_button2 = Button(window, text = "P", command = park2, anchor = 'w',
                    width = 1, height=1, activebackground = "#33B5E5")
    quit_button_window = canvas.create_window(550, 410, anchor='nw', window=quit_button2)

    window.mainloop()







if __name__ == '__main__':
    main()