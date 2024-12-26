from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from crud.wallet import wallet_request_crud

ROOT_ENDPOINT = "/wallet/api/v1/wallet_request/"


class TestWalletRequest:
    async def test_create_wallet_request(
        self,
        async_session: AsyncSession,
        http_client: AsyncClient,
    ) -> None:
        params = {"address": "TJG8Ad5TetnybUXC618GewPrgsa5dhbpie"}
        response = await http_client.post(ROOT_ENDPOINT, params=params)
        assert response.status_code == 201
        await async_session.close()
        created_wallet = await wallet_request_crud.get_by_adress(
            db=async_session, address=params["address"]
        )
        assert created_wallet is not None
