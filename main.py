import os
import httpx
from dataclasses import dataclass
from furl import furl


@dataclass
class OwnerRezApiUser:
    """Class for getting the user."""
    agent: str
    username: str
    token: str

    def get_auth(self):
        return self.username, self.token

    def headers(self):
        return {'user-agent': self.agent}


API_URL = "https://api.ownerreservations.com"


def get_user() -> OwnerRezApiUser:
    return OwnerRezApiUser(agent=os.environ.get('owner_rez_user_agent', 'api_python_agent'),
                           username=os.environ.get('owner_rez_username', None),
                           token=os.environ.get('owner_rez_token', None))


def get_template(request_url: furl, auth_user: OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_user = get_user()
    print(get_template(furl(API_URL).set(path=f'v2/fielddefinitions'), api_user))
