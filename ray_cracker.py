
#!/usr/bin/env python3

import os
import sys
import time

# Terminal colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

LOADING_TIME = 5


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(RED + BOLD + r"""
 ____   ___  __   __
|  _ \ / _ \ \ \ / /
| |_) | | | | \ V /
|  _ <| |_| |  | |
|_| \_\\___/   |_|
""" + RESET)

    print(CYAN + BOLD + "       RAY CIPHER CRACKER" + RESET)
    print(GRAY + "       SHIFT ANALYSIS SYSTEM" + RESET)
    print(RED + "  " + "=" * 38 + RESET)


def decode_with_shift(numbers, shift):
    result = []

    for token in numbers.split("-"):
        token = token.strip()

        if not token:
            continue

        if not token.isdigit():
            raise ValueError("Input mesti mengandungi nombor sahaja.")

        number = int(token)

        if number == 0:
            result.append(" ")
        elif 1 <= number <= 26:
            original = (number - 1 - shift) % 26
            result.append(chr(original + ord("A")))
        else:
            raise ValueError("Nombor mesti antara 0 hingga 26.")

    return "".join(result)


def loading_animation(seconds=5):
    symbols = ["-", "\\", "|", "/"]
    start = time.monotonic()
    index = 0

    while time.monotonic() - start < seconds:
        symbol = symbols[index % len(symbols)]

        sys.stdout.write(
            "\r" + YELLOW + BOLD
            + f"  [{symbol}] ANALYZING CIPHER... "
            + f"{min(int(time.monotonic() - start) + 1, seconds)}/{seconds}s"
            + RESET
        )
        sys.stdout.flush()

        time.sleep(0.1)
        index += 1

    sys.stdout.write(
        "\r" + GREEN + BOLD
        + "  [✓] ANALYSIS COMPLETE!          "
        + RESET + "\n"
    )
    sys.stdout.flush()


def crack_mode():
    print(CYAN + "\n  >> CRACKING MODE" + RESET)
    code = input(WHITE + "\n  ENTER CIPHER > " + RESET).strip()

    try:
        # Validate input before starting the animation
        for token in code.split("-"):
            if not token.strip().isdigit():
                raise ValueError
            if not 0 <= int(token.strip()) <= 26:
                raise ValueError

        loading_animation(LOADING_TIME)

        print(CYAN + BOLD + "\n  >> POSSIBLE DECRYPTIONS\n" + RESET)

        for shift in range(26):
            decoded = decode_with_shift(code, shift)

            if shift == 7:
                print(
                    GREEN + BOLD
                    + f"  SHIFT {shift:02d} | {decoded}"
                    + RESET
                )
            else:
                print(
                    GRAY
                    + f"  SHIFT {shift:02d} | {decoded}"
                    + RESET
                )

        print(RED + "\n  " + "=" * 38 + RESET)
        print(GREEN + "  [✓] 26 SHIFT COMBINATIONS TESTED" + RESET)

    except ValueError:
        print(RED + "\n  [!] Invalid cipher input." + RESET)
        print(GRAY + "  Use numbers from 0 to 26 separated by hyphens." + RESET)


def main():
    while True:
        clear_screen()
        banner()

        print(WHITE + "\n  [1] " + RESET + "CRACK CIPHER")
        print(WHITE + "  [0] " + RESET + "EXIT")
        print(RED + "  " + "-" * 38 + RESET)

        choice = input(WHITE + "\n  SELECT OPTION > " + RESET).strip()

        if choice == "1":
            crack_mode()
            input(GRAY + "\n  Press ENTER to return to menu..." + RESET)

        elif choice == "0":
            print(RED + "\n  RAY CRACKER OFFLINE. GOODBYE." + RESET)
            break

        else:
            print(RED + "\n  [!] Invalid selection." + RESET)
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n\n  SESSION TERMINATED." + RESET)

