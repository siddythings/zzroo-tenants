from pydantic import BaseModel


class SettingsModel(BaseModel):
    settings_id: int
    settings_name: str
    settings_icon: str
    settings_route: str
