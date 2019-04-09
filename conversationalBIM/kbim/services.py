import requests
import urllib.request
import json

def two_legged_authenticate():
    url = "https://developer.api.autodesk.com/authentication/v1/authenticate"
    payload = "client_id=6iJdE4Buo9PhkD4B9EV9zLnMgWf8kZUW&client_secret=B7QR6AEb6Kzq81II&grant_type=client_credentials&scope=account%3Aread&undefined="
    headers = {
       'Content-Type': "application/x-www-form-urlencoded",
       'cache-control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        return "Token generated"
    else:
       return "Error"


def three_legged_token(code):
    url = "https://developer.api.autodesk.com/authentication/v1/gettoken"
    payload = {
        'client_id': '6iJdE4Buo9PhkD4B9EV9zLnMgWf8kZUW',
        'client_secret': 'B7QR6AEb6Kzq81II',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/kbim/oauth/callback'
    }
    #payload = "client_id=6iJdE4Buo9PhkD4B9EV9zLnMgWf8kZUW&client_secret=B7QR6AEb6Kzq81II&grant_type=authorization_code&code=b7cci6zg_QDIhsjovVYZCq2XJy1t3Rh0Tnik5hBK&redirect_uri=http%3A%2F%2Flocalhost%3A8000&undefined="
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    }
    res = requests.request("POST", url, data=payload, headers=headers)
    if res.status_code == 200:
        return res.json()
    else:
        return None

responses = {
    "what's your name": "my name is EchoBot",
    "what's the weather today": "it's sunny"
}

def respond(message):
    if message in responses:
        return responses[message]
    else:
        return "Sorry, I have not been programmed to answer this question"