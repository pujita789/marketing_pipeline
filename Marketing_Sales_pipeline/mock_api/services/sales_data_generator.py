import random
from datetime import datetime, timedelta

PRODUCTS = [
    "Laptop",
    "Mobile",
    "Headphones",
    "Smart Watch",
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


def generate_sales_data(records=100):

    orders = []

    for i in range(records):

        quantity = random.randint(1, 5)

        price = random.randint(1000, 50000)

        orders.append({

            "order_id": f"ORD{i+1000}",

            "customer_id": f"CUST{random.randint(1000,1099)}",

            "campaign_name": random.choice(CAMPAIGNS),

            "product_name": random.choice(PRODUCTS),

            "quantity": quantity,

            "amount": quantity * price,

            "order_date": random_date()

        })

    return orders