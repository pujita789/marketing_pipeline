import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

CUSTOMER_TYPES = [
    "New",
    "Returning",
    "Premium"
]


def random_date():
    return (
        datetime.today() -
        timedelta(days=random.randint(0, 365))
    ).strftime("%Y-%m-%d")


def generate_customer_data(records=100):

    customers = []

    for i in range(records):

        customers.append({

            "customer_id": f"CUST{i+1000}",

            "customer_name": fake.name(),

            "email": fake.email(),

            "phone": fake.phone_number(),

            "city": fake.city(),

            "country": fake.country(),

            "customer_type": random.choice(CUSTOMER_TYPES),

            "customer_since": random_date()

        })

    return customers