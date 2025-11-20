import smtplib
from email.mime.text import MIMEText
import requests

class AlertManager:
    def __init__(self, config):
        self.email = config["alerting"].get("email")
        self.slack = config["alerting"].get("slack_webhook")

    def notify(self, rule_name, log_line):
        subject = f"[ALERT] Rule Triggered: {rule_name}"
        body = f"Rule: {rule_name}\nLog Line: {log_line}"

        print(subject)
        print(body)

        if self.email:
            self.send_email(subject, body)

        if self.slack:
            self.send_slack(f"{subject}\n{body}")

    def send_email(self, subject, body):
        try:
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = "monitor@localhost"
            msg["To"] = self.email
            smtplib.SMTP("localhost").sendmail(msg["From"], msg["To"], msg.as_string())
        except:
            print("Email sending failed")

    def send_slack(self, text):
        try:
            requests.post(self.slack, json={"text": text})
        except:
            print("Slack alert failed")
