import asyncio
import datetime
import os
import httpx
from dataclasses import dataclass
from furl import furl
import arrow


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


def get_authorized(request_url: furl, auth_user: OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def get_authorized_async(request_url: furl, auth_user: OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


def default_start_date() -> str:
    return arrow.get(datetime.date(2000, 1, 1)).to('utc').format("YYYY-MM-DD")


async def async_main():
    user = get_user()
    in_the_beginning_date = default_start_date()
    id = 1

    # print(get_authorized(furl(API_URL).set(path=f'v2/fielddefinitions'), get_user()))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/bookings', args=dict(since_utc=in_the_beginning_date)), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/fielddefinitions'), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/fields', args=dict(entity_type='property', entity_id=id)), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/guests', args=dict(created_since_utc=in_the_beginning_date)), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/inquiries', args=dict(since_utc=in_the_beginning_date)), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/listings'), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/owners'), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/properties'), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/quotes', args=dict(created_since_utc=in_the_beginning_date)), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/tagdefinitions', args=dict(active=True)), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/users/me'), user))
    print(await get_authorized_async(furl(API_URL).set(path=f'v2/webhooksubscriptions'), user))


if __name__ == '__main__':
    asyncio.run(async_main())

