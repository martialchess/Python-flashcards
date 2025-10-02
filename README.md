# Python Flashcards

A modern GUI flashcard application to practice Python syntax with a sleek, modern design.

## Features

- 🎨 Modern design with Facebook blue (#1877F2) and deep purple (#6A0DAD) color scheme
- 💳 Flashcards with rounded edges and shadow effects
- 🔄 Flip cards to see questions and answers
- ⌨️ Keyboard shortcuts for easy navigation
- 📊 Progress indicator showing current position
- 📝 JSON-based flashcard storage for easy customization

## Requirements

- Python 3.x
- tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/martialchess/Python-flashcards.git
cd Python-flashcards
```

2. Ensure Python 3 and tkinter are installed:
```bash
python3 --version
python3 -m tkinter  # Should open a test window
```

## Usage

Run the flashcard application:
```bash
python3 flashcard_app.py
```

### Controls

- **Flip Button** or **Space**: Flip the current card to see the answer
- **Next Button** or **Right Arrow (→)**: Move to the next card
- **Previous Button** or **Left Arrow (←)**: Move to the previous card

## Customizing Flashcards

Edit the `flashcards.json` file to add, remove, or modify flashcards. Each flashcard should have a `question` and `answer` field:

```json
[
  {
    "question": "Your question here",
    "answer": "Your answer here"
  }
]
```

## License

MIT License
