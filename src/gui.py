import tkinter as tk
from tkinter import messagebox, ttk

from ai_helper import ask_mentor
from missions import (
    MISSIONS,
    caesar_decrypt,
    caesar_encrypt,
    get_emails,
    get_logs,
    get_passwords,
    get_vulnerabilities,
    sha_hash,
    simulated_scan,
    vigenere_encrypt,
)
from models import Student
from scoring import add_reward, get_level_name, get_success_rate, record_answer


class CyberQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberQuest - Ethical Hacking Simulator")
        self.root.geometry("1050x700")
        self.root.configure(bg="#101820")

        self.student = Student(username="Student")
        self.selected_system = "Web Server"
        self.passwords = get_passwords()
        self.emails = get_emails()
        self.email_index = 0

        self.colors = {
            "bg": "#101820",
            "panel": "#1d2b34",
            "button": "#2d6a4f",
            "button2": "#3a86ff",
            "text": "#f4f7f5",
            "accent": "#00d084",
            "warning": "#ffbe0b",
        }
        self.font_name = "Courier New"

        self.make_layout()
        self.show_dashboard()

    def make_layout(self):
        title = tk.Label(
            self.root,
            text="CyberQuest",
            font=(self.font_name, 26, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["accent"],
        )
        title.pack(pady=10)

        self.main_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.main_frame.pack(fill="both", expand=True, padx=12, pady=8)

        self.menu_frame = tk.Frame(self.main_frame, bg=self.colors["panel"], width=220)
        self.menu_frame.pack(side="left", fill="y", padx=(0, 10))

        self.content_frame = tk.Frame(self.main_frame, bg=self.colors["panel"])
        self.content_frame.pack(side="left", fill="both", expand=True)

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Virtual Lab", self.show_lab),
            ("Password Audit", self.show_password_mission),
            ("Phishing Detector", self.show_phishing_mission),
            ("Network Scanner", self.show_scanner_mission),
            ("Vulnerability Hunt", self.show_vulnerability_mission),
            ("Log Investigator", self.show_log_mission),
            ("Digital Forensics", self.show_forensics_mission),
            ("Encryption Lab", self.show_crypto_mission),
            ("AI Cyber Mentor", self.show_ai_mentor),
            ("Ethics", self.show_ethics),
        ]

        for text, command in buttons:
            button = tk.Button(
                self.menu_frame,
                text=text,
                command=command,
                bg=self.colors["button"],
                fg="black",
                font=(self.font_name, 11),
                width=20,
                relief="raised",
                pady=8,
            )
            button.pack(pady=5, padx=10)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def add_heading(self, text):
        label = tk.Label(
            self.content_frame,
            text=text,
            bg=self.colors["panel"],
            fg=self.colors["accent"],
            font=(self.font_name, 20, "bold"),
        )
        label.pack(pady=12)

    def add_text(self, text, size=12):
        label = tk.Label(
            self.content_frame,
            text=text,
            bg=self.colors["panel"],
            fg=self.colors["text"],
            font=(self.font_name, size),
            justify="left",
            wraplength=720,
        )
        label.pack(pady=6, padx=20, anchor="w")
        return label

    def add_button(self, text, command, color=None):
        if color is None:
            color = self.colors["button2"]

        button = tk.Button(
            self.content_frame,
            text=text,
            command=command,
            bg=color,
            fg="black",
            font=(self.font_name, 11),
            relief="raised",
            padx=12,
            pady=8,
        )
        button.pack(pady=6)
        return button

    def reward_mission(self, mission_key):
        mission = MISSIONS[mission_key]
        before_xp = self.student.xp
        add_reward(self.student, mission)

        if self.student.xp > before_xp:
            messagebox.showinfo(
                "Mission Complete",
                f"+{mission.xp_reward} XP\nBadge earned: {mission.badge}",
            )
        else:
            messagebox.showinfo("Already Complete", "You already earned this mission reward.")

    def show_dashboard(self):
        self.clear_content()
        self.add_heading("Student Dashboard")

        level_name = get_level_name(self.student.xp)
        success_rate = get_success_rate(self.student)

        self.add_text(f"Username: {self.student.username}", 14)
        self.add_text(f"Current Level: {level_name}", 14)
        self.add_text(f"XP Earned: {self.student.xp}", 14)
        self.add_text(f"Completed Missions: {len(self.student.completed_missions)}", 14)
        self.add_text(f"Success Rate: {success_rate}%", 14)

        progress = ttk.Progressbar(self.content_frame, length=500, maximum=700)
        progress["value"] = self.student.xp
        progress.pack(pady=10)

        badges = ", ".join(self.student.badges)
        if badges == "":
            badges = "No badges yet. Complete missions to earn badges."

        self.add_text("Badges: " + badges, 13)

    def show_lab(self):
        self.clear_content()
        self.add_heading("Virtual Hacking Lab")
        self.add_text("Click a simulated system to investigate it. No real computers are scanned.")

        systems = ["Web Server", "Database Server", "Email Server", "Employee Computer", "Firewall"]

        lab_frame = tk.Frame(self.content_frame, bg=self.colors["panel"])
        lab_frame.pack(pady=20)

        for system in systems:
            button = tk.Button(
                lab_frame,
                text=system,
                width=20,
                height=3,
                bg="#243b4a",
                fg="black",
                font=(self.font_name, 11),
                relief="raised",
                command=lambda name=system: self.select_system(name),
            )
            button.pack(side="left", padx=8)

        self.system_label = self.add_text(f"Selected system: {self.selected_system}", 14)

    def select_system(self, system_name):
        self.selected_system = system_name
        self.system_label.config(text=f"Selected system: {self.selected_system}")

    def show_password_mission(self):
        self.clear_content()
        self.add_heading("Mission 1: Weak Password Audit")
        self.add_text("Choose which passwords are weak. Then read the explanation.")

        for item in self.passwords:
            password = item["password"]
            button = tk.Button(
                self.content_frame,
                text=password,
                width=25,
                bg="#243b4a",
                fg="black",
                font=(self.font_name, 11),
                relief="raised",
                command=lambda chosen=item: self.check_password(chosen),
            )
            button.pack(pady=5)

        self.add_button("Finish Mission", lambda: self.reward_mission("password"))

    def check_password(self, item):
        record_answer(self.student, True)
        strength = "Weak" if item["is_weak"] else "Stronger"
        messagebox.showinfo(strength + " Password", item["reason"])

    def show_phishing_mission(self):
        self.clear_content()
        self.add_heading("Mission 2: Phishing Detector")

        email = self.emails[self.email_index]
        self.add_text("Subject: " + email["subject"], 14)
        self.add_text("From: " + email["sender"], 13)
        self.add_text("Message: " + email["body"], 13)

        self.add_button("Safe", lambda: self.check_email(False))
        self.add_button("Phishing", lambda: self.check_email(True), self.colors["warning"])
        self.add_button("Finish Mission", lambda: self.reward_mission("phishing"))

    def check_email(self, guessed_phishing):
        email = self.emails[self.email_index]
        was_correct = guessed_phishing == email["is_phishing"]
        record_answer(self.student, was_correct)

        if was_correct:
            title = "Correct"
        else:
            title = "Try Again"

        messagebox.showinfo(title, email["reason"])

        self.email_index = (self.email_index + 1) % len(self.emails)
        self.show_phishing_mission()

    def show_scanner_mission(self):
        self.clear_content()
        self.add_heading("Mission 3: Network Scanner")
        self.add_text(f"Selected target: {self.selected_system}")
        self.add_button("Run Safe Simulated Scan", self.run_scan)
        self.add_button("Finish Mission", lambda: self.reward_mission("scanner"))

    def run_scan(self):
        results = simulated_scan(self.selected_system)
        output = "Scanning...\n\n" + "\n".join(results)
        messagebox.showinfo("Scan Results", output)

    def show_vulnerability_mission(self):
        self.clear_content()
        self.add_heading("Mission 4: Vulnerability Hunt")
        self.add_text("Inspect each issue and choose a mitigation step.")

        for item in get_vulnerabilities():
            text = item["system"] + ": " + item["issue"]
            button = tk.Button(
                self.content_frame,
                text=text,
                width=45,
                bg="#243b4a",
                fg="black",
                font=(self.font_name, 11),
                relief="raised",
                command=lambda chosen=item: self.show_fix(chosen),
            )
            button.pack(pady=5)

        self.add_button("Finish Mission", lambda: self.reward_mission("vulnerabilities"))

    def show_fix(self, item):
        record_answer(self.student, True)
        messagebox.showinfo("Mitigation", item["fix"])

    def show_log_mission(self):
        self.clear_content()
        self.add_heading("Mission 5: Log Investigator")
        self.add_text("Read the fake logs and decide if the activity is suspicious.")

        log_box = tk.Text(
            self.content_frame,
            width=85,
            height=10,
            bg="#0b1117",
            fg=self.colors["accent"],
            font=(self.font_name, 11),
        )
        log_box.pack(pady=10)

        for line in get_logs():
            log_box.insert("end", line + "\n")

        log_box.config(state="disabled")

        self.add_button("Suspicious", lambda: self.check_logs(True), self.colors["warning"])
        self.add_button("Not Suspicious", lambda: self.check_logs(False))
        self.add_button("Finish Mission", lambda: self.reward_mission("logs"))

    def check_logs(self, answer):
        record_answer(self.student, answer is True)

        if answer:
            messagebox.showinfo("Correct", "Several failed admin logins followed by a success is suspicious.")
        else:
            messagebox.showinfo("Look Closer", "Repeated failed logins can be a sign of brute-force activity.")

    def show_forensics_mission(self):
        self.clear_content()
        self.add_heading("Mission 6: Digital Forensics")
        self.add_text("Incident clues:")
        self.add_text("1. Three failed admin logins happened in a row.")
        self.add_text("2. Admin login succeeded from an unknown device.")
        self.add_text("3. A firewall rule was changed soon after.")
        self.add_text("What most likely happened?")

        self.add_button("Normal software update", lambda: self.check_forensics(False))
        self.add_button("Possible account compromise", lambda: self.check_forensics(True), self.colors["warning"])
        self.add_button("Printer error", lambda: self.check_forensics(False))
        self.add_button("Finish Mission", lambda: self.reward_mission("forensics"))

    def check_forensics(self, was_correct):
        record_answer(self.student, was_correct)

        if was_correct:
            messagebox.showinfo("Correct", "The evidence suggests someone may have guessed or stolen the admin password.")
        else:
            messagebox.showinfo("Try Again", "The login pattern and firewall change point to a security incident.")

    def show_crypto_mission(self):
        self.clear_content()
        self.add_heading("Mission 7: Encryption Lab")

        self.add_text("Plain text:")
        self.crypto_entry = tk.Entry(self.content_frame, width=55)
        self.crypto_entry.config(font=(self.font_name, 11))
        self.crypto_entry.insert(0, "cyber quest")
        self.crypto_entry.pack(pady=5)

        self.add_text("Key or shift:")
        self.key_entry = tk.Entry(self.content_frame, width=20)
        self.key_entry.config(font=(self.font_name, 11))
        self.key_entry.insert(0, "3")
        self.key_entry.pack(pady=5)

        self.crypto_output = tk.Text(
            self.content_frame,
            width=80,
            height=8,
            bg="#0b1117",
            fg=self.colors["accent"],
            font=(self.font_name, 11),
        )
        self.crypto_output.pack(pady=10)

        self.add_button("Caesar Cipher", self.run_caesar)
        self.add_button("Vigenere Cipher", self.run_vigenere)
        self.add_button("SHA-256 Hash", self.run_hash)
        self.add_button("Finish Mission", lambda: self.reward_mission("crypto"))

    def run_caesar(self):
        text = self.crypto_entry.get()

        try:
            shift = int(self.key_entry.get())
        except ValueError:
            shift = 3

        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        self.show_crypto_output(encrypted, decrypted)

    def run_vigenere(self):
        text = self.crypto_entry.get()
        key = self.key_entry.get()

        if key.isnumeric():
            key = "key"

        encrypted = vigenere_encrypt(text, key)
        self.show_crypto_output(encrypted, "Vigenere decrypt is not shown in this beginner demo.")

    def run_hash(self):
        text = self.crypto_entry.get()
        encrypted = sha_hash(text)
        self.show_crypto_output(encrypted, "Hashes are one way, so they are not decrypted.")

    def show_crypto_output(self, encrypted, decrypted):
        self.crypto_output.delete("1.0", "end")
        self.crypto_output.insert("end", "Plain Text\n")
        self.crypto_output.insert("end", self.crypto_entry.get() + "\n\n")
        self.crypto_output.insert("end", "Encrypted Text\n")
        self.crypto_output.insert("end", encrypted + "\n\n")
        self.crypto_output.insert("end", "Decrypted Text\n")
        self.crypto_output.insert("end", decrypted + "\n")

    def show_ai_mentor(self):
        self.clear_content()
        self.add_heading("AI Cyber Mentor")
        self.add_text("Ask a cybersecurity question. This simple mentor uses local beginner answers.")

        self.mentor_entry = tk.Entry(self.content_frame, width=70)
        self.mentor_entry.config(font=(self.font_name, 11))
        self.mentor_entry.insert(0, "What is SQL Injection?")
        self.mentor_entry.pack(pady=10)

        self.mentor_answer = tk.Label(
            self.content_frame,
            text="",
            bg=self.colors["panel"],
            fg=self.colors["text"],
            wraplength=700,
            justify="left",
            font=(self.font_name, 13),
        )
        self.mentor_answer.pack(pady=10, padx=20)

        self.add_button("Ask Mentor", self.answer_question)

    def answer_question(self):
        question = self.mentor_entry.get()
        answer = ask_mentor(question)
        self.mentor_answer.config(text=answer)

    def show_ethics(self):
        self.clear_content()
        self.add_heading("Cybersecurity Ethics")
        self.add_text("Ethical hacking means learning safely and helping people protect systems.")
        self.add_text("Always get permission before testing a system.")
        self.add_text("Never steal data, damage systems, or attack real computers.")
        self.add_text("Report security problems responsibly.")


def start_app():
    root = tk.Tk()
    app = CyberQuestApp(root)
    root.mainloop()
