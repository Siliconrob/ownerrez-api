import httpx
from furl import furl
import owner_rez_api_user as orez


def get_authorized(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    with httpx.Client(headers=auth_user.headers()) as client:
        r = client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def get_authorized_async(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.get(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def post_authorized_async(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.post(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def patch_authorized_async(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.patch(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def put_authorized_async(request_url: furl, send_data: dict, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.put(request_url.url, data=send_data, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()


async def delete_authorized_async(request_url: furl, auth_user: orez.OwnerRezApiUser) -> dict:
    async with httpx.AsyncClient(headers=auth_user.headers()) as client:
        r = await client.delete(request_url.url, auth=auth_user.get_auth())
        r.raise_for_status()
        return r.json()
