USERS = {
    "Admin": {"integrity": "High"},
    "Bob": {"integrity": "Low"}
}

FILES = {
    "security_log.txt": {"integrity": "High"}
}

INTEGRITY = {"Low": 1, "Medium": 2, "High": 3}

# Security log Function
def add_log_event(user_id, event_data):
    with open("security_log.txt", "a") as log:
        log.write(f"User: {user_id}, File: {event_data["file"]}, Action: {event_data["action"]}, Status: {event_data["status"]}")
    
# Security Check Function
def check_access(user_id, file, action):
    user_integrity = INTEGRITY.get(USERS[user_id]["integrity"], 1)
    file_integrity = INTEGRITY.get(FILES[file]["integrity"], 1)

    if user_integrity >= file_integrity:
        return True
    else:
        add_log_event(user_id, {"file": file, "action": action, "status": "Denied"})
        return False

# Log Reading Function
def read_logs(user_id):
    user_integrity = INTEGRITY.get(USERS[user_id]["integrity"], 1)
    logs_integrity = INTEGRITY.get(FILES["security_log.txt"]["integrity"], 3)

    if user_integrity >= logs_integrity:
        print("Access Granted!")
        with open("security_log.txt", "r") as log:
            print(log.read())
        return True
    else:
        add_log_event(user_id, {"file": "security_log.txt", "action": "read", "status": "Denied"})
        return False