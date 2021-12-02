# This program mimics a pokedex. Search for a gen 1 pokemon and see what they look like along with their stats.
# Program will also let you compare 2 gen 1 pokemon.

from tkinter import *

def main():

    # creating and editing the window for the pokedex using tkinter
    window = Tk()
    frame = Frame(window)
    window.configure(bg='#f25f5f')
    frame.configure(bg='#f25f5f')
    window.title('Pokedex')
    window.configure(width=900, height=900)
    window.resizable(False, False)

    # creating a search bar
    searchbar = Entry(frame)
    searchbar.pack(side=LEFT, fill=BOTH, expand=1,)
    searchbar.focus_set()
    button = Button(frame, text='Search')
    button.pack(side=RIGHT)
    frame.pack(side=TOP)
    txt = Text(window)
    txt.pack(side=BOTTOM)
    window.mainloop()
    
    my_label = Label(window, test = "Start Typing...")






main()