#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Animation Test Tool - Interactive Testing & Fine-Tuning
========================================================
Test all loading animation styles and adjust parameters in real-time
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from loading_animations import ModernProgressBar, ModernBounceLoader, HorizontalPulseLoader


class AnimationTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Master Search - Animation Tester")
        self.root.geometry("800x700")
        
        # Current animation instances
        self.current_progress = None
        self.current_loader = None
        self.animation_running = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the test interface"""
        
        # Title
        title = ttk.Label(self.root, text="🎬 Loading Animation Fine-Tuning", 
                         font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # ===== PROGRESS BAR SECTION =====
        progress_frame = ttk.LabelFrame(self.root, text=" Progress Bar Styles ", padding="10")
        progress_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(progress_frame, text="Select Style:").pack(side="left", padx=5)
        
        self.style_var = tk.StringVar(value="neon-pulse")
        styles = ["gradient", "neon", "neon-pulse", "smooth", "multi", "shimmer"]
        for style in styles:
            ttk.Radiobutton(progress_frame, text=style, variable=self.style_var, 
                          value=style, command=self.create_progress_bar).pack(side="left", padx=5)
        
        # Progress bar display area
        self.progress_canvas_frame = ttk.Frame(self.root)
        self.progress_canvas_frame.pack(fill="x", padx=10, pady=5)
        
        # Controls
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=5)
        
        ttk.Button(control_frame, text="▶️ Start", command=self.start_animation).pack(side="left", padx=5)
        ttk.Button(control_frame, text="⏹️ Stop", command=self.stop_animation).pack(side="left", padx=5)
        ttk.Button(control_frame, text="🔄 Restart", command=self.restart_animation).pack(side="left", padx=5)
        
        # Status
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(self.root, textvariable=self.status_var, 
                                font=("Arial", 11), foreground="blue")
        status_label.pack(pady=5)
        
        # ===== PARAMETERS SECTION =====
        params_frame = ttk.LabelFrame(self.root, text=" Animation Parameters ", padding="10")
        params_frame.pack(fill="x", padx=10, pady=5)
        
        # Width
        width_frame = ttk.Frame(params_frame)
        width_frame.pack(fill="x", pady=5)
        ttk.Label(width_frame, text="Width:").pack(side="left", padx=5)
        self.width_var = tk.IntVar(value=600)
        ttk.Scale(width_frame, from_=200, to=800, variable=self.width_var, 
                 orient="horizontal", command=lambda v: self.create_progress_bar()).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Label(width_frame, textvariable=self.width_var, width=4).pack(side="left", padx=5)
        
        # Height
        height_frame = ttk.Frame(params_frame)
        height_frame.pack(fill="x", pady=5)
        ttk.Label(height_frame, text="Height:").pack(side="left", padx=5)
        self.height_var = tk.IntVar(value=12)
        ttk.Scale(height_frame, from_=4, to=30, variable=self.height_var, 
                 orient="horizontal", command=lambda v: self.create_progress_bar()).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Label(height_frame, textvariable=self.height_var, width=4).pack(side="left", padx=5)
        
        # Color
        color_frame = ttk.Frame(params_frame)
        color_frame.pack(fill="x", pady=5)
        ttk.Label(color_frame, text="Color:").pack(side="left", padx=5)
        self.color_var = tk.StringVar(value="#00A8FF")
        colors = ["#00A8FF", "#00EEFF", "#00FF00", "#FF00FF", "#FFD700"]
        color_combo = ttk.Combobox(color_frame, textvariable=self.color_var, values=colors, width=12)
        color_combo.pack(side="left", padx=5)
        color_combo.bind("<<ComboboxSelected>>", lambda e: self.create_progress_bar())
        
        # ===== SPEED SECTION =====
        speed_frame = ttk.LabelFrame(self.root, text=" Animation Speed ", padding="10")
        speed_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(speed_frame, text="Speed (lower = faster):").pack(side="left", padx=5)
        self.speed_var = tk.IntVar(value=30)
        ttk.Scale(speed_frame, from_=10, to=100, variable=self.speed_var, 
                 orient="horizontal").pack(side="left", fill="x", expand=True, padx=5)
        ttk.Label(speed_frame, textvariable=self.speed_var, width=4).pack(side="left", padx=5)
        
        # ===== INFO SECTION =====
        info_frame = ttk.LabelFrame(self.root, text=" Current Settings ", padding="10")
        info_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.info_text = tk.Text(info_frame, height=6, width=80, font=("Courier", 9))
        self.info_text.pack(fill="both", expand=True)
        
        # Initial creation
        self.create_progress_bar()
        self.update_info()
    
    def create_progress_bar(self):
        """Create a new progress bar with current settings"""
        # Destroy old one
        if self.current_progress is not None:
            try:
                self.current_progress.stop_indeterminate()
                self.current_progress.destroy()
            except:
                pass
        
        # Clear canvas frame
        for widget in self.progress_canvas_frame.winfo_children():
            widget.destroy()
        
        # Create new progress bar
        self.current_progress = ModernProgressBar(
            self.progress_canvas_frame,
            width=self.width_var.get(),
            height=self.height_var.get(),
            color=self.color_var.get(),
            style=self.style_var.get()
        )
        
        self.update_info()
        
        if self.animation_running:
            self.current_progress.start_indeterminate()
    
    def start_animation(self):
        """Start the animation"""
        self.animation_running = True
        if self.current_progress:
            self.current_progress.start_indeterminate()
        self.status_var.set("▶️ Animation läuft...")
    
    def stop_animation(self):
        """Stop the animation"""
        self.animation_running = False
        if self.current_progress:
            self.current_progress.stop_indeterminate()
        self.status_var.set("⏹️ Animation gestoppt")
    
    def restart_animation(self):
        """Restart the animation"""
        self.stop_animation()
        self.root.after(200, self.start_animation)
    
    def update_info(self):
        """Update info display"""
        if self.current_progress:
            info = f"""
Current Configuration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Style:        {self.style_var.get()}
Width:        {self.width_var.get()} px
Height:       {self.height_var.get()} px
Color:        {self.color_var.get()}
Speed:        {self.speed_var.get()} ms (FPS ≈ {33//(self.speed_var.get()+3)})

Status:       {'RUNNING ▶️' if self.animation_running else 'STOPPED ⏹️'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tipps zum Feinabstimmen:
• Probiere alle 5 Styles durch
• Erhöhe die Height für bessere Sichtbarkeit
• Spiele mit Colors herum
• Speed beeinflusst die Flüssigkeit
            """
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(1.0, info)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationTester(root)
    root.mainloop()
