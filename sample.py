import base64
import mimetypes
import os
import urllib
import webbrowser
import json

from adal import AuthenticationContext
import pyperclip
import requests

CLIENT_ID = "" #Application ID fro Azure AD Portal
AUTHORITY_URL = 'https://login.microsoftonline.com/common'
RESOURCE = 'https://graph.microsoft.com'
API_VERSION = 'beta'

def api_endpoint(url):
    if urllib.parse.urlparse(url).scheme in ['http', 'https']:
        return url
    return urllib.parse.urljoin(f'{RESOURCE}/{API_VERSION}/',
                                url.lstrip('/'))

def device_flow_session(client_id, auto=False):

    ctx = AuthenticationContext(AUTHORITY_URL, api_version=None)
    device_code = ctx.acquire_user_code(RESOURCE,client_id)

    if auto:
        pyperclip.copy(device_code['user_code'])
        webbrowser.open(device_code['verification_url'])
        print(f'The code {device_code["user_code"]} has been copied to your clipboard, '
              f'and your web browser is opening {device_code["verification_url"]}. '
              'Paste the code to sign in.')
    else:
        print(device_code['message'])

    token_response = ctx.acquire_token_with_device_code(RESOURCE,device_code,client_id)
    if not token_response.get('accessToken', None):
        return None
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token_response["accessToken"]}',
                            'SdkVersion': 'sample-python-adal',
                            'x-client-SKU': 'sample-python-adal'})
    return session

if __name__ == '__main__':
    session = device_flow_session(CLIENT_ID)
    #   List calendars
    cal = session.get("https://graph.microsoft.com/beta/me/calendars")
    cal = cal.json()
    for i in cal['value']:
        print(i['name'])

    #   Create Event
    data = {"subject":"Test Event",
            "body":{"contentType":"HTML","content":"Test content"},
            "start":{"dateTime":"2018-09-05T16:30:00",
                     "timeZone":"Pacific Standard Time"},
            "end":{"dateTime":"2018-09-05T17:30:00",
                   "timeZone":"Pacific Standard Time"},
            "location":{"displayName":"First Floor"},
            "attendees":[{"emailAddress":{"address":"testuser@dannybritto.onmicrosoft.com",
                                          "name":"Test User"},
                          "type":"required"}]
            }
    data = json.dumps(data)
    create_Event = session.post("https://graph.microsoft.com/beta/me/calendar/events",data=data,headers={"Content-type":"application/json"})
