import os
import datetime

class ChatLogger:
    def __init__(self, log_dir: str = "logs"):
        os.makedirs(log_dir, exist_ok=True)
        date_str = datetime.date.today().isoformat()
        self.path = os.path.join(log_dir, f"chat_{date_str}.txt")

    def log(self, role: str, content: str):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {role.upper()}: {content}\n")