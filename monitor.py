import re
from datetime import datetime
from alert import send_alert

LOG_FILE = "logs/app.log"

ERROR_PATTERNS = [
    r"ERROR",
    r"FAIL",
    r"EXCEPTION",
    r"CRITICAL",
    r"WARNING"
]

def scan_logs():
    with open(LOG_FILE, "r") as file:
        lines = file.readlines()

    error_count = 0
    error_lines = []

    for line in lines:
        for pattern in ERROR_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                error_count += 1
                error_lines.append(line.strip())

    print(f"[{datetime.now()}] Errors detected: {error_count}")

    if error_count > 0:
        send_alert(error_count, error_lines)

if __name__ == "__main__":
    scan_logs()
