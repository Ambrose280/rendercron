import schedule
import time
import requests

def visit_url():
    try:
        response = requests.get("https://zigbot.onrender.com")
        response.raise_for_status()
        print(f"Visited URL successfully at {time.ctime()}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit URL: {e}")

# Schedule the job every 4 minutes
schedule.every(4).minutes.do(visit_url)

print("Worker started, visiting https://zigbot.onrender.com every 4 minutes")

while True:
    schedule.run_pending()
    time.sleep(1)
