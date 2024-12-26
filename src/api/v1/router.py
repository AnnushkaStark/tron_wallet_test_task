from fastapi import APIRouter

from api.v1.endpoints.wallet import router as wallet_request_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    wallet_request_router, prefix="/wallet_request", tags=["WalletRequest"]
)
