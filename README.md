# Even 1's Turing Machine - A Python Tkinter Application 🎮🤖

## Introduction 🎉

Welcome to the **Even 1's Turing Machine** project! This Python application implements a **Turing machine** that checks whether a given binary string has an **even number of '1's**. It uses **Tkinter** for an interactive graphical user interface (GUI), allowing users to input a binary string and visualize the Turing machine's operation step-by-step.

## Key Features 🔑

- **Even/Odd '1's Check**: The Turing machine will analyze whether the number of '1's in the input binary string is even or odd.
- **Interactive GUI**: Built using Python's Tkinter library, it provides an easy-to-use interface for interacting with the Turing machine.
- **Step-by-Step Animation**: Visualize how the Turing machine processes the tape, moves the head, and changes states during the computation.
- **Real-Time Feedback**: The result (either "accept" or "reject") is displayed based on the machine's final state after processing the entire input string.

## Project Breakdown 🛠️

### 1. **The Turing Machine Class (`EvenOnesTM`)**

This class is the core of the Turing machine's logic. It processes the input tape (a binary string) to determine whether the number of '1's is even.

- **`__init__(self, tape)`**: The constructor initializes the Turing machine with a tape, a head at the start position, and the initial state `q0`.
- **`step(self)`**: This method processes one step of the Turing machine. It reads the symbol under the head, performs state transitions based on the symbol, and moves the head one position to the right.
- **`run(self)`**: This method repeatedly calls `step()` until the Turing machine halts (either accepting or rejecting the input).

#### State Transitions 🔄:

- **State `q0`**:
  - On reading '1', transition to state `q1`.
  - On reading '0', stay in state `q0`.
  
- **State `q1`**:
  - On reading '1', transition back to state `q0`.
  - On reading '0', stay in state `q1`.

The machine **accepts** the string if, after processing the entire tape, it ends in state `q0` (an even number of '1's). If the machine ends in state `q1`, the string is **rejected** (odd number of '1's).

### 2. **The GUI Class (`TuringMachineApp`)**

This class provides the graphical interface for the user to interact with the Turing machine.

- **`__init__(self, root)`**: Initializes the Tkinter window with the necessary widgets, including labels, input fields, and buttons for interaction.
- **`run_tm(self)`**: This method handles user input, validates it, and runs the Turing machine.
- **`animation(self, tape_input, tm)`**: Simulates the Turing machine's head movements and updates the animation in real time.
- **`update_animation(self, tape_input, tm, head_position)`**: Updates the display to show the current state, head position, and tape.
- **`clear_animation(self)`**: Clears the animation display once the computation is complete.

## How It Works 🔧

1. The user enters a binary string (only '0's and '1's) into the input field.
2. The **Turing machine** checks whether the string has an **even** or **odd** number of '1's.
3. The GUI provides a visual step-by-step animation, showing the Turing machine's tape and head movement.
4. Once the tape is fully processed, the machine **accepts** (if the count of '1's is even) or **rejects** (if the count of '1's is odd) the string.
5. The result is displayed on the GUI.

## Installation 🛠️

To run this project locally, follow these steps:

1. **Install Python**: If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
2. **Install Tkinter**: Tkinter should come pre-installed with Python. If it's missing, you can install it by running:
   ```bash
   pip install tk
3. Clone this repository or download the script and run it.

## Running the Application 🚀

After setting up the environment:

1. Open the script file in your preferred Python editor (e.g., VS Code, PyCharm).
2. Run the script, and the GUI should appear.
3. Enter a binary string (e.g., "1100", "10101", "111") and click **Run Turing Machine** to see the result.

## Example 👇

## Example 1: Even Number of 1's 👇

**Input:**  
Binary String: `1100`

**Processing Steps:**
- Head starts at the first character: `1` → State: `q0` → Move to the next character.
- Head moves to the second character: `1` → State: `q1` → Move to the next character.
- Head moves to the third character: `0` → State remains `q1` → Move to the next character.
- Head moves to the fourth character: `0` → State remains `q1` → End of tape.

**Result:**  
The string has an **even** number of '1's (2 '1's). **Result: Accept** ✅

## Example 2: Odd Number of 1's 👇

**Input:**  
Binary String: `1011`

**Processing Steps:**
- Head starts at the first character: `1` → State: `q0` → Move to the next character.
- Head moves to the second character: `0` → State remains `q0` → Move to the next character.
- Head moves to the third character: `1` → State: `q1` → Move to the next character.
- Head moves to the fourth character: `1` → State: `q0` → End of tape.

**Result:**  
The string has an **odd** number of '1's (3 '1's). **Result: Reject** ❌

## Conclusion 🎯

This project is a great example of how a simple algorithm can be visualized and interacted with using modern tools like Tkinter. It allows users to understand how a **Turing machine** operates and the importance of **state transitions** in computational theory.


