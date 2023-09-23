import tkinter as tk

def calculate():
    num1 = float(e1.get())
    num2 = float(e2.get())
    operation = operation_var.get()

    if operation == '+':
        result.set(num1 + num2)
    elif operation == '-':
        result.set(num1 - num2)
    elif operation == '*':
        result.set(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            result.set("Division by zero error")
        else:
            result.set(num1 / num2)
    else:
        result.set("Invalid operation")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create GUI components
frame = tk.Frame(app)
frame.pack(pady=10)

l1 = tk.Label(frame, text="Enter first number:")
l1.grid(row=0, column=0)

e1 = tk.Entry(frame)
e1.grid(row=0, column=1)

l2 = tk.Label(frame, text="Enter second number:")
l2.grid(row=1, column=0)

e2 = tk.Entry(frame)
e2.grid(row=1, column=1)

operation_var = tk.StringVar()
operation_label = tk.Label(frame, text="Select operation:")
operation_label.grid(row=2, column=0)

operation_menu = tk.OptionMenu(frame, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=2, column=1)

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar()
result_label = tk.Label(app, textvariable=result)
result_label.pack(pady=10)

app.mainloop()
