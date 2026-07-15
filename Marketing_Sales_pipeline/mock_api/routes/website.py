from fastapi import APIRouter

from mock_api.services.website_data_generator import generate_website_sessions

router = APIRouter()


@router.get("/sessions")
def get_website_sessions(records: int = 100):

    return {
        "source": "Website Analytics",
        "records": generate_website_sessions(records)
    }