import tkinter as tk

# Function to handle button clicks
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    elif text == "⌫":
        expression = expression[:-1]
        screen_var.set(expression)
    else:
        expression += text
        screen_var.set(expression)

# Create main window
root = tk.Tk()
root.title("Calcify GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Variable to store expression
expression = ""
screen_var = tk.StringVar()

# Display screen
entry = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=8, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/", "⌫"],
    ["4", "5", "6", "*", "("],
    ["1", "2", "3", "-", ")"],
    ["0", ".", "=", "+", "C"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        button = tk.Button(
            frame,
            text=btn,
            font="Arial 14 bold",
            bd=2,
            relief=tk.RAISED
        )
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
