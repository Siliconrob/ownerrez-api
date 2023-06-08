import httpx
from furl import furl
import owner_rez_api_user as orez


def get(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def get_async(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


def post(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.post(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def post_async(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.post(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


def patch(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.patch(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def patch_async(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.patch(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


def put(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.put(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def put_async(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.put(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


def delete(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.delete(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def delete_async(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.delete(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()
