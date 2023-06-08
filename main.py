import asyncio
import datetime
import arrow
import owner_rez_api_user as orez
import owner_rez_api_template_requests as api
from furl import furl

API_URL = "https://api.ownerreservations.com"


def default_start_date() -> str:
    return arrow.get(datetime.date(2000, 1, 1)).to('utc').format("YYYY-MM-DD")


def run_gets(start_date: str, start_id: int, input_user: orez.OwnerRezApiUser):
    print(api.get(furl(API_URL).set(path=f'v2/bookings', args=dict(since_utc=start_date)), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/fielddefinitions'), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/fields', args=dict(entity_type='property', entity_id=start_id)), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/guests', args=dict(created_since_utc=start_date)), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/inquiries', args=dict(since_utc=start_date)), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/listings'), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/owners'), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/properties'), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/quotes', args=dict(created_since_utc=start_date)), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/tagdefinitions', args=dict(active=True)), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/users/me'), input_user))
    print(api.get(furl(API_URL).set(path=f'v2/webhooksubscriptions'), input_user))


async def run_gets_async(start_date: str, start_id: int, input_user: orez.OwnerRezApiUser):
    print(await api.get_async(furl(API_URL).set(path=f'v2/bookings', args=dict(since_utc=start_date)), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/fielddefinitions'), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/fields', args=dict(entity_type='property', entity_id=start_id)), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/guests', args=dict(created_since_utc=start_date)), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/inquiries', args=dict(since_utc=start_date)), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/listings'), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/owners'), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/properties'), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/quotes', args=dict(created_since_utc=start_date)), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/tagdefinitions', args=dict(active=True)), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/users/me'), input_user))
    print(await api.get_async(furl(API_URL).set(path=f'v2/webhooksubscriptions'), input_user))


async def async_main():
    await run_gets_async(default_start_date(), 1, orez.get_user())
    # print(get_authorized(furl(API_URL).set(path=f'v2/fielddefinitions'), get_user()))


if __name__ == '__main__':
    asyncio.run(async_main())
