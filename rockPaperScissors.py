import random
import tkinter as tk


class RPSGame:

  def __init__(self, root):
    self.root = root
    self.root.title("Rock Paper Scissors")
    self.root.geometry("380x480")
    self.root.config(bg="#1e1e2f")
    self.root.resizable(False, False)

    self.user_score = 0
    self.comp_score = 0

    # Title Header
    tk.Label(
        root,
        text="🎮 Rock Paper Scissors",
        fg="#a29bfe",
        bg="#1e1e2f",
        font=("Arial", 16, "bold"),
    ).pack(pady=15)

    # Scoreboard Frame
    score_frame = tk.Frame(root, bg="#2d2d44")
    score_frame.pack(fill=tk.X, padx=20, pady=5, ipady=10)

    self.score_label = tk.Label(
        score_frame,
        text="Player: 0  |  Computer: 0",
        fg="white",
        bg="#2d2d44",
        font=("Arial", 12, "bold"),
    )
    self.score_label.pack()

    # Result Display Area
    result_frame = tk.Frame(root, bg="#1e1e2f")
    result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    self.choice_label = tk.Label(
        result_frame,
        text="Make your move!",
        fg="#dfe6e9",
        bg="#1e1e2f",
        font=("Arial", 12),
    )
    self.choice_label.pack(pady=10)

    self.outcome_label = tk.Label(
        result_frame,
        text="",
        fg="#55efc4",
        bg="#1e1e2f",
        font=("Arial", 16, "bold"),
    )
    self.outcome_label.pack(pady=10)

    # Buttons Frame (Rock, Paper, Scissors choices)
    btn_frame = tk.Frame(root, bg="#1e1e2f")
    btn_frame.pack(fill=tk.X, padx=20, pady=15)

    btn_style = {
        "font": ("Arial", 12, "bold"),
        "fg": "white",
        "bd": 0,
        "relief": tk.FLAT,
        "padx": 10,
        "pady": 10,
    }

    rock_btn = tk.Button(
        btn_frame,
        text="🪨 Rock",
        bg="#0984e3",
        activebackground="#74b9ff",
        command=lambda: self.play("Rock"),
        **btn_style
    )
    rock_btn.grid(row=0, column=0, padx=5, sticky="ew")

    paper_btn = tk.Button(
        btn_frame,
        text="📄 Paper",
        bg="#00b894",
        activebackground="#55efc4",
        command=lambda: self.play("Paper"),
        **btn_style
    )
    paper_btn.grid(row=0, column=1, padx=5, sticky="ew")

    scissors_btn = tk.Button(
        btn_frame,
        text="✂️ Scissors",
        bg="#d63031",
        activebackground="#ff7675",
        command=lambda: self.play("Scissors"),
        **btn_style
    )
    scissors_btn.grid(row=0, column=2, padx=5, sticky="ew")

    btn_frame.columnconfigure(0, weight=1)
    btn_frame.columnconfigure(1, weight=1)
    btn_frame.columnconfigure(2, weight=1)

    # Reset Scores Button
    reset_btn = tk.Button(
        root,
        text="🔄 Reset Scores",
        font=("Arial", 10, "bold"),
        bg="#636e72",
        fg="white",
        activebackground="#b2bec3",
        activeforeground="white",
        bd=0,
        relief=tk.FLAT,
        command=self.reset_game,
    )
    reset_btn.pack(fill=tk.X, padx=20, pady=10, ipady=6)

  def play(self, user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)

    emoji_map = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

    # Display user vs computer choices
    self.choice_label.config(
        text=(
            f"You: {emoji_map[user_choice]}  vs  PC: {emoji_map[comp_choice]}"
        )
    )

    # Determine winner logic
    if user_choice == comp_choice:
      outcome = "It's a Tie! 🤝"
      self.outcome_label.config(fg="#ffeaa7")
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Rock")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
      outcome = "You Win! 🎉"
      self.user_score += 1
      self.outcome_label.config(fg="#55efc4")
    else:
      outcome = "You Lose! 😢"
      self.comp_score += 1
      self.outcome_label.config(fg="#ff7675")

    self.outcome_label.config(text=outcome)
    self.score_label.config(
        text=f"Player: {self.user_score}  |  Computer: {self.comp_score}"
    )

  def reset_game(self):
    self.user_score = 0
    self.comp_score = 0
    self.score_label.config(text="Player: 0  |  Computer: 0")
    self.choice_label.config(text="Make your move!")
    self.outcome_label.config(text="")


if __name__ == "__main__":
  root = tk.Tk()
  app = RPSGame(root)
  root.mainloop()