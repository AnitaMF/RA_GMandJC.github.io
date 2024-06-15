import random
import tkinter as tk 

class GAME: 
    def __init__(self, root):
        self.root = root
        self.root.title("GUI guess number game ")
        self.root.geometry("420x300")  

        self.program_guess = random.randrange(1, 21)
        self.guess_try = 0
        
        self.create_GUI()

    def create_GUI(self):          
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, bg="red", fg="white", font=("Arial", 12, "bold"))
        self.exit_button.pack()

        self.label = tk.Label(self.root, text="I am thinking of a number between 1 to 20", font=("Arial", 14))
        self.label.pack()

        self.label2 = tk.Label(self.root, text="What is your guess?",  font=("Arial", 12))
        self.label2.pack()

        self.userguess = tk.Entry(self.root, font=("Arial", 12))
        self.userguess.pack()

        self.guessButton = tk.Button(self.root, text="Guess", command=self.play_game, bg="blue", fg= "white",font=("Arial", 12, "bold"))
        self.guessButton.pack()

        self.restart_button = tk.Button(self.root, text="New game", command=self.restart_game, font=("Arial", 12))
        self.restart_button.pack()
        
        self.show_button = tk.Button(self.root, text="Reveal", command=self.reveal_number, font=("Arial", 12))
        self.show_button.pack()
        
        self.output_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.output_label.pack()

        self.reveal_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.reveal_label.pack()

        self.try_label = tk.Label(self.root, text=f"Number of tries: {self.guess_try}", font=("Arial", 12))
        self.try_label.pack()

    def play_game(self):
        try:
            guess = int(self.userguess.get())  
            self.userguess.delete(0, tk.END)  
            self.guess_try += 1
            self.try_label.config(text=f"Number of tries: {self.guess_try}")  # Update the try_label
            if guess == self.program_guess:
                self.output_label.config(text=f"You are right, that is the number!")
            elif guess < self.program_guess: 
                self.output_label.config(text="The number is bigger.")
            else:
                self.output_label.config(text="The number is smaller.")
        except ValueError:
            self.output_label.config(text="Please enter a valid number.")

    def restart_game(self):
        self.program_guess = random.randrange(1, 21)  
        self.guess_try = 0
        self.userguess.delete(0, tk.END)
        self.output_label.config(text="")
        self.reveal_label.config(text="")
        self.try_label.config(text=f"Number of tries: {self.guess_try}")  

    def reveal_number(self):
        self.reveal_label.config(text=f"The number is {self.program_guess}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GAME(root)
    root.mainloop()
