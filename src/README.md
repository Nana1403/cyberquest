# CyberQuest - Ethical Hacking Simulator

CyberQuest is a beginner-friendly cybersecurity training app made with Python, Tkinter, and Pydantic.

Students complete safe simulated missions instead of attacking real computers. The goal is to learn cybersecurity concepts, ethics, and defensive thinking.

## Features

- Virtual hacking lab with simulated systems
- Weak password audit
- Phishing email detector
- Safe network scanner simulation
- Vulnerability hunt
- Log investigator
- Digital forensics challenge
- Encryption lab with Caesar cipher, Vigenere cipher, and SHA-256 hashing
- Simple AI Cyber Mentor
- XP, badges, levels, and a dashboard

## Project Structure

```text
cyberquest/
├── main.py
├── gui.py
├── models.py
├── missions.py
├── ai_helper.py
├── scoring.py
├── data/
│   ├── emails.json
│   ├── logs.json
│   ├── passwords.json
│   └── vulnerabilities.json
├── assets/
│   ├── icons/
│   └── images/
├── requirements.txt
└── README.md
```

## How To Run

Install the requirement:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python main.py
```

## Safety Note

This app does not scan real networks, attack real systems, or collect real credentials. Everything is simulated for learning.

## Beginner Notes

The code is written in a simple style on purpose. Most functions have clear names, and the app avoids complicated patterns so students can read and edit it.

## Future Improvements

- Add student login so each student can save their own progress.
- Save XP, badges, and completed missions to a file.
- Add more missions about secure coding, malware awareness, and incident response.
- Add more realistic fake logs for students to investigate.
- Add a quiz mode after each mission.
- Add sound effects or animations when students earn badges.
- Add teacher mode so an instructor can view class progress.
- Add difficulty levels for beginner, intermediate, and advanced students.
- Add more cryptography examples, such as RSA demonstrations.
- Add printable certificates when students complete all missions.

## Add-ons

### Real OpenAI Cyber Mentor

A future add-on could connect the AI Cyber Mentor to the real OpenAI API. Instead of only using the small local answer list in `ai_helper.py`, the app could send student questions to an OpenAI model and show a custom explanation.

Example idea:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input="Explain phishing to a beginner cybersecurity student."
)

print(response.output_text)
```

This add-on would need:

- An OpenAI API key stored safely as an environment variable.
- The `openai` Python package installed.
- Safety rules in the prompt so the mentor teaches ethical hacking only.
- A fallback to the local mentor if the internet or API key is not available.

### Other Add-on Ideas

- Leaderboard for friendly classroom competition.
- More badge types and level names.
- Export progress as a text file or CSV file.
- Add image icons for servers, firewalls, and computers.
- Add a mission editor so students can create their own safe challenges.
