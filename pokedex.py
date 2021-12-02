# This program mimics a pokedex. 
# Search for a gen 1 pokemon and see what they look like along with their stats.
# This program will take statistics from a file and convert them into a pokedex.

from tkinter import *
from PIL import Image ,ImageTk
import pdb


def main():
    # creating a GUI
    window = Tk()
    window.title('Pokedex')
    window.geometry('900x900')
    window.configure(bg='#f25f5f')
    window.resizable(False, False)
    img = ImageTk.PhotoImage(Image.open('pokedex.png'))
    banner = Label(window, image=img)
    banner.image = img
    banner.pack()
    
    # opening and reading a file
    infile = open('pokestats.txt', 'r')

    # create a label
    my_label = Label(window, text="Search for a Generation 1 Pokemon",
        font=("Simsun", 14), fg="black")
    my_label.pack(pady=20)

    # create an entry box
    poke_input = Entry(window, font =('Simsun', 20))
    poke_input.pack(pady=20)               
    
    # creating the search button and adding a binding functon
    button = Button(window, bd='4', text='Search', fg='black', bg='white', command=lambda: filescanner(pokemon_image, poke_input))
    button.pack()

    # create a list box
    my_list = Listbox(window, width=30)
    my_list.pack(pady=60)

    # create an image
    pokemon_image = Label(window)
    pokemon_image.pack()

    # selecting a line in the file
    pokemonlst = []  # create a list of pokemon 
    for line in infile:
        line = line.strip()  # stripping the new line character from the last index
        pokemon = line.split(" ")  # splitting the words in the line
        pokemonlst.append(pokemon[0])  # appending the pokemon name to pokemon list

    # add the pokemon to our list
    update(pokemonlst, my_list)

    # add events
    my_list.bind("<<ListboxSelect>>", lambda evt: fillout(evt, poke_input, my_list))  #create a binding on the listbox onclick
    poke_input.bind("<KeyRelease>", lambda evt: check(evt, poke_input, pokemonlst, my_list))  # create a binding on the enrty box
    window.bind("<Return>", lambda: filescanner(pokemon_image, poke_input))

    # run the main loop
    window.mainloop()


def update(data, my_list):
    '''Function to update the listbox.'''
    # clear the list box
    my_list.delete(0, END)

    # add pokemon to list box
    for item in data:
        my_list.insert(END, item)


def fillout(evt, poke_input, my_list):
    '''Function to update the entry box with listbox clicked.'''
    # delete whatever is in the entry box
    poke_input.delete(0, END)

    # add clicked list item to entry box
    poke_input.insert(0, my_list.get(ACTIVE))


def check(evt, poke_input, pokemonlst, my_list):
    '''Function to check entry vs listbox.'''
    # grab what was typed
    typed = poke_input.get()

    if typed == '':
        data = pokemonlst
    else:
        data = []
        for item in pokemonlst:
            if typed.lower() in item.lower():
                data.append(item)

    # update listbox with selected items
    update(data, my_list)


def filescanner(pokemon_image, poke_input):
    '''Function that runs when the button is pressed.'''
    # Open the file in the function
    file = open('pokestats.txt', 'r')

    # Take the user input from the field
    user_input = poke_input.get()
    
    # Loop over the file
    for line in file:

        # stripping the new line character from the last index
        line = line.strip()

        # splitting the words in the line
        pokemon = line.split(" ")

        # If the user input matches the pokemon name update the data
        if pokemon[0].lower() == user_input.lower():
            # creating an empty label field which will display the pokemons image
            png = pokemon[1] + user_input.lower().capitalize() + ".png"
            img = ImageTk.PhotoImage(Image.open(png).resize((100, 100)))
            print(png)
            pokemon_image.config(image=img)
            pokemon_image.image = img


if __name__ == "__main__":
    main()