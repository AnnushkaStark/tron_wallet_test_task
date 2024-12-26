from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.dependencies.database import get_async_db
from crud.wallet import wallet_request_crud
from schemas.wallet import WalletRequestPaginatedResponse
from service import wallet as wallet_service

router = APIRouter()


@router.get("/", response_model=WalletRequestPaginatedResponse)
async def read_wallets(
    skip: int = 0, limit: int = 20, db: AsyncSession = Depends(get_async_db)
):
    return await wallet_request_crud.get_multi_with_total(
        db=db, skip=skip, limit=limit
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def get_wallet_request(
    address: str, db: AsyncSession = Depends(get_async_db)
):
    try:
        return await wallet_service.request(db=db, address=address)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
