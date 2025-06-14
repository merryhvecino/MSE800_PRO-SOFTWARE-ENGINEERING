import datetime

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def build_log_entry(event_type, user_id, message, timestamp):
    return f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"

def save_log(entry, filepath="rental_log.txt"):
    with open(filepath, "a") as file:
        file.write(entry)

def log_event(event_type, user_id, message):
    timestamp = get_timestamp()
    entry = build_log_entry(event_type, user_id, message, timestamp)
    save_log(entry)
