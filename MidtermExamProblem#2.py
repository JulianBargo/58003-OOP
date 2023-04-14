import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Midterm Exam Problem 2")
# create the input label and entry widget for centimeters
cm_label = tk.Label(root, text="Enter the distance in centimeter(cm):")
cm_label.grid(row=0, column=0)
cm_entry = tk.Entry(root, width=20)
cm_entry.grid(row=0, column=1)

# create the output labels and entry widgets for meters and kilometers
m_label = tk.Label(root, text="Conversion into meters(m):")
m_label.grid(row=1, column=0)
m_entry = tk.Entry(root, width=20)
m_entry.grid(row=1, column=1)

km_label = tk.Label(root, text="Conversion into kilometers(km):")
km_label.grid(row=2, column=0)
km_entry = tk.Entry(root, width=20)
km_entry.grid(row=2, column=1)


# define a function to convert the length from centimeters to meters and kilometers
def convert_length():
    try:
        cm = float(cm_entry.get())
        m = cm / 100
        km = cm / 100000
        m_entry.delete(0, tk.END)
        km_entry.delete(0, tk.END)
        m_entry.insert(0, str(m))
        km_entry.insert(0, str(km))
    except ValueError:
        cm_entry.delete(0, tk.END)
        m_entry.delete(0, tk.END)
        km_entry.delete(0, tk.END)
        cm_entry.insert(0, "Invalid input")


# create the convert button
convert_button = tk.Button(root, text="Convert", command=convert_length)
convert_button.grid(row=3, column=0, columnspan=2)

# run the main loop
root.mainloop()

if __name__ == "__main__":
    CircleGUI()
