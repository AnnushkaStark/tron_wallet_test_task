from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from databases.database import Base


class WalletRequest(Base):
    """
    Модель кошелька

    # Attrs:
        - id: int - идетификатор
        - address: str - url  в сети tron
        - bandwith: float - пропускная способноссть
        - energy: float - энергия
        - balance: float - баланс
    """

    __tablename__ = "wallet_request"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    address: Mapped[str] = mapped_column(String, unique=True, index=True)
    bandwith: Mapped[float]
    energy: Mapped[float]
    balance: Mapped[float]
