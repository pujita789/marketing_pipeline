from fastapi import APIRouter

from mock_api.services.email_data_generator import generate_email_campaigns

router = APIRouter()


@router.get("/campaigns")
def get_email_campaigns(records: int = 100):

    return {
        "source": "Email Marketing",
        "records": generate_email_campaigns(records)
    }