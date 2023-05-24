import tkinter as tk
import tkinter.messagebox as messagebox

# Function to register a new admin
def register():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username is available
    if username not in admin_data:
        admin_data[username] = password
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showerror("Error", "Username already exists!")

    # Clear the input fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to handle admin login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password match
    if username in admin_data and admin_data[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        show_management_window()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

    # Clear the input fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to show the management window
def show_management_window():
    login_window.destroy()

    management_window = tk.Tk()
    management_window.title("Stock Management")

    # Function to manage stock
    def manage_stock():
        # Implement the code to manage stock
        pass

    # Function to view all stock
    def view_stock():
        # Implement the code to view stock
        pass

    # Create buttons for stock management and viewing
    manage_button = tk.Button(management_window, text="Manage Stock", command=manage_stock)
    manage_button.pack()

    view_button = tk.Button(management_window, text="View Stock", command=view_stock)
    view_button.pack()

    management_window.mainloop()

# Create the main window for admin registration and login
login_window = tk.Tk()
login_window.title("Manager Login")

# Create labels and entry fields for username and password
username_label = tk.Label(login_window, text="Username:")
username_label.pack()

username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Create buttons for registration and login
register_button = tk.Button(login_window, text="Register", command=register)
register_button.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

admin_data = {}  # Dictionary to store admin credentials

login_window.mainloop()
