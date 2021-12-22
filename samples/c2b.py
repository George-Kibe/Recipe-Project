import json
import requests
from requests.api import request
import keys
from keys import generate_access_token

access_token=generate_access_token()

def register_url():
    api_url="https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers={"Authorization":"Bearer %s" % access_token}
    request={
        "ShortCode": keys.business_short_code,
        "ResponseType": "Completed",
        "ConfirmationURL":"http://test.comparables.co.ke/confirm",
        "ValidationURL":"http://test.comparables.co.ke/validate",
    }

    response=requests.post(api_url, json=request, headers=headers)
    print(response.text)

def simulate_c2b_transaction():
    api_url="https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers={"Authorization":"Bearer %s" % access_token}
    request={
        "ShortCode":keys.business_short_code,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn":keys.test_msisdn,
        "BillRefNumber":"87654321", #like an account number or invoice no
    }
    response=requests.post(api_url, json=request, headers=headers)
    print(response.text)

simulate_c2b_transaction()
