from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from crud.wallet import wallet_request_crud
from models import WalletRequest
from schemas.wallet import WalletRequestCreate, WalletRequestUpdate
from utilties.parser import get_request


async def create(
    db: AsyncSession, schema: WalletRequestCreate
) -> WalletRequest:
    wallet_info = await wallet_request_crud.create(db=db, create_schema=schema)
    return wallet_info


async def update(
    db: AsyncSession, db_obj: WalletRequest, schema: WalletRequestCreate
):
    update_data = WalletRequestUpdate(
        bandwith=schema.bandwith, energy=schema.energy, balance=schema.balance
    )
    wallet_info = await wallet_request_crud.update(
        db=db,
        db_obj=db_obj,
        update_data=update_data.model_dump(exclude_unset=True),
    )
    return wallet_info


async def request(db: AsyncSession, adress: str) -> Optional[WalletRequest]:
    try:
        schema = await get_request(adress=adress)
    except Exception as e:
        raise Exception(str(e))
    if exsisted_object := await wallet_request_crud.get_by_adress(
        db=db, adress=adress
    ):
        return await update(db=db, db_obj=exsisted_object, schema=schema)
    return await create(db=db, chema=schema)
