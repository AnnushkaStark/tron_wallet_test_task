from tronpy import Tron

from schemas.wallet import WalletRequestCreate


async def get_request(adress: str) -> WalletRequestCreate:
    tron_client = Tron()
    try:
        account_info = tron_client.get_account(addr=adress)
        account = WalletRequestCreate(
            adress=adress,
            bandwith=account_info["bandwith"],
            balance=account_info["balance"] / 100000,
            energy=account_info["energy"],
        )
        return account
    except Exception as e:
        raise Exception(str(e))
