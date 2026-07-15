import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

CAMPAIGNS = [
    "Summer Sale",
    "Laptop Launch",
    "Monsoon Offer",
    "Winter Collection",
    "Diwali Blast"
]

LEAD_STATUS = [
    "New",
    "Qualified",
    "Contacted",
    "Converted",
    "Lost"
]

LEAD_SOURCES = [
    "Google Ads",
    "Meta Ads",
    "Organic Search",
    "Referral",
    "Website",
    "Email Campaign"
]


def random_date():
    return (
        datetime.today() - timedelta(days=random.randint(0, 30))
    ).strftime("%Y-%m-%d")


def generate_crm_data(records=100):

    leads = []

    for i in range(records):

        status = random.choice(LEAD_STATUS)

        # Only converted leads generate revenue
        if status == "Converted":
            customer_id = f"CUST{i+1000}"
            conversion_value = round(
                random.uniform(1000, 25000),
                2
            )
            conversion_date = random_date()
        else:
            customer_id = None
            conversion_value = 0
            conversion_date = None

        leads.append({

            "lead_id": f"LEAD{i+1000}",

            "customer_id": customer_id,

            "lead_name": fake.name(),

            "email": fake.email(),

            "phone": fake.phone_number(),

            "campaign_name": random.choice(CAMPAIGNS),

            "lead_source": random.choice(LEAD_SOURCES),

            "lead_status": status,

            "conversion_value": conversion_value,

            "conversion_date": conversion_date,

            "created_date": random_date()

        })

    return leads