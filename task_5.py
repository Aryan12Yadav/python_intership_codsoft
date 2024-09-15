import tkinter as tk  # Import the tkinter module for GUI elements
from tkinter import messagebox, simpledialog  # Import specific components for message boxes and dialogs

class ContactManagerApp:
    def __init__(self, root):
        self.root = root  # Store the main window reference
        self.root.title("Contact Manager")  # Set the window title
        self.root.geometry("800x600")  # Set the window size
        self.root.config(bg="light pink")  # Set the background color of the window

        # Initialize contact list as an empty dictionary
        self.contacts = {}

        # Create the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, 
                                    text="Aryan Yadav Project",  # Text to display on the label
                                    font=("Helvetica", 16, "bold"),  # Font style, size, and weight
                                    bg="light pink")  # Background color of the label
        self.title_label.pack(pady=20)  # Pack the label with padding

        # Main Menu Frame
        self.main_menu_frame = tk.Frame(self.root, bg="light pink")  # Create a frame for the main menu
        self.main_menu_frame.pack(pady=20)  # Pack the frame with padding

        # Add Contact Button
        self.add_contact_button = tk.Button(self.main_menu_frame, 
                                            text="Add Contact",  # Text on the button
                                            command=self.add_contact,  # Function to call when the button is pressed
                                            font=("Helvetica", 12, "bold"),  # Font style, size, and weight
                                            width=20, height=2,  # Button width and height
                                            bg="#FFDDC1")  # Background color of the button
        self.add_contact_button.pack(pady=10)  # Pack the button with padding

        # View Contacts Button
        self.view_contacts_button = tk.Button(self.main_menu_frame, 
                                              text="View Contact List",  # Text on the button
                                              command=self.view_contacts,  # Function to call when the button is pressed
                                              font=("Helvetica", 12, "bold"),  # Font style, size, and weight
                                              width=20, height=2,  # Button width and height
                                              bg="#FFABAB")  # Background color of the button
        self.view_contacts_button.pack(pady=10)  # Pack the button with padding

        # Search Contact Button
        self.search_contact_button = tk.Button(self.main_menu_frame, 
                                               text="Search Contact",  # Text on the button
                                               command=self.search_contact,  # Function to call when the button is pressed
                                               font=("Helvetica", 12, "bold"),  # Font style, size, and weight
                                               width=20, height=2,  # Button width and height
                                               bg="#FFC3A0")  # Background color of the button
        self.search_contact_button.pack(pady=10)  # Pack the button with padding

        # Update Contact Button
        self.update_contact_button = tk.Button(self.main_menu_frame, 
                                               text="Update Contact",  # Text on the button
                                               command=self.update_contact,  # Function to call when the button is pressed
                                               font=("Helvetica", 12, "bold"),  # Font style, size, and weight
                                               width=20, height=2,  # Button width and height
                                               bg="#B9FBC0")  # Background color of the button
        self.update_contact_button.pack(pady=10)  # Pack the button with padding

        # Delete Contact Button
        self.delete_contact_button = tk.Button(self.main_menu_frame, 
                                               text="Delete Contact",  # Text on the button
                                               command=self.delete_contact,  # Function to call when the button is pressed
                                               font=("Helvetica", 12, "bold"),  # Font style, size, and weight
                                               width=20, height=2,  # Button width and height
                                               bg="#D5AAFF")  # Background color of the button
        self.delete_contact_button.pack(pady=10)  # Pack the button with padding

    def add_contact(self):
        # Prompt the user to enter a contact name
        name = simpledialog.askstring("Add Contact", "Enter contact name:")
        if name in self.contacts:
            messagebox.showwarning("Warning", "Contact already exists!")  # Show warning if contact exists
            return
        
        # Prompt the user to enter contact details
        phone = simpledialog.askstring("Add Contact", "Enter phone number:")
        email = simpledialog.askstring("Add Contact", "Enter email:")
        address = simpledialog.askstring("Add Contact", "Enter address:")

        # Add the new contact to the contacts dictionary
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Info", "Contact added successfully!")  # Show success message

    def view_contacts(self):
        # Create a new window to display the contact list
        view_window = tk.Toplevel(self.root)
        view_window.title("Contact List")  # Set the window title
        view_window.geometry("400x300")  # Set the window size
        view_window.config(bg="light pink")  # Set the background color of the window

        tk.Label(view_window, text="Contact List", bg="light pink").pack(pady=10)  # Label for the contact list
        contact_list = tk.Listbox(view_window, width=50, height=15)  # Listbox to display contacts
        contact_list.pack()  # Pack the listbox

        # Populate the listbox with contact names
        for name in self.contacts:
            contact_list.insert(tk.END, name)

        # Bind double-click event to show contact details
        contact_list.bind("<Double-1>", lambda e: self.show_contact_details(contact_list.get(contact_list.curselection())))

    def show_contact_details(self, name):
        # Get contact details from the dictionary
        contact = self.contacts.get(name, {})
        # Format the contact details into a message string
        message = f"Name: {name}\nPhone: {contact.get('phone', 'N/A')}\nEmail: {contact.get('email', 'N/A')}\nAddress: {contact.get('address', 'N/A')}"
        # Show the contact details in a message box
        messagebox.showinfo("Contact Details", message)

    def search_contact(self):
        # Prompt the user to enter a search term
        search_name = simpledialog.askstring("Search Contact", "Enter contact name or phone number:")
        # Find contacts that match the search term
        result = [(name, info) for name, info in self.contacts.items() if search_name.lower() in name.lower() or search_name in info['phone']]

        # Create a new window to display search results
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Results")  # Set the window title
        search_window.geometry("400x300")  # Set the window size
        search_window.config(bg="light pink")  # Set the background color of the window

        tk.Label(search_window, text="Search Results", bg="light pink").pack(pady=10)  # Label for search results
        result_list = tk.Listbox(search_window, width=50, height=15)  # Listbox to display search results
        result_list.pack()  # Pack the listbox

        # Populate the listbox with search results
        for name, info in result:
            result_list.insert(tk.END, f"{name} - {info['phone']}")

    def update_contact(self):
        # Prompt the user to enter the name of the contact to update
        name = simpledialog.askstring("Update Contact", "Enter contact name to update:")
        if name not in self.contacts:
            messagebox.showwarning("Warning", "Contact not found!")  # Show warning if contact does not exist
            return
        
        # Prompt the user to enter new contact details with initial values
        phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=self.contacts[name]['phone'])
        email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=self.contacts[name]['email'])
        address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=self.contacts[name]['address'])

        # Update the contact in the dictionary
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Info", "Contact updated successfully!")  # Show success message

    def delete_contact(self):
        # Prompt the user to enter the name of the contact to delete
        name = simpledialog.askstring("Delete Contact", "Enter contact name to delete:")
        if name in self.contacts:
            del self.contacts[name]  # Remove the contact from the dictionary
            messagebox.showinfo("Info", "Contact deleted successfully!")  # Show success message
        else:
            messagebox.showwarning("Warning", "Contact not found!")  # Show warning if contact does not exist

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = ContactManagerApp(root)  # Initialize the application
    root.mainloop()  # Start the Tkinter event loop
