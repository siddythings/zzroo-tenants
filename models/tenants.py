from pydantic import BaseModel


class TenantModel(BaseModel):
    tenant_id: int
    first_name: str
    image: str
    last_name: str
    email: str
    phone: str
    address: str
    city: str
    state: str
    zip_code: str
    move_in_date: str
    lease_term_months: int
    monthly_rent: float
    security_deposit: float
    emergency_contact_name: str
    emergency_contact_phone: str
    room_number: int
