from fastapi import FastAPI

from mock_api.routes.google_ads import router as google_router
from mock_api.routes.meta_ads import router as meta_router
from mock_api.routes.crm import router as crm_router
from mock_api.routes.customers import router as customer_router
from mock_api.routes.sales import router as sales_router
from mock_api.routes.website import router as website_router
from mock_api.routes.email import router as email_router
from mock_api.routes.support import router as support_router
from config.settings import settings
print(settings.MINIO_ENDPOINT , 'here is the items of settings')
app = FastAPI(
    title="Marketing Company Simulator",
    description="Mock APIs representing independent marketing systems",
    version="1.0"
)

app.include_router(
    google_router,
    prefix="/api/google",
    tags=["Google Ads"]
)
app.include_router(
    meta_router,
    prefix="/api/meta",
    tags=["Meta Ads"]

)
app.include_router(
    crm_router  , 
    prefix= "/api/crm",
    tags=["CRM"]
) , 
app.include_router(
    customer_router , 
    prefix= "/api/customers", 
    tags=["Customers"]
),
app.include_router(
    email_router,
    prefix="/api/email",
    tags=["Emails"]
),
app.include_router(
    sales_router,
    prefix= "/api/sales",
    tags=["Sales_"]
),
app.include_router(
    support_router,
    prefix= "/api/support",
    tags=["Support"]
),
app.include_router(
    website_router,
    prefix= "/api/website",
    tags=["website"]
)
@app.get("/")
def home():
    return {
        "company": "AdVista Marketing",
        "status": "Running"
    }