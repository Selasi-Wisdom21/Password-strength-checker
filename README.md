# Password Strength Checker

A simple Python command-line tool that evaluates the strength of a user-entered password based on length and character composition.

## Features

- Prompts the user to enter a password via the terminal
- Scores the password out of **7 points** based on:
  - **Length**
    - 8–10 characters → +1
    - 11–15 characters → +2
    - 16+ characters → +3
  - **Character composition**
    - Contains an uppercase letter → +1
    - Contains a digit (0–9) → +1
    - Contains a lowercase letter → +1
    - Contains a special character (`!@#$%^&`) → +1
- Classifies the password as **Weak**, **Medium**, or **Strong** based on the final score
- Displays guidance on what makes a strong password

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `re` module)

## Installation

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

## Usage

Run the script from the terminal:

```bash
python "Password_Strength.py"
```

You'll be prompted to enter a password, and the script will output a strength score and rating.

### Example

```
Password Strength checker
Enter your password: MySecureP@ss123
MySecureP@ss123
Password strength score: 6/7
Strength: Strong
A STRONG PASSWORD SHOULD BE AT LEAST 10 CHARACTERS LONG AND CONTAIN UPPERCASE, LOWERCASE, SPECIAL CHARACTERS AND NUMBERS
```

## Scoring Breakdown

| Score Range | Strength |
|-------------|----------|
| 0–2         | Weak     |
| 3–4         | Medium   |
| 5–7         | Strong   |

## Known Limitations

- The password is printed to the terminal in plain text after entry (not masked) — not suitable for production/security-sensitive use as-is.
- Special character check only covers `!@#$%^&`; other symbols (e.g., `*`, `?`, `_`, `-`) are not recognized.
- A score of exactly `5` falls into neither the "Medium" (`<= 4`) nor "Strong" (`> 5`) branch due to the current conditional logic, so it prints nothing — this is a minor bug worth fixing (e.g., changing the last condition to `>= 5`).

## Author

Selasi

## License

This project is for educational purposes.

