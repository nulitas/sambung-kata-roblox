# Sambung Kata Helper (Roblox)

A quick and lightweight terminal helper script designed to help you win "Sambung Kata" (Word Chain) games, specifically tailored to the unique syllable and fallback rules used in Roblox games like *Sambat*.

## Features

- **Massive Dictionary**: Uses a full 71,500+ word KBBI dataset, which includes common words, loan words, and slang (e.g., *angpao*).
- **Smart Game-Logic Prediction**: Automatically calculates the exact syllable the game will likely ask for next, based on the **"Last Vowel"** (Vokal Terakhir) rule used by many Roblox bots.
- **Multi-Level Lookahead**: Shows you what words can be formed from the last 3 letters, 2 letters, and 1 letter of your answer, so you're never caught off guard.
- **Clean Results**: Automatically filters out spaced phrases, hyphens, and invalid inputs.

## Requirements

- Python 3.x
- `python-dotenv` package (for securely loading the dictionary links)

```bash
pip install python-dotenv
```

## Setup

1. Clone the repository to your local machine:
```bash
git clone https://github.com/nulitas/sambung-kata-roblox.git
cd sambung-kata-roblox
```

2. Create a `.env` file in the root directory and add the direct link to the raw text dictionary:
```env
# URL for the Indonesian KBBI Wordlist (txt format)
ID_DICT_URL="https://raw.githubusercontent.com/damzaky/kumpulan-kata-bahasa-indonesia-KBBI/master/list_1.0.0.txt"
```

## Usage

Run the script:
```bash
python sambung_kata.py
```

### How to use the helper:
1. When it's your turn, or when you are planning your next move, simply type the prefix/syllable you need (e.g., `ang`).
2. The script will instantly return a list of words that **start** with `ang`.
3. Look at the `*...*` prediction next to the words. This shows you exactly what syllable the next player will be forced to answer with!
   - Example: `anggur (Lanjut: *UR* -> urat, urus; 'GUR' -> gurih, guru; 'R' -> rumah, rusa)` 
   - Since `U` is the last vowel, the game will most likely ask for `UR`. You immediately know the next player's valid options.

## Disclaimer

This is a personal utility script created to help find valid dictionary words and understand word-chain game logic. Use it responsibly!


