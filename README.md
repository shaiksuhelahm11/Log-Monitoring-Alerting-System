# Log Monitoring & Alerting System

A Python-based monitoring tool that scans application logs, detects error patterns, and generates alerts. 
Built for DevOps-style troubleshooting and automated detection of failures.

##  Features
- Scans log files for ERROR, FAIL, WARNING, CRITICAL patterns  
- Regex-based pattern matching  
- Console-based alerts (extendable to Slack/email)  
- Lightweight and suitable for cron scheduling  
- Simple modular structure  

## Folder Structure
log-monitor/
│── logs/
│   └── app.log  
│── monitor.py  
│── alert.py  
│── README.md  
│── requirements.txt

## Future Enhancements
- Slack / Email alerts  
- Integration with CloudWatch logs  
- Log rotation handling  
- Export report to database  
