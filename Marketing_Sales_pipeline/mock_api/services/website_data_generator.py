import random
from datetime import datetime, timedelta

DEVICES = [
    "Desktop",
    "Mobile",
    "Tablet"
]

CAMPAIGNS = [
    "Summer Sale",
    "Laptop Launch",
    "Monsoon Offer",
    "Winter Collection",
    "Diwali Blast"
]


def random_date():

    return (
        datetime.today() -
        timedelta(days=random.randint(0, 30))
    ).strftime("%Y-%m-%d")


def generate_website_sessions(records=100):

    sessions = []   # ✅ Use a different variable name

    for i in range(records):

        sessions.append({

            "session_id": f"SES{i+1000}",

            "visitor_id": f"VIS{random.randint(1000,9999)}",

            "campaign_name": random.choice(CAMPAIGNS),

            "page_views": random.randint(1,15),

            "session_duration_seconds": random.randint(30,1800),

            "bounce": random.choice([True, False]),

            "device": random.choice(DEVICES),

            "visit_date": random_date()

        })

    return sessions