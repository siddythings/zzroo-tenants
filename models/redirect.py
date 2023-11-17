
from pydantic import BaseModel


class OnClickRedirectPage(BaseModel):
    url: str
    on_click: bool = True
