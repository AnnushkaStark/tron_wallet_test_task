from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from models import WalletRequest

ROOT_ENDPOINT = "/wallet/api/v1/wallet_request/"


class TestReadMulti:
    async def test_read_multi_wallets(
        self,
        async_session: AsyncSession,
        http_client: AsyncClient,
        wallet_first_fixture: WalletRequest,
        wallet_second_fixture: WalletRequest,
    ) -> None:
        response = await http_client.get(ROOT_ENDPOINT)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["total"] == 2
        assert len(response_data["objects"]) == 2
        assert (
            response_data["objects"][0]["address"]
            == wallet_first_fixture.address
        )
        assert (
            response_data["objects"][1]["address"]
            == wallet_second_fixture.address
        )
