from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.

def viewEmailData(request, year = None):
    apiURL = 'http://127.0.0.1:8000/api/emails/'
    if year:
        apiURL += f'{year}/'
    
    response = requests.get(apiURL)

    if response.status_code == 200:
        apiData = response.json()
        years = set()
        for email in apiData['emails']:
            email['email_date'] = datetime.fromisoformat(email['email_date'])
            years.add(email['email_date'].year)
        years = sorted(list(years), reverse = True)
    else:
        apiData = {'error': 'Unable to fetch data'}
    
    return render(request, 'emailData.html', {'api_data': apiData, 'years': years})