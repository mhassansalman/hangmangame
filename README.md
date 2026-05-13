# Hangman Game 🎮

A terminal-based Hangman game built in Python. Guess the hidden word letter by letter before the man gets hanged!

Made as a first-semester Python project.

---

## Features

- Random words from 3 categories: Vegetables, Fruits, and Sports
- Hint shown at the start of each game
- Visual hangman drawn step by step in the terminal
- Player score tracking (wins, losses, total games) saved across sessions
- Input validation and duplicate guess detection
- Play again option after each game

---

## Files

| File | Purpose |
|------|---------|
| `finalgame.py` | Main game logic |
| `lists.py` | Word lists for each category |
| `scores.py` | Stores player stats (auto-updated on each game) |

---

## How to Run

Make sure you have Python 3 installed.

```bash
python finalgame.py
```

All 3 files must be in the same folder.

---

## How to Play

1. Enter your name
2. Your previous stats are shown (if any)
3. A hint tells you the category of the word
4. Guess one letter at a time
5. You get 6 wrong attempts before game over
6. Choose to play again or quit at the end

---
## Sample GamePlay
Enter your first name: hassan

Welcome, hassan!
Stats: Wins = 5, Losses = 0, Total Games = 5

 _____   
|     |  
|        
|        
|        
==========
Hint: Sports name
_ _ _ _ _ _ _ _ _ _

-------------------------------------------------------
Enter a single letter: c
Right guess!
 _____   
|     |  
|        
|        
|        
==========
_ _ _ _ _ _ _ _ _ _

-------------------------------------------------------
Enter a single letter: k
Wrong guess!
Wrong Attempts: 1
 _____   
|     |  
|     O  
|        
|        
==========
_ _ _ _ _ _ _ _ _ _

-------------------------------------------------------
Enter a single letter: b
Right guess!
 _____   
|     |  
|     O  
|        
|        
==========
b _ _ _ _ _ b _ _ _

-------------------------------------------------------
Enter a single letter: a
Right guess!
...
Congratulations! You Won!

Do you want to play again? (y/n): n

Thanks for playing! Goodbye, hassan!
Final Stats: Wins = 6, Losses = 0, Total Games = 6


## Requirements

- Python 3.x
- No external libraries needed
