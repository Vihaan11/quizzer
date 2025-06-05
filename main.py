import json
import tkinter as tk
from tkinter import ttk
from windows import dpi_awareness

frames='None'

dpi_awareness(1)

class QuizzerWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x300+640+350')
        self.minsize(600,300)
        self.title("Quizzer")
        self.resizable(False,False)
    def reset_resizable(self):
        self.geometry('600x400+640+250')
        self.minsize(600, 400)
        self.resizable(True, True)
class StarterFrame(ttk.Frame):
    def __init__(self, container:QuizzerWindow):
        super().__init__(container, padding=15)
        self.title_label = ttk.Label(self, font=('Comic Sans MS', 25), text="Welcome to the Quizzer app", anchor='center')
        self.title_label.pack(fill="both", expand=True)
        self.proceed_button = ttk.Button(self, text='Proceed ->', command=proceed_button)
        self.proceed_button.pack(fill='both', expand=True, padx=30, pady=50)
class EndFrame(ttk.Frame):
    def __init__(self, container:QuizzerWindow):
        super().__init__(container, padding=15)
        self.title_label = ttk.Label(self, font=('Comic Sans MS', 25), text="The quiz has ended", anchor='center')
        self.score_label = ttk.Label(self, font=('Comic Sans MS', 25), textvariable=score, anchor='center')
        self.end_button = ttk.Button(self, text='End', command=proceed_button)
        self.title_label.pack(fill="both", expand=True)
        self.score_label.pack(fill="both", expand=True)
        self.end_button.pack(fill="both", expand=True)
class QuesFrame(ttk.Frame):
    def __init__(self, container, ques:str, options:dict):
        super().__init__(container)
        self.question = ttk.Label(self, font=('Comic Sans MS', 25), text=ques, anchor='center')
        self.error_label = ttk.Label(self, font=('Comic Sans MS', 10), textvariable=error_var, anchor='center', foreground='#cccc00')
        self.question.pack(fill="both", expand=True)
        self.options_frame = ttk.Frame(self)
        self.options_frame.pack(fill='both',expand=True)
        self.error_label.pack(fill="both")
        self.options_frame.rowconfigure(0, weight=1)
        for i, option in enumerate(list(options.values())):
            self.options_frame.columnconfigure(i, weight=1)
            if options['correct'] == option:
                ttk.Button(self.options_frame, text=option, command=proceed_button).grid(row=0, column=i, sticky='nsew')
            else:
                ttk.Button(self.options_frame, text=option, command=wrong_ans).grid(row=0, column=i, sticky='nsew')


# [{'ques':'#the ques', 'options':{'correct':'# correct opt', 'wrong1':'# wrong opt' , 'wrong2':....}}, ....]
def proceed_button(*args):
    root.reset_resizable()
    global frames
    global score
    if isinstance(frames, str):
        root.reset_resizable()
        with open('questions.json', 'r+') as f:
            data = list(json.loads(str(f.read())))
            f.seek(0)
            frames = []
            for item in data:
                frames.append(QuesFrame(root, item['ques'], item['options']))
            frames.append(EndFrame(root))
            frames = iter(frames)
        next(frames).grid(row=0, column=0, sticky='nsew')

    else:
        try:
            next(frames).grid(row=0, column=0, sticky='nsew')
            score.set(int(score.get()) + 10)
        except StopIteration:root.destroy()
def wrong_ans(*args):
    error_var.set("Wrong Answer!")
    def proceed(*args):
        try:
            next(frames).grid(row=0, column=0, sticky='nsew')
            root.after(250, lambda:error_var.set(''))
            print('nxtfr')
        except StopIteration:
            root.destroy()
    root.after(500,proceed)



root = QuizzerWindow()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

error_var = tk.StringVar()
score=tk.IntVar()
score.set(0)

starter_frame = StarterFrame(root)
starter_frame.grid(row=0, column=0, sticky='nsew')

if __name__ == '__main__':
    root.mainloop()