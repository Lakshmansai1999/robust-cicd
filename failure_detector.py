import sys

def classify_failure(log_text):
    log_text = log_text.lower()

    if "exception" in log_text:
        return "Application Code Issue"
    elif "jenkinsfile" in log_text:
        return "Pipeline Configuration Issue"
    elif "connection refused" in log_text:
        return "Infrastructure Issue"
    elif "docker" in log_text or "container" in log_text:
        return "Docker/Agent Issue"
    else:
        return "Unknown Issue"

if __name__ == "__main__":
    logs = sys.stdin.read()
    print(classify_failure(logs))
