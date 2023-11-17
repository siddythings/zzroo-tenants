from flet import *
from core.common import CommonContent


class AppBar:
    def __init__(self, page: Page):
        self.page = page

    def appbar(self, type):
        first_page_contents = Container(
            content=Column(
                controls=[
                    Row(alignment='spaceBetween',
                        controls=[
                            Row(
                                #   on_click=lambda e: shrink(e),
                                controls=[
                                    Text("ZZROO"),
                                    Text(
                                        f"{type}", style=TextThemeStyle.TITLE_MEDIUM, weight=FontWeight.W_700, color=CommonContent.PRIMARY)
                                ]),
                            Row(
                                controls=[
                                    Icon(icons.SEARCH),
                                    IconButton(icon=icons.NOTIFICATIONS_OUTLINED, on_click=lambda _: self.page.go(
                                        '/create_task'))
                                ],
                            ),
                        ],
                        )
                ],
            ),
        )

        container = Container(
            width=self.page.window_width,
            height=42,
            # bgcolor=CommonContent.PRIMARY,
            border_radius=10,

            content=ResponsiveRow(
                controls=[
                    Container(
                        width=self.page.window_width,
                        height=self.page.window_height,
                        padding=padding.only(
                            top=10, left=20,
                            right=20, bottom=5
                        ),
                        content=Column(
                            controls=[
                                first_page_contents
                            ]
                        )
                    )
                ]
            ),
            visible=False
        )

        return container
