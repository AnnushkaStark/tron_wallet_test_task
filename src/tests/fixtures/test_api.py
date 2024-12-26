import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from models import WalletRequest


@pytest_asyncio.fixture
async def wallet_first_fixture(async_session: AsyncSession) -> WalletRequest:
    wallet = WalletRequest(
        address="TXYZ1234567890", bandwith=1000.0, energy=500.0, balance=10.0
    )
    async_session.add(wallet)
    await async_session.commit()
    await async_session.refresh(wallet)
    return wallet


@pytest_asyncio.fixture
async def wallet_second_fixture(async_session: AsyncSession) -> WalletRequest:
    wallet = WalletRequest(
        address="TJG8Ad5TetnybUXC618GewPrgsa5dhbpie",
        bandwith=1000.0,
        energy=500.0,
        balance=10.0,
    )
    async_session.add(wallet)
    await async_session.commit()
    await async_session.refresh(wallet)
    return wallet
