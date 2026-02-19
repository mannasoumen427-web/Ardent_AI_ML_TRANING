

import statistics

def get_number(prompt):
    """Safely get a float from user input (type casting)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌ Invalid input! Please enter a valid number.\n")

def basic_calculator():
    print("\n" + "="*45)
    print("       🔢  BASIC CALCULATOR")
    print("="*45)
    a = get_number("  Enter first number  : ")
    print("  Operations: +  -  *  /  %")
    op = input("  Choose operation   : ").strip()
    b = get_number("  Enter second number : ")

    if op == '+':
        result = a + b
        label = f"{a} + {b}"
    elif op == '-':
        result = a - b
        label = f"{a} - {b}"
    elif op == '*':
        result = a * b
        label = f"{a} × {b}"
    elif op == '/':
        if b == 0:
            print("  ❌ Error: Division by zero!\n")
            return
        result = a / b
        label = f"{a} ÷ {b}"
    elif op == '%':
        result = a % b
        label = f"{a} mod {b}"
    else:
        print("  ❌ Unknown operator!\n")
        return

    print(f"\n  ✅ {label} = {result}\n")

def stats_calculator():
    print("\n" + "="*45)
    print("       📊  STATISTICS CALCULATOR")
    print("="*45)
    raw = input("  Enter numbers separated by spaces: ").strip()

    try:
        # Type casting: convert each token to float
        numbers = [float(x) for x in raw.split()]
        if not numbers:
            raise ValueError
    except ValueError:
        print("  ❌ Invalid input! Enter space-separated numbers.\n")
        return

    n = len(numbers)
    total = sum(numbers)
    avg = total / n
    med = statistics.median(numbers)

    # Mode (handle no unique mode)
    try:
        mod = statistics.mode(numbers)
        mode_str = str(mod)
    except statistics.StatisticsError:
        # multimode available in Python 3.8+
        try:
            modes = statistics.multimode(numbers)
            mode_str = ", ".join(str(m) for m in modes) + " (multiple)"
        except AttributeError:
            mode_str = "No unique mode"

    mn = min(numbers)
    mx = max(numbers)

    print(f"""
  Numbers  : {numbers}
  ─────────────────────────────────────
  Count    : {n}
  Sum      : {total}
  Mean/Avg : {avg}
  Median   : {med}
  Mode     : {mode_str}
  Min      : {mn}
  Max      : {mx}
  Range    : {mx - mn}
""")

def percentage_calculator():
    print("\n" + "="*45)
    print("       💯  PERCENTAGE CALCULATOR")
    print("="*45)
    print("  1. What is X% of Y?")
    print("  2. X is what % of Y?")
    print("  3. % change from X to Y?")
    choice = input("  Choose (1/2/3): ").strip()

    if choice == '1':
        x = get_number("  Enter percentage (X): ")
        y = get_number("  Enter number (Y)    : ")
        print(f"\n  ✅ {x}% of {y} = {(x/100)*y}\n")
    elif choice == '2':
        x = get_number("  Enter part (X) : ")
        y = get_number("  Enter whole (Y) : ")
        if y == 0:
            print("  ❌ Whole cannot be zero!\n")
            return
        print(f"\n  ✅ {x} is {(x/y)*100:.2f}% of {y}\n")
    elif choice == '3':
        x = get_number("  Enter old value (X): ")
        y = get_number("  Enter new value (Y): ")
        if x == 0:
            print("  ❌ Old value cannot be zero!\n")
            return
        change = ((y - x) / abs(x)) * 100
        direction = "increase" if change >= 0 else "decrease"
        print(f"\n  ✅ {abs(change):.2f}% {direction} from {x} to {y}\n")
    else:
        print("  ❌ Invalid choice!\n")

def main():
    print("\n" + "★"*45)
    print("   ★   STAT CALC — Python Edition   ★")
    print("★"*45)

    menu = """
  ┌─────────────────────────────────────┐
  │  1 → Basic Calculator (+ - * / %)  │
  │  2 → Statistics (mean/median/mode) │
  │  3 → Percentage Calculator         │
  │  0 → Exit                          │
  └─────────────────────────────────────┘
"""
    while True:
        print(menu)
        choice = input("  Your choice: ").strip()

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            stats_calculator()
        elif choice == '3':
            percentage_calculator()
        elif choice == '0':
            print("\n  👋 Goodbye!\n")
            break
        else:
            print("  ❌ Invalid choice. Try 0–3.\n")

if __name__ == "__main__":
    main()
