from fastapi import APIRouter

from mock_api.services.meta_data_gen import generate_meta_campaigns

router = APIRouter()


@router.get("/campaigns")
def get_meta_campaigns(records: int = 100):

    return {
        "source": "Meta Ads",
        "records": generate_meta_campaigns(records)
    }