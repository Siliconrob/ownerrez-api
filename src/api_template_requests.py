from datetime import timedelta
import httpx
import stamina
from furl import furl
from src.api_user import OwnerRezApiUser

max_retry_attempts = 3
timeout_delay = timedelta(seconds=10)

API_URL = "https://api.ownerrez.com"


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
def get(request_url: furl, auth_user: OwnerRezApiUser) -> httpx.Response:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
async def get_async(request_url: furl, auth_user: OwnerRezApiUser) -> httpx.Response:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
def post(request_url: furl, send_data: dict, auth_user: OwnerRezApiUser) -> httpx.Response:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.post(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
async def post_async(request_url: furl, send_data: dict, auth_user: OwnerRezApiUser) -> httpx.Response:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.post(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
def patch(request_url: furl, send_data: dict, auth_user: OwnerRezApiUser) -> httpx.Response:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.patch(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
async def patch_async(request_url: furl, send_data: dict, auth_user: OwnerRezApiUser) -> httpx.Response:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.patch(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
def put(request_url: furl, send_data: dict, auth_user: OwnerRezApiUser) -> httpx.Response:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.put(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
async def put_async(request_url: furl, send_data: dict, auth_user: OwnerRezApiUser) -> httpx.Response:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.put(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
def delete(request_url: furl, auth_user: OwnerRezApiUser) -> httpx.Response:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.delete(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r


@stamina.retry(on=httpx.HTTPError, attempts=max_retry_attempts, timeout=timeout_delay)
async def delete_async(request_url: furl, auth_user: OwnerRezApiUser) -> httpx.Response:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.delete(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r
