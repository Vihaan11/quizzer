import json
import tkinter as tk
from tkinter import ttk
from windows import dpi_awareness


dpi_awareness(1)

no_of_opt=2

class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('650x350+590+300')
        self.minsize(600, 300)
        self.resizable(height=True, width=False)

root = RootWindow()


question = tk.StringVar()
radio_var = tk.StringVar()
session_data = {}
options = {}

class AnswerFrame(ttk.Frame):
    def __init__(self,container, index:int):
        super().__init__(container)
        self.index=index
        self.entry = ttk.Entry(self)
        self.radio = ttk.Radiobutton(self, variable=radio_var, value=f"opt{index}", command=self.entry.focus)
        self.radio.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.grid()
    def get_ans(self):
        return self.entry.get()
    def select_radio(self):
        radio_var.set(f'opt{str(self.index)}')


def add_opt(*args):
    global no_of_opt
    no_of_opt+=1
    options_operator[f'opt{no_of_opt}']=AnswerFrame(answers_frame,no_of_opt)

def finalize(*args):
    my_options = list(options_operator.keys())
    for num,current_option_index in enumerate(my_options):
        if options_operator[current_option_index].get_ans().strip() != '':
            if current_option_index == radio_var.get():
                options['correct'] = options_operator[current_option_index].get_ans()
            else:
                options[f'wrong{num}'] = options_operator[current_option_index].get_ans() # added this num logic for uniqueness of keys
    session_data['ques'] = question.get()
    session_data['options'] = options
    with open('questions.json','r+') as f:
        try:
            data = list(json.load(f))
        except json.decoder.JSONDecodeError:
            data=[]
        data.append(session_data)
        f.seek(0)
        f.truncate()
        json.dump(data,f)
    root.destroy()


mainframe = ttk.Frame(root, padding=10)
mainframe.pack(fill='both', expand=True)


question_frame = ttk.Frame(mainframe, padding=(30, 10))
question_frame.grid(row=0, column=0, columnspan=2)
ttk.Label(question_frame, text='Question:', padding=(0, 0, 10, 0)).grid()
question_entry = ttk.Entry(question_frame, textvariable=question, width=60)
question_entry.grid(row=0, column=1)

answers_frame = ttk.Frame(mainframe, padding=(30, 10))
answers_frame.grid(row=1, column=0)

buttons_frame=ttk.Frame(mainframe)
buttons_frame.grid(row=1, column=1)

add_opt_button = ttk.Button(buttons_frame, text='Add Option', command=add_opt)
add_opt_button.pack()

retrieve_button = ttk.Button(buttons_frame, text='Write to file', command=finalize)
retrieve_button.pack()

options_operator = {"opt1":AnswerFrame(answers_frame,1), "opt2":AnswerFrame(answers_frame,2)}
options_operator['opt1'].select_radio()


if __name__ == "__main__": root.mainloop()