import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid Operation"
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid Input")
    except ZeroDivisionError:
        label_result.config(text="Cannot divide by zero")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set up the layout
root.geometry("300x250")
root.configure(bg='lightblue')

# Number 1
tk.Label(root, text="Number 1:", bg='lightblue').pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Number 2
tk.Label(root, text="Number 2:", bg='lightblue').pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Operation choice
operation_var = tk.StringVar(value="+")
tk.Radiobutton(root, text="+", variable=operation_var, value="+", bg='lightblue').pack(pady=2)
tk.Radiobutton(root, text="-", variable=operation_var, value="-", bg='lightblue').pack(pady=2)
tk.Radiobutton(root, text="*", variable=operation_var, value="*", bg='lightblue').pack(pady=2)
tk.Radiobutton(root, text="/", variable=operation_var, value="/", bg='lightblue').pack(pady=2)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg='lightgreen').pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", bg='lightblue')
label_result.pack(pady=10)

# Run the application
root.mainloop()
