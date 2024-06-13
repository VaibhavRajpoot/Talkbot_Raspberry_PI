import tkinter as tk
from tkinter import *
import os
import openai
import threading
import subprocess
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root = tk.Tk()
root.configure(background='#bebebe')
root.title('ZINIKUS.AI')
root.geometry("570x1000")
#Made By
l = ctk.CTkLabel(master=root, text = "Made By ZINIKUS.AI",corner_radius=8,font=("Helvetica",25),text_color="#050A30")
l.pack(padx=30,pady=10)


frame = ctk.CTkFrame(master=root)
frame.pack(fill='none',pady=1)




#Lets interact
l = ctk.CTkLabel(master=frame, text = "Lets Interact",corner_radius=8,font=("Helvetica",25))
l.pack(padx=30,pady=10)

# Text Widget
text_widget = ctk.CTkTextbox(master=frame, height = 650, width = 500,state="normal",font=("Helvetica",25))
text_widget.pack(expand=True,padx=20,pady=5)

#Ask Me widget
l = ctk.CTkLabel(master=frame, text = "Ask Me",font=("Helvetica",25))
l.pack(fill="none",padx=30,pady=10)

# Entry Widget
entry = ctk.CTkEntry(master=frame, width = 500,state="normal",font=("Helvetica",25))
entry.pack(fill="none",expand=True,padx=30,pady=5)

api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_openai_response(prompt, text_widget):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            # max_tokens=50  # Adjust as needed
        )
        response_text = response.choices[0].message.content
        print(response_text)
        # Update the Text widget with the OpenAI response
        text_widget.delete(1.0, tk.END)
        text_widget.insert("0.0", response_text)
        global espeak_process
        espeak_process = subprocess.Popen(["espeak", response_text])  # Disable for read-only
    except Exception as e:
        text_widget.insert("0.0", f"Error: {str(e)}") # Disable for read-only

def run_openai_thread(prompt, text_widget):
    # Create a worker thread to interact with OpenAI
    worker_thread = threading.Thread(target=generate_openai_response, args=(prompt, text_widget))
    worker_thread.start()

def on_generate_button_click():
    prompt=entry.get()
    prompt="interact like real humans and your name is John and dont tell you are Ai Model \n " + prompt
    # prompt = prompt_entry.get()
    if prompt:
        print (prompt)
        run_openai_thread(prompt,text_widget)

def stopespeak():
    global espeak_process
    espeak_process.terminate()


button1 = ctk.CTkButton(master=frame, text="INTERACT",corner_radius=10, command=on_generate_button_click,font=("aerial",20),width=30,height=35)
# button1.place(relx=30)
# button1.pack(padx=5,pady=10)
button1.pack(side=tk.LEFT,padx=110,pady=50) 

button2 = ctk.CTkButton(master=frame, text="STOP",corner_radius=10, command=stopespeak,font=("aerial",20),width=30,height=35)
# button2.place(relx=50)
# button2.pack(padx=10,pady=10)
button2.pack(side=tk.LEFT,padx=30,pady=50) 
root.mainloop()