import random
from datetime import datetime, timedelta

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
        timedelta(days=random.randint(0,30))
    ).strftime("%Y-%m-%d")


def generate_email_campaigns(records=100):

    campaigns = []

    for i in range(records):

        sent = random.randint(5000,30000)

        opened = random.randint(1000,sent)

        clicked = random.randint(100,opened)

        campaigns.append({

            "email_campaign_id": f"EM{i+1000}",

            "campaign_name": random.choice(CAMPAIGNS),

            "emails_sent": sent,

            "emails_opened": opened,

            "emails_clicked": clicked,

            "unsubscribe_count": random.randint(0,50),

            "send_date": random_date()

        })

    return campaigns