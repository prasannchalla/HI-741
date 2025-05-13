import tkinter as tk
from tkinter import messagebox
from validator import Validator  # Updated import
from patientRecordManager import PatientRecordManager  # Updated import
from admin import Admin  # Updated import
from manager import Manager  # Updated import
from healthProfessional import HealthProfessional  # Updated import
import os

# Correct file paths for credentials, patient data, and notes
CREDENTIALS_FILE = "Patient_data.csv"  # Your credentials file path
PATIENT_DATA_FILE = "Patient_data.csv"  # Your patient data file path
NOTES_FILE = "Notes.csv"  # Your patient notes file path

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Clinical Data UI")  # Window title
        self.validator = Validator(CREDENTIALS_FILE)  # Initialize credential validator
        self.record_manager = PatientRecordManager(PATIENT_DATA_FILE, NOTES_FILE)  # Manage patient records
        self.current_user = None
        self.username = None
        self.role = None
        self._login_screen()  # Start with the login screen

    def _login_screen(self):
        self._clear_frame()  # Clear any existing widgets

        # Add username and password input fields
        tk.Label(self.master, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1)

        # Login button
        tk.Button(self.master, text="Login", command=self._validate_login).grid(row=2, columnspan=2)

    def _validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate credentials
        if self.validator.validate_credentials(username, password):
            self.username = username
            self.role = self.validator.get_user_role(username)
            self._launch_role_interface()  # Launch role-specific interface
        else:
            messagebox.showerror("Error", "Invalid credentials")  # Show error message

    def _launch_role_interface(self):
        self._clear_frame()  # Clear any existing widgets

        # Different interfaces for different roles
        if self.role == "admin":
            self.current_user = Admin(self.role, self.record_manager)
            tk.Button(self.master, text="Count Visits", command=self.current_user.count_visits).pack()
        elif self.role == "management":
            self.current_user = Manager(self.role, self.record_manager)
            tk.Button(self.master, text="Generate Key Stats", command=self.current_user.generate_statistics).pack()
        elif self.role in ["nurse", "clinician"]:
            self.current_user = HealthProfessional(self.role, self.record_manager)
            tk.Button(self.master, text="Retrieve Patient", command=self.current_user.retrieve_patient).pack()
            tk.Button(self.master, text="Add Patient", command=self.current_user.add_patient).pack()
            tk.Button(self.master, text="Remove Patient", command=self.current_user.remove_patient).pack()
            tk.Button(self.master, text="Count Visits", command=self.current_user.count_visits).pack()
            tk.Button(self.master, text="View Note", command=self.current_user.view_note).pack()
        else:
            messagebox.showerror("Error", "Unknown role")  # Handle unknown role error

        # Exit button to close the application
        tk.Button(self.master, text="Exit", command=self.master.quit).pack()

    def _clear_frame(self):
        # Clear all widgets from the current window
        for widget in self.master.winfo_children():
            widget.destroy()

# Run the application if this script is executed directly
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = App(root)  # Initialize the application with the Tk window
    root.mainloop()  # Start the Tkinter event loop
