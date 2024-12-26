from typing import List, Optional

from pydantic import BaseModel


class WalletRequestBase(BaseModel):
    adress: str
    bandwith: float
    energy: float
    balance: float

    class Config:
        from_attributes = True


class WalletRequestCreate(WalletRequestBase):
    ...


class WalletRequestUpdate(BaseModel):
    bandwith: Optional[float] = None
    energy: Optional[float] = None
    balance: Optional[float] = None


class WalletRequestResponse(WalletRequestBase):
    id: int


class WalletRequestPaginatedResponse(BaseModel):
    limit: int
    offset: int
    total: int
    objects: List[WalletRequestResponse]
