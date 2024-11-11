import tkinter as tk
from tkinter import messagebox

class EvenOnesTM:
    def __init__(self, tape):
        self.tape = list(tape)  # The tape is the input string as a list of characters
        self.head = 0           # Head starts at the beginning of the tape
        self.state = 'q0'       # Start state

    def step(self):
        if self.head >= len(self.tape):
            return 'reject'

        # Read the current symbol under the head
        symbol = self.tape[self.head]

        # Turing machine transition rules
        if self.state == 'q0':
            if symbol == '1':
                self.state = 'q1'
            # If symbol is '0', remain in q0
        elif self.state == 'q1':
            if symbol == '1':
                self.state = 'q0'
            # If symbol is '0', remain in q1

        self.head += 1  # Move the head to the right

        # Check if the machine is in a final state and end of tape is reached
        if self.head == len(self.tape):
            if self.state == 'q0':  # Accept if in state q0 at the end
                return 'accept'
            else:                   # Reject if in state q1 at the end
                return 'reject'

        return 'continue'  # Continue processing if not at the end of the tape

    def run(self):
        while True:
            result = self.step()
            if result in ('accept', 'reject'):
                return result

# Interactive frontend using tkinter with modern styling
class TuringMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Even 1's Turing Machine")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f0f0")

        # Title Label
        self.title_label = tk.Label(self.root, text="Turing Machine - Even Number of 1's", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Input Label
        self.input_label = tk.Label(self.root, text="Enter a binary string:", font=("Arial", 14), bg="#f0f0f0")
        self.input_label.pack(pady=10)

        # Input Entry
        self.entry = tk.Entry(self.root, font=("Arial", 14), width=40, borderwidth=2, relief="solid")
        self.entry.pack(pady=10)

        # Process Button
        self.process_button = tk.Button(self.root, text="Run Turing Machine", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.run_tm)
        self.process_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#00796b")
        self.result_label.pack(pady=20)

        # Animation Frames
        self.animation_frame = tk.Label(self.root, text="", font=("Arial", 14), bg="#f0f0f0", fg="#e64a19")
        self.animation_frame.pack(pady=10)

    def run_tm(self):
        tape_input = self.entry.get()

        # Validate input (only allow '0's and '1's)
        if not set(tape_input).issubset({'0', '1'}):
            messagebox.showerror("Invalid Input", "Please enter a binary string (only '0's and '1's).")
            return

        tm = EvenOnesTM(tape_input)
        self.animation(tape_input, tm)

        result = tm.run()

        if result == 'accept':
            self.result_label.config(text="The string has an even number of 1's.", fg="#388e3c")
        else:
            self.result_label.config(text="The string has an odd number of 1's.", fg="#d32f2f")

    def animation(self, tape_input, tm):
        self.animation_frame.config(text="Processing...")

        # Simulate head movement and update animation
        for i in range(len(tape_input)):
            tm.head = i
            self.root.after(i * 500, self.update_animation(tape_input, tm, i))
        
        self.root.after(len(tape_input) * 500, self.clear_animation)

    def update_animation(self, tape_input, tm, head_position):
        tape_display = ''.join(['[' + ch + ']' if i == head_position else ch for i, ch in enumerate(tape_input)])
        self.animation_frame.config(text=f"Tape: {tape_display}  State: {tm.state}  Head Position: {head_position + 1}")
        self.root.update()

    def clear_animation(self):
        self.animation_frame.config(text="")
        self.root.update()

# Create the root window and start the GUI
root = tk.Tk()
app = TuringMachineApp(root)
root.mainloop()