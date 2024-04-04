from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span=1, color='dark-gray'):
        super().__init__(
            master=parent,
            text=text,
            corner_radius=STYLING['corner-radius'],
            font=font,
            fg_color= COLORS[color]['fg'],
            hover_color=COLORS[color]['hover'],
            text_color=COLORS[color]['text'],
            command=func,
        )
        self.grid(column=col, row=row, sticky='nsew', padx=STYLING['gap'], pady=STYLING['gap'], columnspan=span)


class NumButton(Button):
    def __init__(self, parent, text, func, col, row, font, span, color='light-gray'):
        super().__init__(
            parent=parent,
            text=text,
            font=font,
            color=color,
            row=row,
            col=col,
            func=lambda: func(text),
            span=span
        )

class MathButton(Button):
    def __init__(self, parent, text, func, col, row, font, operator, color='orange'):
        super().__init__(
            parent=parent,
            text=text,
            font=font,
            color=color,
            row=row,
            col=col,
            func=lambda: func(operator),
        )
class ImageButton(CTkButton):
    def __init__(self, parent, func, col, row, image, text='', color='dark-gray'):
        super().__init__(
            master=parent,
            text=text,
            corner_radius=STYLING['corner-radius'],
            image=image,
            fg_color=COLORS[color]['fg'],
            hover_color=COLORS[color]['hover'],
            text_color=COLORS[color]['text'],
            command=func,
        )
        self.grid(column=col, row=row, sticky='nsew', padx=STYLING['gap'], pady=STYLING['gap'])

class MathImageButton(ImageButton):
    def __init__(self, parent, text, func, col, row,image, operator, color='orange'):
        super().__init__(
            parent=parent,
            text=text,
            color=color,
            row=row,
            col=col,
            image=image,
            func=lambda: func(operator),
        )