import tkinter as tk

def show_bsod():
    root.destroy()

    bsod = tk.Tk()
    bsod.attributes("-fullscreen", True)  # Set the window to fullscreen
    bsod.configure(bg="red")  # Changed to red for BSOD

    base_text = """ :(  Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.
    Stop code: VIRUS_NET_FAILURE  """

    label = tk.Label(
        bsod,
        text=base_text + "25% complete",
        bg="red",  # Background color red
        fg="white",
        font=("Consolas", 20),  # Slightly smaller font size to fit better
        justify="left",
        anchor="nw",  # Align text to top left
        padx=20,  # Add some padding from left
        pady=20   # Add some padding from top
    )

    # Add the label to a frame to enable better centering
    frame = tk.Frame(bsod, bg="red")
    frame.pack(expand=True, fill="both")  # Expand and fill the frame

    label.pack(expand=True, anchor="n")  # Pack label inside the frame to center

    progress_values = ["25% complete", "50% complete", "75% complete", "100% complete"]

    def update_progress(index=0):
        if index < len(progress_values):
            label.config(text=base_text + progress_values[index])
            bsod.after(1000, lambda: update_progress(index + 1))
        else:
            bsod.destroy()

    update_progress()

    bsod.bind("<Escape>", lambda e: bsod.destroy())

    bsod.mainloop()

# --- Fake Login ---
root = tk.Tk()
root.title("virus.net Login")
root.geometry("400x300")
root.configure(bg="black")  # Keep background black for login screen

title = tk.Label(root, text="Log in to virus.net", fg="red", bg="black", font=("Arial", 18))  # Text color red on black bg
title.pack(pady=20)

username = tk.Entry(root)
username.pack(pady=5)

password = tk.Entry(root, show="*")
password.pack(pady=5)

submit = tk.Button(root, text="Log In", command=show_bsod)
submit.pack(pady=20)

root.mainloop()
