from fastapi import APIRouter

from mock_api.services.crm_data_gen import generate_crm_data

router = APIRouter()


@router.get("/leads")
def get_crms(records: int = 100):

    return {
        "source": "CRM",
        "records": generate_crm_data(records)
    }