import tkinter as tk
from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkCheckBox
from CTkMessagebox import CTkMessagebox
import re

# Password visibility and obscuring
def toggle_password():
    if show_password_var.get():
        password_entry.configure(show="")  # make password plain
    else:
        password_entry.configure(show="*")  # Hide the password

#Variables to store properties' contents of the feedback Messagebox
message = ""
title = ""
icon = ""

# Function to check password complexity
def check_password():
    global message, title, icon
    
    #Variables to check if requirements of strong password are met
    len_check = None
    upper_check = None
    lower_check = None
    num_check = None
    special_check = None
    
    #fetching password from the password entry
    password = password_entry.get()
    
    #None or empty password
    if password == "" or password == " ":
        CTkMessagebox(title="Warning", 
                        message="No Password entered. Please enter a password", 
                        icon="warning", 
                        option_1="Ok")
    else:
         # checking password length
        if len(password) < 8:
            message +="❌ Password is at least 8 characters long\n"
        else:
            message +="✅ Password is at least 8 characters long\n"
            len_check = True
        
        #checking if password has upper character(s)
        if not re.search(r'[A-Z]', password):
            message +="❌ Password contains at least one uppercase letter\n"
        else:
            message +="✅ Password contains at least one uppercase letter\n"
            upper_check = True
           
           
        #checking if password has lower character(s)
        if not re.search(r'[a-z]', password):
             message +="❌ Password contains at least one lowercase letter\n"
        else:
            message +="✅ Password contains at least one lowercase letter\n"
            lower_check = True

        
        #checking if password has digit(s)
        if not re.search(r'\d', password):
            message +="❌ Password contains at least one digit\n"
        else:
            message +="✅ Password contains at least one digit\n"
            num_check = True

        
        #checking if password has special character(s)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password): 
            message +="❌ Password contains at least one special character\n"
        else:
            message +="✅ Password contains at least one special character\n"
            special_check = True

        #Checking if all criteria are met
        if len_check == upper_check == lower_check == num_check == special_check == True:
            title = "Strong Password"
            icon = "check"
        else:
            title = "Weak Password"
            icon = "cancel"
    
        CTkMessagebox(title=title, 
                  message=message, 
                  icon=icon, 
                  option_1="Ok")
        
        
        
   #Changing the global varibales to have empty string to avoid unending concatenation
    message = ""
    title = ""
    icon = ""


app = CTk()
app.geometry("800x600")
app.title("Password Complexity Checker")
app.resizable(False, False)  


#Header
title_label = CTkLabel(app, text="🔐 Password Complexity Checker 🔒", 
                       font=("Arial", 22, "bold"), 
                       fg_color="#4682b4",  
                       text_color="white", 
                       corner_radius=8, width=400, height=50)
title_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

#Checkbox to show/hide password
show_password_var = tk.BooleanVar()
show_password_checkbox = CTkCheckBox(app, text="Show Password", variable=show_password_var, 
                                     command=toggle_password, text_color="white")
show_password_checkbox.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Password entry field
password_entry = CTkEntry(app, placeholder_text="Enter your password", show="*", width=300, height=40, corner_radius=8)
password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Check button
check_button = CTkButton(app, text="Check Password", command=check_password, font=("Arial Bold", 14),
                         width=200, height=40, corner_radius=8, fg_color="#32cd32",  
                         hover_color="#228b22",  
                         text_color="white")
check_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

# Footer
footer_label = CTkLabel(app, 
                        text="Aziizkaar@Prodigy InfoTech", 
                        font=("Arial", 14), text_color="white")
footer_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Run the application
app.mainloop()
