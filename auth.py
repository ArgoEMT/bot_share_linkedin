import requests
import webbrowser
import json


def get_authorization_code(
    client_id,
    redirect_uri,
):
    response = requests.get(
        "https://www.linkedin.com/oauth/v2/authorization",
        params={
            'response_type': 'code',
            'client_id': client_id,
            'redirect_uri': requests.utils.unquote(redirect_uri),
            'scope': requests.utils.unquote('r_liteprofile%20r_emailaddress%20w_member_social')
        },
    )
    webbrowser.open(response.url)
    return response.content


def get_grant_token(
    accessToken,
    client_id,
    client_secret,
    redirect_uri
):
    response = requests.post(
        requests.utils.unquote(
            "https://www.linkedin.com/oauth/v2/accessToken"),
        data={
            "grant_type": "authorization_code",
            "code": accessToken,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri
        },
    )
    
    return {
        "status": response.status_code,
        "content": json.loads(response.content)
    }
