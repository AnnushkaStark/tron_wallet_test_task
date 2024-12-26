from typing import Optional, Sequence

from sqlalchemy import func, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models import WalletRequest
from schemas.wallet import WalletRequestCreate, WalletRequestUpdate


class WalletRequestCRUD:
    async def create(
        self,
        db: AsyncSession,
        create_schema: WalletRequestCreate,
        commit: bool = True,
    ) -> WalletRequest:
        data = create_schema.model_dump(exclude_unset=True)
        stmt = insert(WalletRequest).values(**data).returning(WalletRequest)
        res = await db.execute(stmt)
        obj = res.scalars().first()
        if commit:
            await db.commit()
            await db.refresh(obj)
        return obj

    async def update(
        self,
        db: AsyncSession,
        update_data: WalletRequestUpdate,
        db_obj: WalletRequest,
        commit: bool = True,
    ) -> WalletRequest:
        if isinstance(update_data, WalletRequestUpdate):
            update_data = update_data.model_dump(exclude_unset=True)
        stmt = (
            update(WalletRequest)
            .where(WalletRequest.id == db_obj.id)
            .values(**update_data)
            .returning(WalletRequest)
        )
        res = await db.execute(stmt)
        obj = res.scalars().first()
        if commit:
            await db.commit()
            await db.refresh(obj)
        return obj

    async def get_multi_with_total(
        self, db: AsyncSession, skip: int = 0, limit: int = 1000
    ) -> Sequence[WalletRequest]:
        statement = (
            select(WalletRequest, func.count().over().label("total"))
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(statement)
        rows = result.mappings().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["WalletRequest"] for r in rows],
        }

    async def get_by_adress(
        self, db: AsyncSession, address: str
    ) -> Optional[WalletRequest]:
        statement = select(WalletRequest).where(
            WalletRequest.address == address
        )
        result = await db.execute(statement)
        return result.scalars().first()


wallet_request_crud = WalletRequestCRUD()
