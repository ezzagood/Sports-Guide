import json
import datetime
import urllib.request

def fetch_sports_data():
    today = datetime.datetime.now(datetime.timezone.utc)
    
    # 3-day rolling schedule structure
    days_data = []
    
    # Sample fallback/live structure for Australian sports broadcasters
    channels = ["Kayo / Fox Sports", "Stan Sport", "ESPN", "beIN Sports", "Optus Sport"]
    sample_events = [
        {"time": "14:00 AEST", "sport": "Motorsport", "event": "Supercars Bathurst 1000", "channel": "Kayo / Fox Sports"},
        {"time": "16:30 AEST", "sport": "Basketball", "event": "NBL: Sydney Kings vs Melbourne United", "channel": "Kayo / Fox Sports"},
        {"time": "18:00 AEST", "sport": "Football", "event": "Premier League Matchday Live", "channel": "Optus Sport"},
        {"time": "20:15 AEST", "sport": "Rugby Union", "event": "The Rugby Championship", "channel": "Stan Sport"},
        {"time": "22:00 AEST", "sport": "Tennis", "event": "ATP Tour Match", "channel": "beIN Sports"},
        {"time": "08:00 AEST", "sport": "Baseball", "event": "MLB Regular Season", "channel": "ESPN"}
    ]
    
    for i in range(3):
        day_date = today + datetime.timedelta(days=i)
        day_name = day_date.strftime("%A, %b %d")
        
        days_data.append({
            "date": day_name,
            "events": sample_events[i % len(sample_events):] + sample_events[:i % len(sample_events)]
        })

    schedule = {
        "last_updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "days": days_data
    }

    # Save to schedule.json
    with open("schedule.json", "w") as f:
        json.dump(schedule, f, indent=2)

    print("schedule.json generated successfully!")

if __name__ == "__main__":
    fetch_sports_data()
