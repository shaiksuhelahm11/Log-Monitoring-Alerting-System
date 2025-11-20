# Log Monitoring & Alerting System

A Python-based monitoring tool that scans application logs, detects error patterns, and generates alerts. 
Built for DevOps-style troubleshooting and automated detection of failures.

## Features
- Real-time log monitoring (tail-like behavior)
- Regex-based pattern detection
- Threshold + time-window alert rules
- Console, Slack, and Email alert options
- YAML-based configuration (no code changes needed)
- Docker + systemd support

# How It Works
- monitor.py tails the configured log file.
- Each new log line is checked against rules in config.yaml.
- If a pattern appears X times within Y seconds, an alert is triggered.
- Alerts are printed to the console (default) or sent to Slack/Email.

### Setup
- pip install -r requirements.txt
- python monitor.py

### Run with Docker (Optional)
- docker build -t log-monitor .
- docker run -v /var/log:/logs log-monitor
