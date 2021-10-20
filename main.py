import tkinter as tk
from Bio.Seq import Seq

# Declare global variables
DNA1 = None
DNA2 = None
Result = None

# This function is called whenever the button is pressed
def convert():

    global DNA1
    global DNA2
    global Result 

    # Convert Celsius to Fahrenheit and update label (through textvariable)
    try:
      val1 = entry_1.get()
      val2 = entry_2.get()
      entry_1_strand = Seq(val1)
      reverse_strand = entry_1_strand.reverse_complement()

      if reverse_strand == val2: 
        Result.set("True")
      else: 
        Result.set("False")

    except:
        pass

# Create the main window
root = tk.Tk()
root.title("DNA Check if Strand is a Complement")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container, specify that we want it to grow with window size
frame.pack(fill=tk.BOTH, expand=True)

# Allow middle cell of grid to grow when window is resized
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

# Variables for holding temperature data
DNA1 = tk.StringVar()
DNA2 = tk.StringVar()
Result = tk.StringVar() 

# Create widgets
entry_1 = tk.Entry(frame, width=7, textvariable=DNA1)
entry_2 = tk.Entry(frame, width=7, textvariable=DNA2)
label_unitc = tk.Label(frame, text="Strand 1")
label_equal = tk.Label(frame, text="Strand 2")
label_fahrenheit = tk.Label(frame, textvariable=Result)
label_unitf = tk.Label(frame, text="Result")
button_convert = tk.Button(frame, text="Convert", command=convert)

# Lay out widgets
entry_1.grid(row=0, column=0, padx=5, pady=5)
entry_2.grid(row=0, column=3, padx=5, pady=5)
label_unitc.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
label_equal.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
label_fahrenheit.grid(row=1, column=1, padx=5, pady=5)
label_unitf.grid(row=1,column=0, padx=5, pady=5, sticky=tk.W)
button_convert.grid(row=1, column=3, columnspan=2, padx=5, pady=5, sticky=tk.E)

# Place cursor in entry box by default
entry_2.focus()


# Run forever!
root.mainloop()