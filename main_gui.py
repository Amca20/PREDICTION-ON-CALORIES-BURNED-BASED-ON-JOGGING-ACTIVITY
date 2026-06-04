import tkinter as tk
from tkinter import ttk
import os
from calory_logic import predict_calories
from recommendation_logic import generate_recommendation

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Function to switch to the result page
def show_result_page(name, height, weight, distance, time, goal_weight_loss, goal_weeks, calories_per_hour, bmi, recommendation, time_needed, distance_needed):
    for widget in root.winfo_children():
        widget.destroy()

    result_frame = ttk.Frame(root, padding="20 20 20 20", borderwidth=2, relief="solid")
    result_frame.pack(padx=20, pady=20, fill="both", expand=True)

    ttk.Label(result_frame, text="Jogging Planner", style="Header.TLabel").pack(pady=10)

    result_text = (
        f"Name: {name}\nHeight: {height} cm\nWeight: {weight} kg\n\n"
        f"BMI: {bmi:.2f}\nCalories Burned Per Hour: {calories_per_hour:.2f} Cal\n\n"
        f"Goal: Lose {goal_weight_loss} kg in {goal_weeks} weeks\n"
        f"Time Needed Per Day: {time_needed:.2f} hours\nDistance Needed Per Day: {distance_needed:.2f} km\n\n"
        f"Recommendation:\n=============================================\n"
        f"{recommendation}\n============================================="
    )
    ttk.Label(result_frame, text=result_text, style="Body.TLabel", justify="left").pack(padx=10, pady=10)

    ttk.Button(result_frame, text="Back", command=create_input_form, style="Accent.TButton").pack(pady=10)

# Function to perform calculations and switch to the result page
def calculate_and_recommend():
    try:
        name = name_entry.get()
        if not name:
            raise ValueError("Name is required")

        try:
            height_cm = float(height_entry.get())
            if height_cm <= 0:
                raise ValueError("Height must be a positive number")
        except ValueError:
            raise ValueError("Invalid height value")

        try:
            weight = float(weight_entry.get())
            if weight <= 0:
                raise ValueError("Weight must be a positive number")
        except ValueError:
            raise ValueError("Invalid weight value")

        try:
            distance = float(distance_entry.get())
            if distance <= 0:
                raise ValueError("Distance must be a positive number")
        except ValueError:
            raise ValueError("Invalid distance value")

        try:
            time = float(time_entry.get())
            if time <= 0:
                raise ValueError("Time must be a positive number")
        except ValueError:
            raise ValueError("Invalid time value")

        try:
            goal_weight_loss = float(goal_weight_loss_entry.get())
            if goal_weight_loss <= 0:
                raise ValueError("Goal weight loss must be a positive number")
        except ValueError:
            raise ValueError("Invalid goal weight loss value")

        try:
            goal_weeks = float(goal_weeks_entry.get())
            if goal_weeks <= 0:
                raise ValueError("Goal weeks must be a positive number")
        except ValueError:
            raise ValueError("Invalid goal weeks value")

        # Calculate BMI (height in cm)
        bmi = weight / ((height_cm / 100) ** 2)

        print(f"Height: {height_cm}, Weight: {weight}, Distance: {distance}, Time: {time}, BMI: {bmi}")

        # Predict calories burned per hour
        calories_per_hour = predict_calories(weight, height_cm, distance, time, bmi)
        print(f"Calories per hour: {calories_per_hour}")

        # Generate personalized recommendation
        recommendation, time_needed, distance_needed = generate_recommendation(weight, height_cm, time, distance, goal_weight_loss, goal_weeks, calories_per_hour)
        print(f"Recommendation: {recommendation}, Time needed: {time_needed}, Distance needed: {distance_needed}")

        # Switch to result page
        show_result_page(name, height_cm, weight, distance, time, goal_weight_loss, goal_weeks, calories_per_hour, bmi, recommendation, time_needed, distance_needed)
    except ValueError as e:
        print(f"Error: {e}")
        message_label.config(text=f"Error: {e}", foreground="red")

# Function to create the input form page
def create_input_form():
    for widget in root.winfo_children():
        widget.destroy()

    input_frame = ttk.Frame(root, padding="20 20 20 20", borderwidth=2, relief="solid")
    input_frame.pack(padx=20, pady=20, fill="both", expand=True)

    ttk.Label(input_frame, text="Jogging Planner", style="Header.TLabel").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(input_frame, text="Name:", style="Body.TLabel").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global name_entry
    name_entry = ttk.Entry(input_frame, style="Body.TEntry")
    name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Height (cm):", style="Body.TLabel").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    global height_entry
    height_entry = ttk.Entry(input_frame, style="Body.TEntry")
    height_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Weight (kg):", style="Body.TLabel").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    global weight_entry
    weight_entry = ttk.Entry(input_frame, style="Body.TEntry")
    weight_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Distance (km/day):", style="Body.TLabel").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    global distance_entry
    distance_entry = ttk.Entry(input_frame, style="Body.TEntry")
    distance_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Time (hours/day):", style="Body.TLabel").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    global time_entry
    time_entry = ttk.Entry(input_frame, style="Body.TEntry")
    time_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Goal Weight Loss (kg):", style="Body.TLabel").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    global goal_weight_loss_entry
    goal_weight_loss_entry = ttk.Entry(input_frame, style="Body.TEntry")
    goal_weight_loss_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Goal Time (weeks):", style="Body.TLabel").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    global goal_weeks_entry
    goal_weeks_entry = ttk.Entry(input_frame, style="Body.TEntry")
    goal_weeks_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    calc_button = ttk.Button(input_frame, text="Calculate and Recommend", command=calculate_and_recommend, style="Accent.TButton")
    calc_button.grid(row=8, column=0, columnspan=2, pady=10)

    global message_label
    message_label = ttk.Label(input_frame, text="", foreground="red")
    message_label.grid(row=9, column=0, columnspan=2, pady=5)

# Function to show the privacy notice and wait for agreement
def show_privacy_notice():
    for widget in root.winfo_children():
        widget.destroy()

    privacy_frame = ttk.Frame(root, padding="20 20 20 20", borderwidth=2, relief="solid")
    privacy_frame.pack(padx=20, pady=20, fill="both", expand=True)

    privacy_text = (
        "We are committed to protecting your privacy. All data you provide while using our system will remain strictly confidential "
        "and will not be used for any purpose other than generating accurate predictions. Your data will not be shared, stored, "
        "or used for machine learning model training. Ensuring the security and privacy of your information is our top priority."
    )
    ttk.Label(privacy_frame, text="Privacy Notice", style="Header.TLabel").pack(pady=10)
    ttk.Label(privacy_frame, text=privacy_text, style="Body.TLabel", justify="left", wraplength=400).pack(padx=10, pady=10)
    ttk.Button(privacy_frame, text="I agree and proceed", command=create_input_form, style="Accent.TButton").pack(pady=10)

# Main GUI window
root = tk.Tk()
root.title("Jogging Planner")

# Apply styles for a modern look
style = ttk.Style()
style.configure("Header.TLabel", font=("Helvetica", 18, "bold"))
style.configure("Body.TLabel", font=("Helvetica", 12))
style.configure("Body.TEntry", font=("Helvetica", 12))
style.configure("Accent.TButton", font=("Helvetica", 12), foreground="black", background="#3498db")
style.map("Accent.TButton", foreground=[("active", "black")], background=[("active", "#2980b9")])

# Show privacy notice on launch
show_privacy_notice()

root.configure(padx=20, pady=20)
root.mainloop()
