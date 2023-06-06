import tkinter as tk
import webbrowser

def open_link(link):
    webbrowser.open(link)

def show_links():
    root = tk.Tk()
    root.geometry("300x150")
    root.title("Choose a Link")

    link1 = tk.Button(root, text="https://www.youtube.com/watch?v=CpNBODqTA34", command=lambda: open_link("https://www.youtube.com/watch?v=CpNBODqTA34"))
    link1.pack(pady=5)

    link2 = tk.Button(root, text="https://www.youtube.com/watch?v=bw7bVpI5VcM", command=lambda: open_link("https://www.youtube.com/watch?v=bw7bVpI5VcM"))
    link2.pack(pady=5)

    link3 = tk.Button(root, text="https://www.youtube.com/watch?v=9iIX4PBplAY", command=lambda: open_link("https://www.youtube.com/watch?v=9iIX4PBplAY"))
    link3.pack(pady=5)

    link4 = tk.Button(root, text="https://www.youtube.com/watch?v=GFA9C2h1lJU", command=lambda: open_link("https://www.youtube.com/watch?v=GFA9C2h1lJU"))
    link4.pack(pady=5)

    root.mainloop()

def negtivte():
    root = tk.Tk()
    root.geometry("300x150")
    root.title("Choose a Link")

    link1 = tk.Button(root, text="https://www.youtube.com/watch?v=CpNBODqTA34",
                      command=lambda: open_link("https://www.youtube.com/watch?v=CpNBODqTA34"))
    link1.pack(pady=5)

    link2 = tk.Button(root, text="https://www.youtube.com/watch?v=bw7bVpI5VcM",
                      command=lambda: open_link("https://www.youtube.com/watch?v=bw7bVpI5VcM"))
    link2.pack(pady=5)

    link3 = tk.Button(root, text="https://www.youtube.com/watch?v=9iIX4PBplAY",
                      command=lambda: open_link("https://www.youtube.com/watch?v=9iIX4PBplAY"))
    link3.pack(pady=5)

    link4 = tk.Button(root, text="https://www.youtube.com/watch?v=GFA9C2h1lJU",
                      command=lambda: open_link("https://www.youtube.com/watch?v=GFA9C2h1lJU"))
    link4.pack(pady=5)

    root.mainloop()

def neural():
    root = tk.Tk()
    root.geometry("300x150")
    root.title("Choose a Link")

    link1 = tk.Button(root, text="https://www.youtube.com/watch?v=ybxt5dBVg5w",
                      command=lambda: open_link("https://www.youtube.com/watch?v=ybxt5dBVg5w"))
    link1.pack(pady=5)

    link2 = tk.Button(root, text="https://www.youtube.com/watch?v=bw7bVpI5VcM",
                      command=lambda: open_link("https://www.youtube.com/watch?v=bw7bVpI5VcM"))
    link2.pack(pady=5)

    link3 = tk.Button(root, text="https://www.youtube.com/watch?v=9iIX4PBplAY",
                      command=lambda: open_link("https://www.youtube.com/watch?v=9iIX4PBplAY"))
    link3.pack(pady=5)

    link4 = tk.Button(root, text="https://www.youtube.com/watch?v=GFA9C2h1lJU",
                      command=lambda: open_link("https://www.youtube.com/watch?v=GFA9C2h1lJU"))
    link4.pack(pady=5)

    root.mainloop()