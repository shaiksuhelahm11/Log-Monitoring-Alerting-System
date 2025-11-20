def send_alert(count, lines):
    print("\n====== ALERT TRIGGERED ======")
    print(f"{count} error(s) detected!")
    print("Recent Error Logs:")
    for line in lines[-5:]:  # Show last 5 errors
        print("-", line)
    print("=============================\n")
