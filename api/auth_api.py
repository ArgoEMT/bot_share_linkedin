import requests
import webbrowser
import json


#? Permission needed
# rw_organization_admin
# w_organization_social
# r_organization_social
# w_member_social
# r_member_social

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
            'scope': requests.utils.unquote('rw_organization_admin%20w_organization_social%20r_organization_social%20r_member_social')
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
