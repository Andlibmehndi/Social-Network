import requests
import json
from datetime import datetime
from django.contrib.auth import get_user_model
from dotenv import load_dotenv
import os

load_dotenv()
GEO_KEY = os.getenv('GEO_KEY')
TZ_KEY = os.getenv('TZ_KEY')
HLD_KEY = os.getenv('HLD_KEY')


def user_update_asynchronous(user_id):
    User = get_user_model()
    user = User.objects.get(id=user_id)

    # Geolocation
    response = json.loads(requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key={GEO_KEY}&ip_address={user.user_ip}").content)
    user.location = f"{response['city']};{response['country']}"
    fetch_timezone = ''
    if response.get('timezone') is not None:
        fetch_timezone = response['timezone']['name']
    user.save()

    # Time Zone
    timezone = json.loads(requests.get(f'https://timezone.abstractapi.com/v1/current_time/?api_key={TZ_KEY}&location="{fetch_timezone}"').content)
    dt = datetime.fromisoformat(timezone['datetime'])

    # Is holiday
    holiday_specific_date = json.loads(requests.get(f"https://holidays.abstractapi.com/v1/?api_key={HLD_KEY}&country={response['country_code']}&year={dt.year}&month={dt.month}&day={dt.day}").content)

    if holiday_specific_date:
        for h in holiday_specific_date:
            if h["type"] in ['public_holiday', 'religious_holiday', 'National']:
                user.is_holiday_on_signup = True
                break
    else:
        user.is_holiday_on_signup = False
    user.save()
