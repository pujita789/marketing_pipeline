from fastapi import APIRouter

from mock_api.services.support_data_generator import generate_support_tickets

router = APIRouter()


@router.get("/tickets")
def get_support_tickets(records: int = 100):

    return {
        "source": "Support",
        "records": generate_support_tickets(records)
    }