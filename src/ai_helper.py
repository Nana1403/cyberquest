CYBER_MENTOR_ANSWERS = {
    "sql": "SQL Injection happens when unsafe user input changes a database query. Developers prevent it with parameterized queries.",
    "password": "Strong passwords are long, hard to guess, and not reused. A password manager can help create and store them.",
    "phishing": "Phishing is a trick that tries to make people click links, open files, or share private information.",
    "port": "A port is like a door into a computer service. For example, port 80 is often used for web traffic.",
    "log": "Logs are records of computer events. Security teams use them to find suspicious behavior.",
    "hash": "A hash turns data into a fixed fingerprint. Hashing is one way, so it is not the same as encryption.",
    "encryption": "Encryption protects information by making it unreadable without the correct key.",
    "ethics": "Ethical hackers only test systems when they have permission and they report problems responsibly.",
}


def ask_mentor(question):
    clean_question = question.lower()

    for keyword, answer in CYBER_MENTOR_ANSWERS.items():
        if keyword in clean_question:
            return answer

    return "I can help with passwords, phishing, ports, logs, hashes, encryption, SQL injection, and ethics."
