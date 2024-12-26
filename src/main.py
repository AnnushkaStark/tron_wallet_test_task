import uvicorn
from fastapi import FastAPI

from api.v1.router import api_router as wallet_router

app = FastAPI(
    title="Wallet",
    openapi_url="/wallet/openapi.json",
    docs_url="/wallet/docs",
)


app.include_router(wallet_router, prefix="/secret_service")
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        proxy_headers=True,
    )
