#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick test for progress bar initial state"""

import tkinter as tk
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from loading_animations import ModernProgressBar

root = tk.Tk()
root.title("Progress Bar Initial State Test")
root.geometry("700x300")

# Frame 1: Empty (0%)
frame1 = tk.Frame(root)
frame1.pack(pady=20, padx=20, fill="x")
tk.Label(frame1, text="0% - Empty (Initial):", font=("Arial", 10, "bold")).pack(anchor="w")
progress1 = ModernProgressBar(frame1, width=600, height=16, color="#00FF00", style="neon-pulse")
progress1.canvas.pack()

# Frame 2: 25%
frame2 = tk.Frame(root)
frame2.pack(pady=20, padx=20, fill="x")
tk.Label(frame2, text="25% - Filling:", font=("Arial", 10, "bold")).pack(anchor="w")
progress2 = ModernProgressBar(frame2, width=600, height=16, color="#00FF00", style="neon-pulse")
progress2.set_progress(0.25)
progress2.canvas.pack()

# Frame 3: 50%
frame3 = tk.Frame(root)
frame3.pack(pady=20, padx=20, fill="x")
tk.Label(frame3, text="50% - Half:", font=("Arial", 10, "bold")).pack(anchor="w")
progress3 = ModernProgressBar(frame3, width=600, height=16, color="#00FF00", style="neon-pulse")
progress3.set_progress(0.50)
progress3.canvas.pack()

# Frame 4: 100%
frame4 = tk.Frame(root)
frame4.pack(pady=20, padx=20, fill="x")
tk.Label(frame4, text="100% - Full:", font=("Arial", 10, "bold")).pack(anchor="w")
progress4 = ModernProgressBar(frame4, width=600, height=16, color="#00FF00", style="neon-pulse")
progress4.set_progress(1.0)
progress4.canvas.pack()

root.mainloop()
