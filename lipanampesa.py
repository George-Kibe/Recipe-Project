import requests
import keys
import base64
from keys import generate_access_token
from utils import get_timestamp

access_token=generate_access_token()
formatted_time=get_timestamp()

def generate_password():   
    data_to_encode=keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time
    encoded_string=base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8')
    return decoded_password

def lipanampesa():    
    api_url="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers={"Authorization":"Bearer %s" % access_token}
    request={
        "BusinessShortCode":keys.business_short_code,
        "Password": generate_password(),
        "Timestamp": formatted_time,
        "TransactionType":"CustomerPayBillOnline",
        "Amount":"1",
        "PartyA":keys.phone_number,
        "PartyB":keys.business_short_code,
        "PhoneNumber":keys.phone_number,
        "CallBackURL":"https://test.comparables.co.ke/lipanampesa",
        "AccountReference":"12345678",
        "TransactionDesc":"Paying School Fees",
    }

    response=requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipanampesa()