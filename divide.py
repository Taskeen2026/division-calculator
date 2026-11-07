import tkinter as tk


def divide():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())

        if b == 0:
            result.config(text="Error: Zero se divide nahi ho sakta!", fg="#E74C3C")
            return

        answer = a / b  # true division, decimal result deta hai

        # 6 decimal places tak, extra zeros hata do (2.500000 -> 2.5, 4.000000 -> 4)
        text = f"{answer:.6f}".rstrip("0").rstrip(".")

        result.config(text=f"{a:g} ÷ {b:g} = {text}", fg="#2ECC71")

    except ValueError:
        result.config(text="Please enter valid numbers!\nEx: 5 and 2", fg="#E74C3C")


def clear():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result.config(text="Enter two numbers", fg="#2ECC71")


# Window
win = tk.Tk()
win.title("Division Calculator")
win.geometry("380x360")
win.config(bg="#0A2342")

tk.Label(
    win,
    text="DIVISION CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="#0A2342",
    fg="white"
).pack(pady=20)

f = tk.Frame(win, bg="#0A2342")
f.pack(pady=10)

tk.Label(f, text="Number 1", bg="#0A2342", fg="white").grid(row=0, column=0, padx=15)
tk.Label(f, text="Number 2", bg="#0A2342", fg="white").grid(row=0, column=1, padx=15)

num1_entry = tk.Entry(f, width=12, justify="center")
num1_entry.grid(row=1, column=0, padx=15, pady=5)

num2_entry = tk.Entry(f, width=12, justify="center")
num2_entry.grid(row=1, column=1, padx=15, pady=5)

tk.Button(
    win,
    text="DIVIDE",
    bg="#E67E22",
    fg="white",
    font=("Arial", 12, "bold"),
    command=divide
).pack(pady=10)

tk.Button(
    win,
    text="CLEAR",
    bg="#E67E22",
    fg="white",
    width=10,
    command=clear
).pack(pady=5)

result = tk.Label(
    win,
    text="Enter two numbers",
    bg="#0A2342",
    fg="#2ECC71",
    font=("Arial", 12)
)
result.pack(pady=20)

win.mainloop()