from fastapi import APIRouter

from mock_api.services.sales_data_generator import generate_sales_data

router = APIRouter()


@router.get("/orders")
def get_sales(records: int = 100):

    return {
        "source": "Sales",
        "records": generate_sales_data(records)
    }