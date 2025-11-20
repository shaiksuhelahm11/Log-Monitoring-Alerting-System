import yaml
import time
import os
from rule_engine import RuleEngine
from alert import AlertManager

def tail(path):
    with open(path, "r") as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if line:
                yield line.strip()
            time.sleep(0.2)

def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    engine = RuleEngine(config["rules"])
    alerts = AlertManager(config)

    print("Log Monitoring Started...")

    for line in tail(config["log_file"]):
        rules_triggered = engine.evaluate(line)

        for rule in rules_triggered:
            alerts.notify(rule, line)

if __name__ == "__main__":
    main()
