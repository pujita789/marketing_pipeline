from fastapi import APIRouter

from mock_api.services.customers_data_generator import generate_customer_data

router = APIRouter()


@router.get("/campaigns")
def get_customers(records: int = 100):

    return {
        "source": "Customers",
        "records": generate_customer_data(records)
    }