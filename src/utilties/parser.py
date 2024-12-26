from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from schemas.wallet import WalletRequestCreate


async def get_request(address: str) -> WalletRequestCreate:
    async with AsyncTron(
        network="mainnet",
        provider=AsyncHTTPProvider(
            api_key="1014a0d3-1dc4-408d-89fa-ca25d13f58f3"
        ),
    ) as tron_client:
        try:
            bandwith = await tron_client.get_bandwidth(addr=address)
            balance = await tron_client.get_account_balance(addr=address)
            account = WalletRequestCreate(
                address=address,
                bandwith=float(bandwith),
                balance=float(balance),
                energy=0.0,
            )
            return account
        except Exception as e:
            raise Exception(str(e))
