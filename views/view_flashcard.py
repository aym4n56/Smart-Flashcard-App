import sqlite3
import os
from flet import *
from views import variables  # Import variables from the views folder

directory = os.path.dirname(os.path.abspath(__file__))
database_file_path = os.path.join(directory, 'flashcard.db')


class ViewFlashcard:
    def __init__(self, page: Page):
        self.page = page
        self.conn = sqlite3.connect(database_file_path)
        self.cursor = self.conn.cursor()

        BG = '#041995'
        FG = '#3450a1'

        self.user_answer_input = TextField(label='Answer', width=400)
        
        view_flashcard = Container(
            content=Column(
                controls=[
                    ElevatedButton(text='Back', on_click=lambda _: self.page.go("/pick_flashcard")),
                    Container(height=20),
                    Text(value=variables.question_text, size=20, weight='bold'),
                    Container(height=20),
                    self.user_answer_input,
                    ElevatedButton(text='Next'),
                ],
            ),
        )

        self.container = Container(
            width=400,
            height=850,
            bgcolor=FG,
            border_radius=35,
            padding=padding.only(top=50, left=20, right=20, bottom=5),
            content=view_flashcard,
        )
            

    def view(self):
        return self.container
