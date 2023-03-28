# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:50:28 2023

@author: niveditha
"""


import tkinter as tk
import pygame

def open_new_window():
    #new_window = tk.Toplevel(root)
    #new_window.title("New Window")
    #new_window.geometry("500x500")
    #tk.Label(new_window, text="Game Over").pack()
   

    # Initialize Pygame
    pygame.init()
    
    # Set up the screen
    screen_width = 550
    screen_height = 550
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # Set up colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    # Set up board parameters
    board_size = 4
    tile_size = screen_width // (board_size) # Add one to include the divider
    divider_width = tile_size // 2
    
    # Draw the board
    for row in range(board_size):
        for col in range(board_size): # Add one to include the divider
            x = col * tile_size
            y = row * tile_size 
            # Draw the tiles
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, white, (x, y, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, black, (x, y, tile_size, tile_size))
    
    # Update the screen
    pygame.display.update()
    
    # Run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Create the main window
root = tk.Tk()
root.title("SPY GRID")
root.geometry("300x200")

# Create a button to open a new window
open_button = tk.Button(root, text="Start game", command=open_new_window)
open_button.pack()

# Start the main event loop
root.mainloop()
