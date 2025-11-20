import re
import time
from collections import deque

class RuleEngine:
    def __init__(self, rules):
        self.rules = rules
        self.history = {rule["name"]: deque() for rule in rules}

    def evaluate(self, log_line):
        triggered = []
        ts = time.time()

        for rule in self.rules:
            if re.search(rule["pattern"], log_line, re.IGNORECASE):
                buf = self.history[rule["name"]]
                buf.append(ts)

                while buf and ts - buf[0] > rule["time_window_sec"]:
                    buf.popleft()

                if len(buf) >= rule["threshold"]:
                    triggered.append(rule["name"])

        return triggered
