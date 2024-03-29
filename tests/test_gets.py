import datetime
import unittest

import arrow
from furl import furl

from src.api_template_requests import API_URL
from src.api_user import OwnerRezApiUser, get_env_user

from src.api_template_requests import get, get_async


def default_start_date() -> str:
    return arrow.get(datetime.date(2000, 1, 1)).to('utc').format("YYYY-MM-DD")


class IntegrationTestCases(unittest.TestCase):

    def setUp(self):
        self.user = get_env_user()
        self.user.is_valid()

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def run_gets(self, start_date: str, start_id: int, input_user: OwnerRezApiUser):
        print(get(furl(API_URL).set(path=f'v2/bookings', args=dict(since_utc=start_date)), input_user))
        print(get(furl(API_URL).set(path=f'v2/fielddefinitions'), input_user))
        print(get(furl(API_URL).set(path=f'v2/fields', args=dict(entity_type='property', entity_id=start_id)), input_user))
        print(get(furl(API_URL).set(path=f'v2/guests', args=dict(created_since_utc=start_date)), input_user))
        print(get(furl(API_URL).set(path=f'v2/inquiries', args=dict(since_utc=start_date)), input_user))
        print(get(furl(API_URL).set(path=f'v2/listings'), input_user))
        print(get(furl(API_URL).set(path=f'v2/owners'), input_user))
        print(get(furl(API_URL).set(path=f'v2/properties'), input_user))
        print(get(furl(API_URL).set(path=f'v2/quotes', args=dict(created_since_utc=start_date)), input_user))
        print(get(furl(API_URL).set(path=f'v2/tagdefinitions', args=dict(active=True)), input_user))
        print(get(furl(API_URL).set(path=f'v2/users/me'), input_user))
        print(get(furl(API_URL).set(path=f'v2/webhooksubscriptions'), input_user))


    async def run_gets_async(self, start_date: str, start_id: int, input_user: OwnerRezApiUser):
        print(await get_async(furl(API_URL).set(path=f'v2/bookings', args=dict(since_utc=start_date)), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/fielddefinitions'), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/fields', args=dict(entity_type='property', entity_id=start_id)), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/guests', args=dict(created_since_utc=start_date)), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/inquiries', args=dict(since_utc=start_date)), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/listings'), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/owners'), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/properties'), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/quotes', args=dict(created_since_utc=start_date)), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/tagdefinitions', args=dict(active=True)), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/users/me'), input_user))
        print(await get_async(furl(API_URL).set(path=f'v2/webhooksubscriptions'), input_user))


if __name__ == '__main__':
    unittest.main()
