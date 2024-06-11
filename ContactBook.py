import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Contact Book", font=('Helvetica', 24, 'bold'))
        self.title_label.pack(pady=20)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, font=('Helvetica', 12))
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts, font=('Helvetica', 12))
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, font=('Helvetica', 12))
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, font=('Helvetica', 12))
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=('Helvetica', 12))
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contacts_str = "\n".join([f"{name}: {info['phone']}" for name, info in self.contacts.items()])
        if not contacts_str:
            contacts_str = "No contacts found."
        messagebox.showinfo("Contacts List", contacts_str)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter Name or Phone Number:")
        if not search_term:
            return
        
        results = [f"{name}: {info['phone']}, {info['email']}, {info['address']}" 
                   for name, info in self.contacts.items() 
                   if search_term.lower() in name.lower() or search_term in info['phone']]
        
        if results:
            result_str = "\n".join(results)
        else:
            result_str = "No matching contacts found."
        
        messagebox.showinfo("Search Results", result_str)

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter Name of the contact to update:")
        if not name or name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return
        
        phone = simpledialog.askstring("Update", f"Enter new Phone Number (current: {self.contacts[name]['phone']}):")
        email = simpledialog.askstring("Update", f"Enter new Email (current: {self.contacts[name]['email']}):")
        address = simpledialog.askstring("Update", f"Enter new Address (current: {self.contacts[name]['address']}):")

        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter Name of the contact to delete:")
        if not name or name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        del self.contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
