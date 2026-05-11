# Turing Machine Simulator 🎰

A custom Turing Machine simulator written in Python. This project reads machine instructions from a formatted text file, simulates an infinite tape, and executes state transitions until it reaches an accept (`acc`) or reject (`rej`) state. 

The provided configuration specifically checks whether a given binary number is **divisible by 3**.

---

## 🎯 About the Project

This implementation provides a flexible framework for running various Turing Machine algorithms. It parses a custom syntax to define the initial tape, the starting state, and the transition functions. 

To mimic the infinite nature of a Turing Machine tape, the program pads the initial input array with blank symbols (`$`), allowing the read/write head to move freely in both directions without throwing out-of-bounds errors.

---

## 📝 Input File Syntax (`podzielnosc3.txt`)

The simulator requires a text file with a specific syntax to build the machine's logic.

**Global Directives:**
* `! input <string>` — Defines the initial string on the tape (e.g., `! input 110`).
* `! start_state <state>` — Defines the starting state (e.g., `! start_state q0`).
* `! Koniec` — Marks the end of the file parsing.

**State Definitions:**
States are declared using `% <state_name>`. Below it, the transition rules are defined in the following format:
`[read_symbol] [write_symbol] [direction (R/L)] [next_state]`

*Example:*

% q0
0 0 R q0
1 1 R q1
$ $ R acc


🧩 Python Implementation Details
The Turing class consists of several key methods handling the simulation:

odczyt_pliku(): Parses the configuration text file and builds a nested dictionary of instructions (dict_instrukcje).

modif_tasma(extend): Pads the initial input with $ symbols to simulate infinite memory on both ends of the tape.

ruch_tasma(ob_znak): Calculates the new position of the read/write head based on the R (Right) or L (Left) instruction.

odczyt_tasma(): The main execution loop. It reads the current symbol, looks up the transition rule, writes the new symbol, moves the head, and updates the state. The loop terminates when the state becomes either "acc" or "rej".

konwersja_tasma_bis(): Cleans up the final tape by removing the padding symbols ($) before printing the final state.

🚀 Execution
Ensure you have Python 3 installed.

Save your Turing machine rules in a file named podzielnosc3.txt in the same directory as the Python script.

Run the script from the terminal:

Bash
python turing.py
Expected Output
For the input 110 (which is 6 in decimal), the machine will reach the acc state and output:

Wynik na taśmie: 110
Liczba jest podzielna przez 3
For inputs not divisible by 3 (e.g., 100 -> 4), it will reach the rej state and output:

Wynik na taśmie: 100
Liczba NIE jest podzielna przez 3.
