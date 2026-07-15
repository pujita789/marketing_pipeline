import random
from datetime import datetime, timedelta

CAMPAIGNS = [
    "Summer Sale",
    "Laptop Launch",
    "Monsoon Offer",
    "Winter Collection",
    "Diwali Blast",
    "Back To School",
    "Premium Membership"
]


def random_date():

    today = datetime.today()

    days = random.randint(0, 30)

    return (
        today - timedelta(days=days)
    ).strftime("%Y-%m-%d")


def generate_google_campaigns(records=100):

    campaigns = []

    for i in range(records):

        campaigns.append({

            "campaign_id": f"GA{i+1000}",

            "campaign_name": random.choice(CAMPAIGNS),

            "date": random_date(),

            "impressions": random.randint(5000, 100000),

            "clicks": random.randint(100, 5000),

            "spend": round(
                random.uniform(100, 15000),
                2
            ),

            "platform": "Google"

        })

    return campaigns