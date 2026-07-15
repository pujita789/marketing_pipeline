import random
from datetime import datetime, timedelta

ISSUES = [
    "Payment",
    "Refund",
    "Delivery",
    "Product Defect",
    "Login Problem"
]

STATUS = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]

PRIORITY = [
    "Low",
    "Medium",
    "High"
]


def random_date():

    return (
        datetime.today() -
        timedelta(days=random.randint(0,30))
    ).strftime("%Y-%m-%d")


def generate_support_tickets(records=100):

    tickets = []

    for i in range(records):

        tickets.append({

            "ticket_id": f"TKT{i+1000}",

            "customer_id": f"CUST{random.randint(1000,1099)}",

            "issue_type": random.choice(ISSUES),

            "priority": random.choice(PRIORITY),

            "status": random.choice(STATUS),

            "resolution_time_hours": random.randint(1,72),

            "created_date": random_date()

        })

    return tickets