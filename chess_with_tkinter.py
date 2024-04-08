import tkinter as tk
from tkinter import ttk
import chess
import customtkinter as ctk
from PIL import Image, ImageTk

LIGHT_COLOR = "#f5f5f5"
DARK_COLOR = "#646464"

class ChessApp(ctk.CTk):
    def __init__(self, width=900, height=600, fen_string=''):
        super().__init__()
        self.__width = width
        self.__height = height
        self.__square_width = min(height, width) / 8

        self.resizable(0, 0)
        self.geometry(f"{self.__width}x{self.__height}")

        self.game_frame = ttk.Frame(self)
        self.game_frame.grid(row=0, column=0)

        self.text_frame = ttk.Frame(self)
        self.text_frame.grid(row=0, column=1)

        self.board = chess.Board()
        self.draw_board()

    def draw_board(self):
        deconstructed_fen = [
            f.split(' ') for f in 
            self.board.__str__().split('\n')
        ]
        import os
        print("Deconstructed fen is: ")
        print(deconstructed_fen)
        for i in range(8):
            for j in range(8):
                button_color = ( LIGHT_COLOR if (i+j) % 2 == 0 else DARK_COLOR )
                
                try:
                    piece = deconstructed_fen[i][j]
                except IndexError as e:
                    print(f"i: {i}, j: {j}")
                    raise e
                button_image = None

                if piece != '.':
                    color = 'b' if deconstructed_fen[i][j].islower() else 'w'

                    button_image_path = os.path.join("skins", "default", color, f"{piece.lower()}.jpg")
                    button_image = ctk.CTkImage(
                        Image.open(button_image_path), 
                        size=(32, 32)
                    )

                ctk.CTkButton(
                    self.game_frame, 
                    height=self.__square_width, 
                    width=self.__square_width,
                    bg_color=( LIGHT_COLOR if (i+j) % 2 == 0 else DARK_COLOR ),
                    fg_color=button_color,
                    hover_color=button_color,
                    text='',
                    image=button_image
                ).grid(row=i, column=j)
        pass

    def run(self):
        self.mainloop()


app = ChessApp()
app.run()