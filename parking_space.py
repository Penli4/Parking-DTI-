import tkinter as tk

def show_parking_lot():
    print("Opening Parking Lot Window")  # Debug print
    parking_window = tk.Tk()
    parking_window.title("Parking Lot Simulation")
    tk.Label(parking_window, text="Welcome to the Parking Lot!").pack()
    parking_window.mainloop()
