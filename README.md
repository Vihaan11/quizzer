# Quizzer App

A simple GUI-based quiz application built with Python and Tkinter. Users can take quizzes, and there's a separate utility to add new questions to the quiz bank.

## Features

* **Interactive Quiz Interface:** Presents questions one by one with multiple-choice answers.
* **Score Tracking:** Displays the user's score at the end of the quiz.
* **Question Management:** A separate script (`question_adder.py`) allows for easy addition of new questions and their options to a JSON file.
* **Dynamic Question Loading:** Questions are loaded from an external `questions.json` file.
* **GUI built with Tkinter:** Provides a graphical user interface for both playing the quiz and adding questions.
* **DPI Awareness:** Includes a utility for better UI display on high-DPI screens (Windows).


## Prerequisites

* Python 3.5+
* Tkinter (usually comes with standard Python installations)

## How to Run the Quiz

1.  **Ensure `questions.json` exists:** This file should contain at least one question. If not, use the `question_adder.py` script to add some.
    * Example `questions.json` structure:
        ```json
        [
            {
                "ques": "What is the capital of France?",
                "options": {
                    "correct": "Paris",
                    "wrong1": "London",
                    "wrong2": "Berlin",
                    "wrong3": "Madrid"
                }
            }
        ]
        ```
2.  **Run `main.py`:**
    ```bash
    python main.py
    ```
3.  The quiz window will appear. Click "Proceed ->" to start the quiz.
4.  Answer the questions. A "Wrong Answer!" message will briefly appear for incorrect selections.
5.  Your final score will be displayed at the end. Click "End" to close the application.

## How to Add New Questions

1.  **Run `question_adder.py`:**
    ```bash
    python question_adder.py
    ```
2.  A window will open to add a new question:
    * Enter the question in the "Question:" field.
    * Enter the answer options in the fields provided.
    * Select the radio button next to the **correct** answer.
    * Click "Add Option" to add more answer choices (default is 2, minimum 1 correct and 1 wrong is needed for the quiz to function as expected with multiple choices).
    * Click "Write to file" to save the question and its options to `questions.json`.
3.  The new question will be appended to the `questions.json` file.

## Code Overview

### `main.py`

* `QuizzerWindow`: Main application window class inheriting from `tk.Tk`.
* `StarterFrame`: The initial frame with the "Welcome" message and "Proceed" button.
* `EndFrame`: The final frame displaying "The quiz has ended" and the score.
* `QuesFrame`: Dynamically created frame for each question, displaying the question and its answer buttons.
* `proceed_button()`: Handles the logic for moving to the next question or ending the quiz. It loads questions from `questions.json` on the first call.
* `wrong_ans()`: Called when a wrong answer is selected, displays an error message briefly before moving to the next question.

### `question_adder.py`

* `RootWindow`: Main window for the question adder utility.
* `AnswerFrame`: A frame to hold an input field for an answer option and a radio button to mark it as correct.
* `add_opt()`: Adds a new `AnswerFrame` for an additional option.
* `finalize()`: Gathers the question and options data, formats it, and appends it to the `questions.json` file.

### `questions.json`

* A JSON array of objects.
* Each object represents a question and has two keys:
    * `ques`: (String) The question text.
    * `options`: (Object) Contains the answer choices.
        * `correct`: (String) The correct answer.
        * `wrong1`, `wrong2`, etc.: (String) Incorrect answer options. The keys for wrong answers must be unique (e.g., `wrong1`, `wrong2`, `anotherWrong`).

### `windows.py`

* `dpi_awareness()`: A simple function to attempt to set DPI awareness on Windows systems for clearer UI rendering. This helps prevent blurriness on high-resolution displays.
