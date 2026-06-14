import hashlib
import json
from pathlib import Path

from models import Mission


DATA_FOLDER = Path(__file__).parent / "data"


def load_json(file_name):
    file_path = DATA_FOLDER / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


MISSIONS = {
    "password": Mission(
        title="Weak Password Audit",
        description="Find weak passwords and learn what makes a password safer.",
        difficulty="Easy",
        xp_reward=50,
        badge="Password Detective",
    ),
    "phishing": Mission(
        title="Phishing Detector",
        description="Read emails and decide if they are safe or phishing.",
        difficulty="Easy",
        xp_reward=50,
        badge="Phishing Spotter",
    ),
    "scanner": Mission(
        title="Network Scanner",
        description="Run a safe simulated scan and study open ports.",
        difficulty="Easy",
        xp_reward=50,
        badge="Network Explorer",
    ),
    "vulnerabilities": Mission(
        title="Vulnerability Hunt",
        description="Find weaknesses in simulated company systems.",
        difficulty="Medium",
        xp_reward=75,
        badge="Vulnerability Hunter",
    ),
    "logs": Mission(
        title="Log Investigator",
        description="Review fake security logs and identify suspicious activity.",
        difficulty="Medium",
        xp_reward=75,
        badge="Log Investigator",
    ),
    "forensics": Mission(
        title="Digital Forensics",
        description="Study clues and decide what happened during an incident.",
        difficulty="Medium",
        xp_reward=100,
        badge="Incident Responder",
    ),
    "crypto": Mission(
        title="Encryption Lab",
        description="Practice Caesar ciphers, Vigenere ciphers, and SHA hashing.",
        difficulty="Easy",
        xp_reward=75,
        badge="Crypto Expert",
    ),
}


def get_passwords():
    return load_json("passwords.json")


def get_emails():
    return load_json("emails.json")


def get_logs():
    return load_json("logs.json")


def get_vulnerabilities():
    return load_json("vulnerabilities.json")


def simulated_scan(system_name):
    scans = {
        "Web Server": ["Port 80 - Open - HTTP", "Port 443 - Open - HTTPS"],
        "Database Server": ["Port 5432 - Open - PostgreSQL", "Port 22 - Open - SSH"],
        "Email Server": ["Port 25 - Open - SMTP", "Port 993 - Open - IMAPS"],
        "Employee Computer": ["Port 3389 - Closed - Remote Desktop", "Port 445 - Open - File Sharing"],
        "Firewall": ["Port 22 - Filtered - SSH", "Port 443 - Open - Admin Panel"],
    }

    return scans.get(system_name, ["No scan data found."])


def caesar_encrypt(text, shift):
    result = ""

    for character in text:
        if character.isalpha():
            start = ord("A") if character.isupper() else ord("a")
            new_letter = chr((ord(character) - start + shift) % 26 + start)
            result = result + new_letter
        else:
            result = result + character

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text, key):
    if key == "":
        return text

    result = ""
    key = key.lower()
    key_index = 0

    for character in text:
        if character.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("a")
            result = result + caesar_encrypt(character, shift)
            key_index = key_index + 1
        else:
            result = result + character

    return result


def sha_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
