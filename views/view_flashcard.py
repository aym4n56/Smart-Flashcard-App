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

        self.question_text = Text(value=variables.question_text, size=20, weight='bold')
        
        view_flashcard = Container(
            content=Column(
                controls=[
                    ElevatedButton(text='Back', on_click=lambda _: self.page.go("/pick_flashcard")),
                    Container(height=20),
                    self.question_text,
                    Container(height=20),
                    self.user_answer_input,
                    ElevatedButton(text='Next', on_click=self.next_question),
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

    def next_question(self, e):
        self.cursor.execute("SELECT question_id, question_text FROM question ORDER BY question_id ASC")            
        questions = self.cursor.fetchall()
        current_question_index = next((index for index, question in enumerate(questions) if question[1] == variables.question_text), -1)
        next_question_index = ((current_question_index + 1) % len(questions))
        variables.question_text = questions[next_question_index][1]
        self.question_text.value = variables.question_text
        print(variables.question_text)
        self.page.update()

    def view(self):
        return self.container
