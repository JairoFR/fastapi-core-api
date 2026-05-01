from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class FacturaBase(BaseModel):
    numero: str
    cliente: str
    monto: float
    pagado: bool = False

class FacturaCreate(FacturaBase):
    pass

class FacturaUpdate(BaseModel):
    cliente: Optional[str] = None
    monto: Optional[float] = None
    pagado: Optional[bool] = None

class FacturaResponse(FacturaBase):
    id: int
    creado_en: datetime = datetime.now()

    class Config:
        from_attributes = True