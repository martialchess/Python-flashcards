#!/usr/bin/env python3
"""
Python Flashcards - A modern GUI flashcard application
"""

import tkinter as tk
from tkinter import font, messagebox
import json
import os


class FlashcardApp:
    """Modern flashcard application with sleek design"""
    
    # Color scheme
    FACEBOOK_BLUE = "#1877F2"
    DEEP_PURPLE = "#6A0DAD"
    CARD_BG = "#FFFFFF"
    TEXT_COLOR = "#333333"
    SHADOW_COLOR = "#CCCCCC"
    
    def __init__(self, root):
        self.root = root
        self.root.title("Python Flashcards")
        self.root.geometry("800x600")
        self.root.configure(bg=self.FACEBOOK_BLUE)
        
        # Load flashcards
        self.flashcards = self.load_flashcards()
        if not self.flashcards:
            messagebox.showerror("Error", "No flashcards found in flashcards.json")
            self.root.destroy()
            return
        
        self.current_index = 0
        self.showing_front = True
        
        # Setup UI
        self.setup_ui()
        self.display_card()
        
        # Keyboard shortcuts
        self.root.bind('<space>', lambda e: self.flip_card())
        self.root.bind('<Left>', lambda e: self.previous_card())
        self.root.bind('<Right>', lambda e: self.next_card())
    
    def load_flashcards(self):
        """Load flashcards from JSON file"""
        try:
            json_path = os.path.join(os.path.dirname(__file__), 'flashcards.json')
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "flashcards.json file not found!")
            return []
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format in flashcards.json")
            return []
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.FACEBOOK_BLUE)
        main_frame.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Progress indicator at the top
        self.progress_label = tk.Label(
            main_frame,
            text="",
            font=('Arial', 12, 'bold'),
            fg=self.CARD_BG,
            bg=self.FACEBOOK_BLUE
        )
        self.progress_label.pack(pady=(0, 20))
        
        # Card frame with shadow effect
        card_container = tk.Frame(main_frame, bg=self.SHADOW_COLOR)
        card_container.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Inner card frame (white card)
        self.card_frame = tk.Frame(
            card_container,
            bg=self.CARD_BG,
            relief='flat',
            bd=0
        )
        self.card_frame.pack(expand=True, fill='both')
        
        # Card label indicator (Question/Answer)
        self.card_type_label = tk.Label(
            self.card_frame,
            text="QUESTION",
            font=('Arial', 10, 'bold'),
            fg=self.DEEP_PURPLE,
            bg=self.CARD_BG
        )
        self.card_type_label.pack(pady=(30, 10))
        
        # Card text
        self.card_text = tk.Label(
            self.card_frame,
            text="",
            font=('Arial', 18),
            fg=self.TEXT_COLOR,
            bg=self.CARD_BG,
            wraplength=650,
            justify='center',
            pady=20
        )
        self.card_text.pack(expand=True)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg=self.FACEBOOK_BLUE)
        button_frame.pack(pady=(20, 0))
        
        # Style for buttons
        button_style = {
            'font': ('Arial', 12, 'bold'),
            'fg': self.CARD_BG,
            'bg': self.DEEP_PURPLE,
            'activebackground': '#8B0DC7',
            'activeforeground': self.CARD_BG,
            'relief': 'flat',
            'bd': 0,
            'padx': 20,
            'pady': 10,
            'cursor': 'hand2'
        }
        
        # Previous button
        self.prev_button = tk.Button(
            button_frame,
            text="◀ Previous",
            command=self.previous_card,
            **button_style
        )
        self.prev_button.pack(side='left', padx=10)
        
        # Flip button
        self.flip_button = tk.Button(
            button_frame,
            text="🔄 Flip",
            command=self.flip_card,
            font=('Arial', 14, 'bold'),
            fg=self.CARD_BG,
            bg=self.DEEP_PURPLE,
            activebackground='#8B0DC7',
            activeforeground=self.CARD_BG,
            relief='flat',
            bd=0,
            padx=30,
            pady=12,
            cursor='hand2'
        )
        self.flip_button.pack(side='left', padx=10)
        
        # Next button
        self.next_button = tk.Button(
            button_frame,
            text="Next ▶",
            command=self.next_card,
            **button_style
        )
        self.next_button.pack(side='left', padx=10)
        
        # Keyboard shortcuts hint
        hint_label = tk.Label(
            main_frame,
            text="Keyboard: Space = Flip | ← → = Navigate",
            font=('Arial', 9),
            fg=self.CARD_BG,
            bg=self.FACEBOOK_BLUE
        )
        hint_label.pack(pady=(15, 0))
    
    def display_card(self):
        """Display the current flashcard"""
        if not self.flashcards:
            return
        
        card = self.flashcards[self.current_index]
        
        # Update progress
        total = len(self.flashcards)
        self.progress_label.config(
            text=f"Card {self.current_index + 1} of {total}"
        )
        
        # Update card content
        if self.showing_front:
            self.card_type_label.config(text="QUESTION")
            self.card_text.config(text=card['question'])
        else:
            self.card_type_label.config(text="ANSWER")
            self.card_text.config(text=card['answer'])
        
        # Update button states
        self.prev_button.config(state='normal' if self.current_index > 0 else 'disabled')
        self.next_button.config(state='normal' if self.current_index < total - 1 else 'disabled')
    
    def flip_card(self):
        """Flip the current card"""
        self.showing_front = not self.showing_front
        self.display_card()
    
    def next_card(self):
        """Move to the next card"""
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            self.showing_front = True
            self.display_card()
    
    def previous_card(self):
        """Move to the previous card"""
        if self.current_index > 0:
            self.current_index -= 1
            self.showing_front = True
            self.display_card()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
