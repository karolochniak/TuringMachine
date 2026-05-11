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
```text
% q0
0 0 R q0
1 1 R q1
$ $ R acc
