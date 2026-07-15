BASE_URL = "http://host.docker.internal:8000"

SOURCES = {

    "google_ads": {

        "url": f"{BASE_URL}/api/google/campaigns",

        "response_key": "records"

    },

    "meta_ads": {

        "url": f"{BASE_URL}/api/meta/campaigns",

        "response_key": "records"

    },
    "sales_ads":{
        "url" : f"{BASE_URL}/api/sales/orders" , 
        "response_key" : "records"
    },
    "support":{
        "url" : f"{BASE_URL}/api/support/tickets" , 
        "response_key" : "records"
    }
   ,
   "website":{
        "url" : f"{BASE_URL}/api/website/sessions" , 
        "response_key" : "records"
    } ,
    "email":{
        "url" : f"{BASE_URL}/api/email/campaigns" , 
        "response_key" : "records"
    } ,
     "customers":{
        "url" : f"{BASE_URL}/api/customers/campaigns" , 
        "response_key" : "records"
    } ,
     "crm":{
        "url" : f"{BASE_URL}/api/crm/leads" , 
        "response_key" : "records"
    } 
}