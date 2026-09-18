# SecureMall — Password-Protected Mall Management System

A menu-driven Python console application for managing mall product data, with password-protected access to every sensitive action. Built to practice secure file handling, hidden password input, and modular Python design.

## Overview

SecureMall lets an admin manage a mall's product inventory through a simple text-based menu. Every action that touches or modifies data — adding a product or viewing the product list — is gated behind a password check. Passwords are entered using hidden ("shadow mode") input so nothing is echoed to the terminal, and the password itself is never hardcoded into any script — it's loaded from a separate file at runtime.

## Features

- 🔐 **Password-protected actions** — adding products and viewing the product catalog both require successful authentication first
- 👁️ **Hidden password input** — uses Python's `getpass` module so typed passwords are never shown on screen
- 📁 **File-based persistence** — product data, trending products, and the stored password all live in separate `.txt` files rather than being hardcoded
- 🧩 **Modular design** — each responsibility (security check, product addition, product viewing, trending display) lives in its own `.py` file and is imported into the main program
- 📊 **Trending products view** — displays a pre-curated list of trending mall products
- 🔁 **Persistent menu loop** — the program keeps running and re-prompting until the user explicitly chooses to exit

## Project Structure

```
SecureMall/
│
├── MyMall.py            # Main entry point — menu-driven interface, imports and ties together all modules
├── security_check.py    # Handles password verification using getpass (shadow/hidden input)
├── safepassword.py    # Creates/stores the password in a text file (run once during setup)
├── StoreManage.py        # Takes user input to add new products to the mall's product file
├── StoreManage.py      # Reads and displays all stored products
├── trending_p.py           # Displays trending products from a pre-created file
│
├── secret_password.txt          # Stores the password (excluded from version control — see below)
├── trending_products.txt     # Stores all added product data
└── trending_p.txt # Pre-populated list of trending products
```

## How It Works

1. **`MyMall.py`** launches a loop that displays a menu with four options:
   - `1` — Add a product (requires password)
   - `2` — View all products (requires password)
   - `3` — View trending products (no password required)
   - `4` — Exit the program

2. When a password-protected option is selected, **`security_check.py`** is called. It:
   - Loads the correct password from `secret_password.txt` via a `load_password()` function (`return file.read().strip()`)
   - Prompts the user with `getpass.getpass()`, which hides input as it's typed
   - Re-prompts on incorrect entries until the correct password is entered

3. Once authenticated, the corresponding module runs:
   - **`StoreManage.py`** collects product details from the user and appends them to `mall_products.txt`
   - **`StoreManage.py`** reads and prints all saved product records

4. **`trending_products.py`** simply reads and displays the contents of a pre-created `trending_p.txt` — no authentication needed, since it's read-only reference data.

## Getting Started

### Prerequisites
- Python 3.10+ (required for `match`/`case` syntax used in the menu)

### Setup

1. Clone the repository:
   ```bash
  git clone https://github.com/GlitchWH/SecureMall---Password-Protected-Mall-Management-System
   ```

2. Set your password by running the password setup script once:
   ```bash
   python safepassword.py
   ```

3. Run the main program:
   ```bash
   python MyMall.py
   ```

4. Follow the on-screen menu to add products, view products, or check trending items.

## Security Notes

- The current implementation stores the password in **plain text** inside `secret_password.txt`. This keeps the password out of source code, but the file itself is still readable if someone has access to it.
- `secret_password.txt` is excluded from version control via `.gitignore` and should **never** be committed or shared.
- This project is intended as a learning exercise in file handling and basic authentication flow — not a production-grade security system. A future improvement would be to hash and salt the password (e.g., using `hashlib.pbkdf2_hmac` or `bcrypt`) rather than storing it as plain text.

## Possible Future Improvements

- [ ] Hash and salt the stored password instead of storing it as plain text
- [ ] Add input validation for menu choices (handle non-numeric input gracefully)
- [ ] Support editing/removing existing products
- [ ] Move product data storage from `.txt` to a structured format (JSON or CSV)
- [ ] Add a login attempt limit / lockout after repeated failures

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Built by GlitchWH as a practice project in Python file handling and basic secure authentication.
