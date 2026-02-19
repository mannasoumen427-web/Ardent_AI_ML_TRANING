# 🧮 STAT CALC — Python Console Calculator

A Python-based interactive console calculator that combines **arithmetic operations** with a full **statistics engine** and a **percentage tool** — all driven by user input with safe type casting.

---

## 🚀 Features

| Module | Capabilities |
|---|---|
| 🔢 Basic Calculator | Addition, Subtraction, Multiplication, Division, Modulo (`%`) |
| 📊 Statistics | Mean, Median, Mode, Count, Sum, Min, Max, Range |
| 💯 Percentage | X% of Y, X as % of Y, % change between two values |

---

## 📁 File Structure

```
stat-calc/
└── calculator.py   # Main script — all logic in one file
```

---

## ▶️ How to Run

**Requirements:** Python 3.6+, no external libraries needed.

```bash
python3 calculator.py
```

You'll be greeted with a menu:

```
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
   ★   STAT CALC — Python Edition   ★
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

  ┌─────────────────────────────────────┐
  │  1 → Basic Calculator (+ - * / %)  │
  │  2 → Statistics (mean/median/mode) │
  │  3 → Percentage Calculator         │
  │  0 → Exit                          │
  └─────────────────────────────────────┘
```

---

## 📖 Usage Examples

### 1️⃣ Basic Calculator
```
Enter first number  : 10
Choose operation    : /
Enter second number : 4

✅ 10.0 ÷ 4.0 = 2.5
```
Supported operators: `+`  `-`  `*`  `/`  `%`

---

### 2️⃣ Statistics Calculator
```
Enter numbers separated by spaces: 3 5 7 7 9

Numbers  : [3.0, 5.0, 7.0, 7.0, 9.0]
─────────────────────────────────────
Count    : 5
Sum      : 31.0
Mean/Avg : 6.2
Median   : 7.0
Mode     : 7.0
Min      : 3.0
Max      : 9.0
Range    : 6.0
```

---

### 3️⃣ Percentage Calculator
```
1. What is X% of Y?       →  20% of 500 = 100.0
2. X is what % of Y?      →  50 is 25.00% of 200
3. % change from X to Y?  →  5.00% increase from 100 to 105
```

---

## 🛠️ Code Highlights

- **Type Casting** — All user input is captured as strings and safely cast to `float` using a `get_number()` helper with `try/except ValueError` to catch bad input.
- **Statistics Module** — Uses Python's built-in `statistics` library for `median` and `mode`; handles multi-mode datasets gracefully via `multimode()` (Python 3.8+).
- **Input Validation** — Every input is validated; errors are reported clearly without crashing the program.
- **Loop Menu** — The app runs in a `while True` loop until the user selects `0` to exit.

---

## 🐍 Requirements

- Python **3.6+** (3.8+ recommended for `multimode` support)
- Standard library only — `statistics` module (built-in, no `pip install` needed)

---

## 📄 License

MIT License — free to use, modify, and distribute.

