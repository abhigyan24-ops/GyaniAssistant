import customtkinter as ctk
import threading
import os
import time

# Import pipeline components
from Listen import Listen
from brain import get_brain_response
from Speak import speak

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GyaniApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gyani Voice Assistant")
        self.geometry("1000x700")
        self.minsize(800, 600)

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._create_sidebar()
        self._create_main_area()

    def _create_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Gyani Assistant", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Action Buttons
        self.btn_news = ctk.CTkButton(self.sidebar_frame, text="News", command=lambda: self.run_script("Tell_News.py"))
        self.btn_news.grid(row=1, column=0, padx=20, pady=10)

        self.btn_joke = ctk.CTkButton(self.sidebar_frame, text="Joke", command=lambda: self.run_script("Joke.py"))
        self.btn_joke.grid(row=2, column=0, padx=20, pady=10)

        self.btn_weather = ctk.CTkButton(self.sidebar_frame, text="Weather", command=lambda: self.run_script("Temperature.py"))
        self.btn_weather.grid(row=3, column=0, padx=20, pady=10)

        self.btn_speed = ctk.CTkButton(self.sidebar_frame, text="Speed Test", command=lambda: self.run_script("speed_test.py"))
        self.btn_speed.grid(row=4, column=0, padx=20, pady=10)

        self.btn_spotify = ctk.CTkButton(self.sidebar_frame, text="Spotify", command=lambda: self.run_script("spotify.py"))
        self.btn_spotify.grid(row=5, column=0, padx=20, pady=10)

        self.btn_reminder = ctk.CTkButton(self.sidebar_frame, text="Set Reminder", command=lambda: self.run_script("SetReaminder.py"))
        self.btn_reminder.grid(row=6, column=0, padx=20, pady=10)

        # Appearance Mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

    def _create_main_area(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Top Bar
        self.top_bar = ctk.CTkFrame(self.main_frame, height=50, fg_color="transparent")
        self.top_bar.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        self.top_bar.grid_columnconfigure(0, weight=1)
        
        self.btn_logs = ctk.CTkButton(self.top_bar, text="View Chat Log", command=self.open_logs)
        self.btn_logs.grid(row=0, column=1, sticky="e")

        # Chat Area
        self.chat_area = ctk.CTkTextbox(self.main_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.chat_area.grid(row=1, column=0, sticky="nsew")
        self.chat_area.configure(state="disabled")
        
        # Configure tags for colors
        # Since customTkinter exposes the underlying tk text widget:
        self.chat_area._textbox.tag_config("user", foreground="#4da6ff")  # Light Blue
        self.chat_area._textbox.tag_config("gyani", foreground="#ff9933") # Orange

        # Bottom Area
        self.bottom_area = ctk.CTkFrame(self.main_frame, height=150, fg_color="transparent")
        self.bottom_area.grid(row=2, column=0, sticky="ew", pady=(20, 0))
        self.bottom_area.grid_columnconfigure(0, weight=1)

        # Mic Button
        self.mic_btn = ctk.CTkButton(
            self.bottom_area, 
            text="🎙️", 
            font=ctk.CTkFont(size=40),
            width=100, height=100, 
            corner_radius=50,
            fg_color="#28a745", # Green when idle
            hover_color="#218838",
            command=self.start_voice_pipeline
        )
        self.mic_btn.grid(row=0, column=0, pady=10)

        # Status Label
        self.status_label = ctk.CTkLabel(self.bottom_area, text="Idle", font=ctk.CTkFont(size=16, weight="bold"))
        self.status_label.grid(row=1, column=0)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def open_logs(self):
        if os.path.exists("chatlogs.txt"):
            os.startfile("chatlogs.txt")
        else:
            self.append_chat("System", "Chat logs file not found.")

    def run_script(self, script_name):
        def script_thread():
            self.update_status(f"Running {script_name}...", "#17a2b8")
            try:
                os.system(f"python {script_name}")
            except Exception as e:
                self.append_chat("System", f"Error running {script_name}: {e}")
            self.update_status("Idle", "#28a745")
        threading.Thread(target=script_thread, daemon=True).start()

    def update_status(self, text, color):
        self.status_label.configure(text=text, text_color=color)
        if text == "Listening...":
            self.mic_btn.configure(fg_color="#dc3545", hover_color="#c82333") # Red
        else:
            self.mic_btn.configure(fg_color="#28a745", hover_color="#218838") # Green
        self.update()

    def append_chat(self, sender, text, tag=None):
        self.chat_area.configure(state="normal")
        self.chat_area.insert("end", f"{sender}: {text}\n\n", tag)
        self.chat_area.see("end")
        self.chat_area.configure(state="disabled")

    def start_voice_pipeline(self):
        # Prevent multiple clicks
        if self.status_label.cget("text") != "Idle":
            return
            
        threading.Thread(target=self.voice_pipeline_thread, daemon=True).start()

    def voice_pipeline_thread(self):
        # 1. Listen
        self.update_status("Listening...", "#dc3545") # Red
        try:
            query = Listen()
        except Exception as e:
            self.append_chat("System", f"Microphone error: {e}")
            self.update_status("Idle", "#28a745")
            return
            
        if not query:
            self.update_status("Idle", "#28a745")
            return
            
        self.append_chat("You", query, "user")
        
        # 2. Brain
        self.update_status("Thinking...", "#ffc107") # Yellow
        response = get_brain_response(query)
        self.append_chat("Gyani", response, "gyani")
        
        # 3. Speak
        self.update_status("Speaking...", "#007bff") # Blue
        speak(response)
        
        self.update_status("Idle", "#28a745") # Back to Green

if __name__ == "__main__":
    app = GyaniApp()
    app.mainloop()