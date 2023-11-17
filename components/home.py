from flet import *


class Home:
    def __init__(self, page):
        self.page = page

    def home(self):
        container = Container(
            width=self.page.window_width,
            height=80,
            border_radius=10,
            bgcolor="red",
            content=Container(
                content=Row(
                    controls=[
                        Text(
                            "Controls Gallery",
                            style=TextThemeStyle.TITLE_MEDIUM,
                            weight=FontWeight.W_500,
                        ),
                        IconButton(
                            content=Image(
                                src="github-mark.svg",
                                width=24,
                                height=24,
                                color=colors.ON_SURFACE,
                            ),
                            url="",
                            url_target="_blank",
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=10,
            ),

            visible=True
        )
        return container
