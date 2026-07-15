from fastapi import APIRouter

from mock_api.services.google_data_generator import generate_google_campaigns

router = APIRouter()


@router.get("/campaigns")
def get_campaigns(records: int = 100):

    return {
        "source": "Google Ads",
        "records": generate_google_campaigns(records)
    }