#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Modern Loading Animation System
==============================================
Beautiful, smooth loading animations for GUI components

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.10
"""

import tkinter as tk
from tkinter import ttk
import math
import threading
import time
from typing import Optional, Callable


class HorizontalPulseLoader:
    """Modern horizontal pulse loader with expanding line from center."""
    
    def __init__(self, parent, size=80, color="#00EEFF", bg_color="#F0F0F0", pulse_duration=1.0):
        self.parent = parent
        self.size = size
        self.color = color
        self.bg_color = bg_color
        self.pulse_duration = pulse_duration
        
        # Create canvas for custom drawing
        self.canvas = tk.Canvas(parent, width=size, height=size, 
                               highlightthickness=0, relief='flat', bg=bg_color)
        self.canvas.pack(pady=5)
        
        # Animation state
        self.animation_running = False
        self.animation_thread = None
        self.pulse_phase = 0.0  # 0.0 to 1.0
        
        # Line configuration
        self.center_x = size // 2
        self.center_y = size // 2
        self.max_length = size // 2 - 5
        
        self._draw_line()
    
    def _draw_line(self):
        """Draw expanding horizontal line from center with current pulse phase."""
        self.canvas.delete("all")
        
        # Calculate current length and opacity based on pulse phase
        if self.pulse_phase <= 0.7:
            # Expanding phase
            length = self.max_length * (self.pulse_phase / 0.7)
            opacity = 1.0
        else:
            # Fade out phase
            length = self.max_length
            fade_phase = (self.pulse_phase - 0.7) / 0.3
            opacity = 1.0 - fade_phase
        
        # Calculate line width based on opacity (simple fade effect)
        line_width = max(1, int(4 * opacity))
        
        # Calculate horizontal line endpoints
        start_x = self.center_x - length
        end_x = self.center_x + length
        y = self.center_y
        
        # Draw horizontal line with variable width for fade effect
        if line_width > 0 and length > 0:
            self.canvas.create_line(start_x, y, end_x, y,
                                  fill=self.color, width=line_width, capstyle=tk.ROUND)
        
        # Draw center dot
        dot_size = int(3 * opacity) if opacity > 0.3 else 0
        if dot_size > 0:
            self.canvas.create_oval(self.center_x - dot_size, self.center_y - dot_size,
                                   self.center_x + dot_size, self.center_y + dot_size,
                                   fill=self.color, outline="")
    
    def start(self):
        """Start the pulsing animation."""
        if not self.animation_running:
            self.animation_running = True
            self.animation_thread = threading.Thread(target=self._animate, daemon=True)
            self.animation_thread.start()
    
    def stop(self):
        """Stop the animation."""
        self.animation_running = False
        if self.animation_thread and self.animation_thread.is_alive():
            self.animation_thread.join(timeout=0.1)
    
    def _animate(self):
        """Animation loop."""
        start_time = time.time()
        
        while self.animation_running:
            current_time = time.time()
            elapsed = current_time - start_time
            
            # Calculate pulse phase (0.0 to 1.0, then reset)
            self.pulse_phase = (elapsed % self.pulse_duration) / self.pulse_duration
            
            # Update display on main thread
            try:
                self.canvas.after_idle(self._draw_line)
                time.sleep(0.016)  # ~60 FPS
            except tk.TclError:
                break  # Canvas destroyed
    
    def destroy(self):
        """Clean up the loader."""
        self.stop()
        if hasattr(self, 'canvas'):
            self.canvas.destroy()


class ModernProgressBar:
    """Modern, animated progress bar with gradient and pulse effects."""
    
    def __init__(self, parent, width=400, height=8, color="#00EEFF", bg_color="#E8E8E8"):
        self.parent = parent
        self.width = width
        self.height = height
        self.color = color
        self.bg_color = bg_color
        
        # Create canvas for custom drawing
        self.canvas = tk.Canvas(parent, width=width, height=height, 
                               highlightthickness=0, relief='flat')
        self.canvas.pack(pady=5)
        
        # Animation state
        self.progress = 0.0
        self.is_indeterminate = False
        self.animation_offset = 0
        self.animation_running = False
        self.animation_thread = None
        
        # Draw initial state
        self._draw_progress()
    
    def _draw_progress(self):
        """Draw the progress bar with current state."""
        self.canvas.delete("all")
        
        # Background
        self.canvas.create_rectangle(0, 0, self.width, self.height,
                                   fill=self.bg_color, outline="")
        
        if self.is_indeterminate:
            # Indeterminate animation - moving gradient
            gradient_width = 80
            x_pos = (self.animation_offset % (self.width + gradient_width)) - gradient_width
            
            # Create moving highlight effect
            self.canvas.create_rectangle(x_pos, 0, x_pos + gradient_width, self.height,
                                       fill=self.color, outline="")
            
            # Add glow effect
            glow_start = max(0, x_pos - 20)
            glow_end = min(self.width, x_pos + gradient_width + 20)
            if glow_end > glow_start:
                self.canvas.create_rectangle(glow_start, 0, glow_end, self.height,
                                           fill=self.color, outline="", stipple="gray25")
        else:
            # Determinate progress
            if self.progress > 0:
                fill_width = int(self.width * self.progress)
                self.canvas.create_rectangle(0, 0, fill_width, self.height,
                                           fill=self.color, outline="")
                
                # Add shine effect
                if fill_width > 20:
                    shine_x = fill_width - 10
                    self.canvas.create_rectangle(shine_x, 0, shine_x + 2, self.height,
                                               fill="#FFFFFF", outline="", stipple="gray12")
    
    def set_progress(self, value: float):
        """Set progress value (0.0 to 1.0)."""
        self.progress = max(0.0, min(1.0, value))
        self.is_indeterminate = False
        self._draw_progress()
    
    def start_indeterminate(self):
        """Start indeterminate animation."""
        self.is_indeterminate = True
        if not self.animation_running:
            self.animation_running = True
            self.animation_thread = threading.Thread(target=self._animate, daemon=True)
            self.animation_thread.start()
    
    def stop_indeterminate(self):
        """Stop indeterminate animation."""
        self.animation_running = False
        self.is_indeterminate = False
        self._draw_progress()
    
    def _animate(self):
        """Animation loop for indeterminate state."""
        while self.animation_running:
            self.animation_offset += 3
            if self.animation_offset > self.width + 100:
                self.animation_offset = -100
            
            try:
                self.canvas.after_idle(self._draw_progress)
                time.sleep(0.03)  # ~30 FPS
            except:
                break
    
    def destroy(self):
        """Clean up the progress bar."""
        self.stop_indeterminate()
        self.canvas.destroy()


class SpinningLoader:
    """Modern spinning loader with smooth rotation."""
    
    def __init__(self, parent, size=32, color="#00A8FF", speed=2):
        self.parent = parent
        self.size = size
        self.color = color
        self.speed = speed
        
        # Create canvas
        self.canvas = tk.Canvas(parent, width=size, height=size,
                               highlightthickness=0, relief='flat', bg='white')
        self.canvas.pack()
        
        # Animation state
        self.angle = 0
        self.animation_running = False
        self.animation_thread = None
    
    def _draw_spinner(self):
        """Draw the spinning loader."""
        self.canvas.delete("all")
        
        center_x = self.size // 2
        center_y = self.size // 2
        radius = self.size // 3
        
        # Draw multiple arcs with different opacity
        for i in range(8):
            start_angle = self.angle + (i * 45)
            alpha = 1.0 - (i * 0.1)
            
            # Calculate arc color with alpha
            color = self._blend_color(self.color, "#FFFFFF", 1.0 - alpha)
            
            # Draw arc segment
            arc_start = start_angle - 20
            arc_extent = 40
            
            self.canvas.create_arc(center_x - radius, center_y - radius,
                                 center_x + radius, center_y + radius,
                                 start=arc_start, extent=arc_extent,
                                 outline=color, width=3, style="arc")
    
    def _blend_color(self, color1: str, color2: str, factor: float) -> str:
        """Blend two colors with given factor."""
        # Simple color blending (could be improved)
        if factor <= 0:
            return color2
        if factor >= 1:
            return color1
        
        # For simplicity, return color1 with some transparency effect
        # In a full implementation, this would do proper RGB blending
        return color1
    
    def start(self):
        """Start the spinning animation."""
        if not self.animation_running:
            self.animation_running = True
            self.animation_thread = threading.Thread(target=self._animate, daemon=True)
            self.animation_thread.start()
    
    def stop(self):
        """Stop the spinning animation."""
        self.animation_running = False
    
    def _animate(self):
        """Animation loop for spinning."""
        while self.animation_running:
            self.angle = (self.angle + self.speed) % 360
            
            try:
                self.canvas.after_idle(self._draw_spinner)
                time.sleep(0.03)  # ~30 FPS
            except:
                break
    
    def destroy(self):
        """Clean up the spinner."""
        self.stop()
        self.canvas.destroy()


class PulsingDots:
    """Pulsing dots loader animation."""
    
    def __init__(self, parent, dots=3, size=8, color="#00A8FF", spacing=15):
        self.parent = parent
        self.dots = dots
        self.size = size
        self.color = color
        self.spacing = spacing
        
        # Calculate total width
        total_width = (dots * size) + ((dots - 1) * spacing)
        
        # Create canvas
        self.canvas = tk.Canvas(parent, width=total_width, height=size * 2,
                               highlightthickness=0, relief='flat', bg='white')
        self.canvas.pack()
        
        # Animation state
        self.phase = 0
        self.animation_running = False
        self.animation_thread = None
    
    def _draw_dots(self):
        """Draw the pulsing dots."""
        self.canvas.delete("all")
        
        for i in range(self.dots):
            # Calculate position
            x = i * (self.size + self.spacing) + self.size // 2
            y = self.size
            
            # Calculate pulse phase for this dot
            dot_phase = (self.phase + (i * 60)) % 360
            
            # Calculate scale based on sine wave
            scale = 0.5 + 0.5 * math.sin(math.radians(dot_phase))
            current_size = self.size * (0.4 + 0.6 * scale)
            
            # Calculate alpha (opacity simulation)
            alpha = 0.3 + 0.7 * scale
            
            # Draw dot (circle)
            radius = current_size // 2
            color = self._alpha_color(self.color, alpha)
            
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                  fill=color, outline="")
    
    def _alpha_color(self, color: str, alpha: float) -> str:
        """Simulate alpha by blending with white background."""
        # Simple alpha simulation - could be improved with proper color math
        if alpha >= 1.0:
            return color
        if alpha <= 0.0:
            return "#FFFFFF"
        
        # For simplicity, return the original color
        # In a full implementation, this would blend with background
        return color
    
    def start(self):
        """Start the pulsing animation."""
        if not self.animation_running:
            self.animation_running = True
            self.animation_thread = threading.Thread(target=self._animate, daemon=True)
            self.animation_thread.start()
    
    def stop(self):
        """Stop the pulsing animation."""
        self.animation_running = False
    
    def _animate(self):
        """Animation loop for pulsing."""
        while self.animation_running:
            self.phase = (self.phase + 6) % 360
            
            try:
                self.canvas.after_idle(self._draw_dots)
                time.sleep(0.05)  # ~20 FPS
            except:
                break
    
    def destroy(self):
        """Clean up the dots."""
        self.stop()
        self.canvas.destroy()


class LoadingOverlay:
    """Modern loading overlay with blur effect simulation."""
    
    def __init__(self, parent, text="Loading...", loader_type="spinner"):
        self.parent = parent
        self.text = text
        self.loader_type = loader_type
        
        # Create overlay frame
        self.overlay = tk.Toplevel(parent)
        self.overlay.overrideredirect(True)  # Remove window decorations
        self.overlay.configure(bg='#F0F0F0')
        self.overlay.attributes('-alpha', 0.95)  # Slight transparency
        
        # Position overlay over parent
        self._position_overlay()
        
        # Create content frame
        content_frame = tk.Frame(self.overlay, bg='white', relief='raised', bd=2)
        content_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Add shadow effect (simple border)
        shadow_frame = tk.Frame(content_frame, bg='#E0E0E0', height=2)
        shadow_frame.pack(fill='x', side='bottom')
        
        # Create loader based on type
        loader_frame = tk.Frame(content_frame, bg='white')
        loader_frame.pack(expand=True)
        
        if loader_type == "spinner":
            self.loader = SpinningLoader(loader_frame, size=48, color="#00A8FF")
        elif loader_type == "dots":
            self.loader = PulsingDots(loader_frame, dots=3, size=12, color="#00A8FF")
        elif loader_type == "radial":
            self.loader = HorizontalPulseLoader(loader_frame, size=64, color="#00A8FF")
        else:  # progress bar
            self.loader = ModernProgressBar(loader_frame, width=200, height=6)
            self.loader.start_indeterminate()
        
        # Add text
        text_label = tk.Label(content_frame, text=text, bg='white', 
                             font=('Segoe UI', 10), fg='#333333')
        text_label.pack(pady=(10, 0))
        
        # Start animation
        if hasattr(self.loader, 'start'):
            self.loader.start()
    
    def _position_overlay(self):
        """Position overlay to cover parent window."""
        self.parent.update_idletasks()
        
        # Get parent geometry
        x = self.parent.winfo_rootx()
        y = self.parent.winfo_rooty()
        width = self.parent.winfo_width()
        height = self.parent.winfo_height()
        
        # Set overlay geometry
        self.overlay.geometry(f"{width}x{height}+{x}+{y}")
    
    def update_text(self, text: str):
        """Update the loading text."""
        self.text = text
        # Find and update text label
        for widget in self.overlay.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label):
                        child.config(text=text)
    
    def set_progress(self, value: float):
        """Set progress if using progress bar loader."""
        if isinstance(self.loader, ModernProgressBar):
            self.loader.set_progress(value)
    
    def close(self):
        """Close the loading overlay."""
        if hasattr(self.loader, 'stop'):
            self.loader.stop()
        elif hasattr(self.loader, 'destroy'):
            self.loader.destroy()
        
        try:
            self.overlay.destroy()
        except:
            pass


# Utility function for easy use
def show_loading(parent, text="Loading...", loader_type="spinner") -> LoadingOverlay:
    """Show a loading overlay. Returns LoadingOverlay instance to control it."""
    return LoadingOverlay(parent, text, loader_type)


if __name__ == "__main__":
    # Demo application
    def test_loaders():
        import tkinter as tk
        
        root = tk.Tk()
        root.title("Modern Loading Animations Demo")
        root.geometry("600x400")
        
        # Test different loaders
        frame1 = tk.LabelFrame(root, text="Progress Bar", padx=10, pady=10)
        frame1.pack(fill='x', padx=10, pady=5)
        
        progress = ModernProgressBar(frame1, width=300, color="#00A8FF")
        
        frame2 = tk.LabelFrame(root, text="Spinning Loader", padx=10, pady=10)
        frame2.pack(fill='x', padx=10, pady=5)
        
        spinner = SpinningLoader(frame2, size=48, color="#FF6B6B")
        
        frame3 = tk.LabelFrame(root, text="Pulsing Dots", padx=10, pady=10)
        frame3.pack(fill='x', padx=10, pady=5)
        
        dots = PulsingDots(frame3, dots=4, size=16, color="#4ECDC4")
        
        frame4 = tk.LabelFrame(root, text="Horizontal Pulse Loader", padx=10, pady=10)
        frame4.pack(fill='x', padx=10, pady=5)
        
        horizontal = HorizontalPulseLoader(frame4, size=64, color="#9B59B6", pulse_duration=1.0)
        
        # Control buttons
        control_frame = tk.Frame(root)
        control_frame.pack(pady=20)
        
        def start_animations():
            progress.start_indeterminate()
            spinner.start()
            dots.start()
            horizontal.start()
        
        def stop_animations():
            progress.stop_indeterminate()
            spinner.stop()
            dots.stop()
            horizontal.stop()
        
        def show_overlay():
            overlay = show_loading(root, "Processing data with horizontal pulse...", "radial")
            root.after(3000, overlay.close)  # Auto-close after 3 seconds
        
        tk.Button(control_frame, text="Start Animations", command=start_animations).pack(side='left', padx=5)
        tk.Button(control_frame, text="Stop Animations", command=stop_animations).pack(side='left', padx=5)
        tk.Button(control_frame, text="Show Overlay", command=show_overlay).pack(side='left', padx=5)
        
        root.mainloop()
    
    test_loaders()