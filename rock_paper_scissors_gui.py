import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from PIL import Image, ImageTk
import os

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock, Paper, Scissors Game")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Game state
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.user_choice = None
        self.computer_choice = None
        
        # Create GUI elements
        self.create_widgets()
        self.update_display()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text="🎮 ROCK, PAPER, SCISSORS 🎮", 
            font=('Arial', 24, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack()
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        self.score_frame.pack(pady=10, padx=20, fill='x')
        
        self.score_label = tk.Label(
            self.score_frame,
            text="🏆 SCORE: You 0 - 0 Computer",
            font=('Arial', 16, 'bold'),
            fg='#f39c12',
            bg='#34495e'
        )
        self.score_label.pack(pady=10)
        
        self.rounds_label = tk.Label(
            self.score_frame,
            text="📊 Rounds Played: 0",
            font=('Arial', 14),
            fg='#ecf0f1',
            bg='#34495e'
        )
        self.rounds_label.pack()
        
        # Game area
        game_frame = tk.Frame(self.root, bg='#2c3e50')
        game_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # User choice area
        user_frame = tk.LabelFrame(
            game_frame, 
            text="🤔 YOUR CHOICE", 
            font=('Arial', 14, 'bold'),
            fg='#3498db',
            bg='#2c3e50',
            bd=2
        )
        user_frame.pack(side='left', fill='both', expand=True, padx=10)
        
        self.user_display = tk.Label(
            user_frame,
            text="",
            font=('Arial', 60),
            bg='#2c3e50',
            fg='#3498db'
        )
        self.user_display.pack(pady=20)
        
        self.user_choice_label = tk.Label(
            user_frame,
            text="Make your choice!",
            font=('Arial', 12),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.user_choice_label.pack()
        
        # VS label
        vs_label = tk.Label(
            game_frame,
            text="VS",
            font=('Arial', 20, 'bold'),
            fg='#e74c3c',
            bg='#2c3e50'
        )
        vs_label.pack(side='left', padx=20)
        
        # Computer choice area
        computer_frame = tk.LabelFrame(
            game_frame, 
            text="🤖 COMPUTER CHOICE", 
            font=('Arial', 14, 'bold'),
            fg='#e74c3c',
            bg='#2c3e50',
            bd=2
        )
        computer_frame.pack(side='left', fill='both', expand=True, padx=10)
        
        self.computer_display = tk.Label(
            computer_frame,
            text="❓",
            font=('Arial', 60),
            bg='#2c3e50',
            fg='#e74c3c'
        )
        self.computer_display.pack(pady=20)
        
        self.computer_choice_label = tk.Label(
            computer_frame,
            text="Waiting...",
            font=('Arial', 12),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.computer_choice_label.pack()
        
        # Choice buttons
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=20)
        
        # Rock button
        self.rock_btn = tk.Button(
            button_frame,
            text="🪨 ROCK",
            font=('Arial', 14, 'bold'),
            bg='#95a5a6',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.make_choice('rock'),
            relief='raised',
            bd=3
        )
        self.rock_btn.pack(side='left', padx=5)
        
        # Paper button
        self.paper_btn = tk.Button(
            button_frame,
            text="📄 PAPER",
            font=('Arial', 14, 'bold'),
            bg='#3498db',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.make_choice('paper'),
            relief='raised',
            bd=3
        )
        self.paper_btn.pack(side='left', padx=5)
        
        # Scissors button
        self.scissors_btn = tk.Button(
            button_frame,
            text="✂️ SCISSORS",
            font=('Arial', 14, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=12,
            height=2,
            command=lambda: self.make_choice('scissors'),
            relief='raised',
            bd=3
        )
        self.scissors_btn.pack(side='left', padx=5)
        
        # Result display
        self.result_frame = tk.Frame(self.root, bg='#2c3e50')
        self.result_frame.pack(pady=10, padx=20, fill='x')
        
        self.result_label = tk.Label(
            self.result_frame,
            text="🎯 Choose your weapon!",
            font=('Arial', 16, 'bold'),
            fg='#f39c12',
            bg='#2c3e50'
        )
        self.result_label.pack()
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg='#2c3e50')
        control_frame.pack(pady=10)
        
        self.reset_btn = tk.Button(
            control_frame,
            text="🔄 RESET SCORE",
            font=('Arial', 12, 'bold'),
            bg='#f39c12',
            fg='white',
            command=self.reset_game,
            relief='raised',
            bd=2
        )
        self.reset_btn.pack(side='left', padx=10)
        
        self.quit_btn = tk.Button(
            control_frame,
            text="🚪 QUIT GAME",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            command=self.quit_game,
            relief='raised',
            bd=2
        )
        self.quit_btn.pack(side='left', padx=10)
        
        # Rules display
        rules_frame = tk.Frame(self.root, bg='#34495e', relief='sunken', bd=2)
        rules_frame.pack(pady=10, padx=20, fill='x')
        
        rules_text = "📋 RULES: Rock beats Scissors | Scissors beat Paper | Paper beats Rock"
        rules_label = tk.Label(
            rules_frame,
            text=rules_text,
            font=('Arial', 10),
            fg='#ecf0f1',
            bg='#34495e'
        )
        rules_label.pack(pady=5)
    
    def get_emoji(self, choice):
        """Get emoji for choice"""
        emoji_map = {
            'rock': '🪨',
            'paper': '📄',
            'scissors': '✂️'
        }
        return emoji_map.get(choice, '❓')
    
    def make_choice(self, choice):
        """Handle user choice"""
        self.user_choice = choice
        self.user_display.config(text=self.get_emoji(choice))
        self.user_choice_label.config(text=choice.upper())
        
        # Disable buttons during animation
        self.disable_buttons()
        
        # Start computer choice animation
        self.animate_computer_choice()
    
    def animate_computer_choice(self):
        """Animate computer choice selection"""
        choices = ['rock', 'paper', 'scissors']
        self.animation_count = 0
        self.animate_loop(choices)
    
    def animate_loop(self, choices):
        """Animation loop for computer choice"""
        if self.animation_count < 10:  # 10 animation cycles
            choice = random.choice(choices)
            self.computer_display.config(text=self.get_emoji(choice))
            self.computer_choice_label.config(text=choice.upper())
            self.animation_count += 1
            self.root.after(100, lambda: self.animate_loop(choices))
        else:
            # Final computer choice
            self.computer_choice = random.choice(choices)
            self.computer_display.config(text=self.get_emoji(self.computer_choice))
            self.computer_choice_label.config(text=self.computer_choice.upper())
            self.determine_winner()
    
    def determine_winner(self):
        """Determine and display winner"""
        if self.user_choice == self.computer_choice:
            result = "tie"
            self.result_label.config(text="🤝 IT'S A TIE!", fg='#f39c12')
        elif (self.user_choice == 'rock' and self.computer_choice == 'scissors') or \
             (self.user_choice == 'scissors' and self.computer_choice == 'paper') or \
             (self.user_choice == 'paper' and self.computer_choice == 'rock'):
            result = "user"
            self.user_score += 1
            self.result_label.config(text="🎉 YOU WIN!", fg='#27ae60')
        else:
            result = "computer"
            self.computer_score += 1
            self.result_label.config(text="😔 YOU LOSE!", fg='#e74c3c')
        
        self.rounds_played += 1
        self.update_display()
        self.enable_buttons()
        
        # Show detailed result
        self.show_detailed_result(result)
    
    def show_detailed_result(self, result):
        """Show detailed result in a message box"""
        if result == "tie":
            message = f"🤝 It's a tie!\n\nYou both chose {self.user_choice.upper()}!"
        elif result == "user":
            message = f"🎉 You win!\n\n{self.user_choice.upper()} beats {self.computer_choice.upper()}!"
        else:
            message = f"😔 You lose!\n\n{self.computer_choice.upper()} beats {self.user_choice.upper()}!"
        
        messagebox.showinfo("Game Result", message)
    
    def disable_buttons(self):
        """Disable choice buttons during animation"""
        self.rock_btn.config(state='disabled')
        self.paper_btn.config(state='disabled')
        self.scissors_btn.config(state='disabled')
    
    def enable_buttons(self):
        """Enable choice buttons"""
        self.rock_btn.config(state='normal')
        self.paper_btn.config(state='normal')
        self.scissors_btn.config(state='normal')
    
    def update_display(self):
        """Update score and rounds display"""
        self.score_label.config(text=f"🏆 SCORE: You {self.user_score} - {self.computer_score} Computer")
        self.rounds_label.config(text=f"📊 Rounds Played: {self.rounds_played}")
    
    def reset_game(self):
        """Reset the game"""
        if messagebox.askyesno("Reset Game", "Are you sure you want to reset the score?"):
            self.user_score = 0
            self.computer_score = 0
            self.rounds_played = 0
            self.user_choice = None
            self.computer_choice = None
            
            # Reset displays
            self.user_display.config(text="❓")
            self.user_choice_label.config(text="Make your choice!")
            self.computer_display.config(text="❓")
            self.computer_choice_label.config(text="Waiting...")
            self.result_label.config(text="🎯 Choose your weapon!", fg='#f39c12')
            
            self.update_display()
            self.enable_buttons()
    
    def quit_game(self):
        """Quit the game"""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            # Show final statistics
            if self.rounds_played > 0:
                win_percentage = (self.user_score / self.rounds_played) * 100
                final_message = f"📊 Final Statistics:\n\n"
                final_message += f"🏆 Final Score: You {self.user_score} - {self.computer_score} Computer\n"
                final_message += f"📈 Total Rounds: {self.rounds_played}\n"
                final_message += f"📊 Your Win Rate: {win_percentage:.1f}%\n\n"
                
                if self.user_score > self.computer_score:
                    final_message += "🎉 CONGRATULATIONS! You are the overall winner!"
                elif self.computer_score > self.user_score:
                    final_message += "🤖 The computer wins this session!"
                else:
                    final_message += "🤝 It's a tie overall!"
                
                messagebox.showinfo("Game Over", final_message)
            
            self.root.quit()

def main():
    """Main function to start the GUI game"""
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (800 // 2)
    y = (root.winfo_screenheight() // 2) - (600 // 2)
    root.geometry(f"800x600+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
