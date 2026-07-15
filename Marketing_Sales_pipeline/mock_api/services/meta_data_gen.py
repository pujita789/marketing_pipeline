import random
from datetime import datetime, timedelta

CAMPAIGNS = [
    "summer_sale",
    "laptop_launch",
    "monsoon_offer",
    "winter_collection",
    "diwali_blast",
    "back_to_school",
    "premium_membership"
]


def random_date():
    return (
        datetime.now() - timedelta(days=random.randint(0, 30))
    ).strftime("%Y-%m-%d")


def generate_meta_campaigns(records=100):

    campaigns = []

    for i in range(records):

        campaigns.append({

            "campaign_id": f"MA{i+1000}",

            "campaign_name": random.choice(CAMPAIGNS),

            "date": random_date(),

            "impressions": random.randint(5000, 120000),

            "clicks": random.randint(100, 6000),

            "spend": round(
                random.uniform(100, 15000),
                2
            ),

            "platform": "Meta"

        })

    return campaigns