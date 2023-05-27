import tkinter as tk
import random


class Exercise:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def display_details(self):
        return f"Exercise: {self.name}\nDuration: {self.duration} minutes"


class CardioExercise(Exercise):
    def __init__(self, name, duration, intensity):
        super().__init__(name, duration)
        self.intensity = intensity

    def display_details(self):
        return f"{super().display_details()}\nIntensity: {self.intensity}"


class StrengthExercise(Exercise):
    def __init__(self, name, duration, weight):
        super().__init__(name, duration)
        self.weight = weight

    def display_details(self):
        return f"{super().display_details()}\nWeight: {self.weight} lbs"


class ExerciseProviderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exercise Provider")

        self.exercises = {
            "btn_exercise1": [Exercise("Running", 30), Exercise("Cycling", 45), Exercise("Jumping Rope", 20)],
            "btn_cardio": [CardioExercise("Jumping Jacks", 15, "Medium"), CardioExercise("Swimming", 60, "High"),
                           CardioExercise("Burpees", 10, "High")],
            "btn_strength": [StrengthExercise("Push-ups", 20, "Bodyweight"),
                             StrengthExercise("Deadlifts", 30, "Barbell"),
                             StrengthExercise("Bench Press", 25, "Dumbbells")]
        }
        self.current_exercise = {}

        self.create_widgets()

    def create_widgets(self):
        # Define pastel colors
        pastel_blue = "#AED6F1"
        pastel_green = "#A9DFBF"
        pastel_pink = "#F9E79F"

        # Set root window background color
        self.root.configure(bg=pastel_blue)

        self.lbl_title = tk.Label(self.root, text="Exercise Provider", font=("Verdana", 18, "bold"), bg=pastel_blue,
                                  fg="black")
        self.lbl_title.pack(pady=10)

        self.btn_exercise1 = tk.Button(self.root, text="Exercise 1", font=("Arial", 12), command=self.show_exercise1,
                                       bg=pastel_green, fg="black")
        self.btn_exercise1.pack(pady=5)

        self.btn_cardio = tk.Button(self.root, text="Cardio Exercise", font=("Arial", 12),
                                    command=self.show_cardio_exercise, bg=pastel_pink, fg="black")
        self.btn_cardio.pack(pady=5)

        self.btn_strength = tk.Button(self.root, text="Strength Exercise", font=("Arial", 12),
                                      command=self.show_strength_exercise, bg=pastel_green, fg="black")
        self.btn_strength.pack(pady=5)

        self.lbl_details = tk.Label(self.root, text="", font=("Verdana", 12), bg=pastel_blue, fg="black")
        self.lbl_details.pack(pady=10)

    def show_exercise1(self):
        exercise_list = self.exercises["btn_exercise1"]
        exercise = self.get_next_exercise("btn_exercise1", exercise_list)
        self.lbl_details.config(text=exercise.display_details())

    def show_cardio_exercise(self):
        exercise_list = self.exercises["btn_cardio"]
        exercise = self.get_next_exercise("btn_cardio", exercise_list)
        self.lbl_details.config(text=exercise.display_details())

    def show_strength_exercise(self):
        exercise_list = self.exercises["btn_strength"]
        exercise = self.get_next_exercise("btn_strength", exercise_list)
        self.lbl_details.config(text=exercise.display_details())

    def get_next_exercise(self, button_name, exercise_list):
        if button_name not in self.current_exercise:
            self.current_exercise[button_name] = -1

        index = self.current_exercise[button_name]
        if index == -1 or index == len(exercise_list) - 1:
            index = random.randint(0, len(exercise_list) - 1)
        else:
            index += 1

        self.current_exercise[button_name] = index
        exercise = exercise_list[index]

        return exercise


# Create the main window
root = tk.Tk()

# Create an instance of the ExerciseProviderApp
app = ExerciseProviderApp(root)

# Start the main event loop
root.mainloop()
