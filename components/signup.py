import flet as ft
import base64
from core.common import CommonContent
from models.redirect import OnClickRedirectPage
from models.signup import UserProfile
from api.lambda_app import API


class Signup:
    def __init__(self, page: ft.Page):
        self.page = page
        self.profile_image = ft.Image(
            src="https://www.w3schools.com/howto/img_avatar.png",
            width=100,
            height=100,
            border_radius=50
        )
        self.first_name = ft.TextField(
            label="First Name",
            hint_text="Enter Your First Name"
        )
        self.last_name = ft.TextField(
            label="Last Name",
            hint_text="Enter Your Last Name"
        )
        self.email = ft.TextField(
            label="Email ID",
            hint_text="Enter Your Email"
        )
        self.phone = ft.TextField(label="Phone",
                                  hint_text="Enter your phone")
        self.address = ft.TextField(label="Address",
                                    hint_text="Enter your address")
        self.city = ft.TextField(label="City",
                                 hint_text="Enter your city")
        self.state = ft.Dropdown(
            label="State",
            hint_text="Choose your state",
            options=[
                ft.dropdown.Option("Select State"),
                ft.dropdown.Option("Andhra Pradesh"),
                ft.dropdown.Option("Arunachal Pradesh"),
                ft.dropdown.Option("Assam"),
                ft.dropdown.Option("Bihar"),
                ft.dropdown.Option("Chhattisgarh"),
                ft.dropdown.Option("Goa"),
                ft.dropdown.Option("Gujarat"),
                ft.dropdown.Option("Haryana"),
                ft.dropdown.Option("Himachal Pradesh"),
                ft.dropdown.Option("Jharkhand"),
                ft.dropdown.Option("Karnataka"),
                ft.dropdown.Option("Kerala"),
                ft.dropdown.Option("Madhya Pradesh"),
                ft.dropdown.Option("Maharashtra"),
                ft.dropdown.Option("Manipur"),
                ft.dropdown.Option("Meghalaya"),
                ft.dropdown.Option("Mizoram"),
                ft.dropdown.Option("Nagaland"),
                ft.dropdown.Option("Odisha"),
                ft.dropdown.Option("Punjab"),
                ft.dropdown.Option("Rajasthan"),
                ft.dropdown.Option("Sikkim"),
                ft.dropdown.Option("Tamil Nadu"),
                ft.dropdown.Option("Telangana"),
                ft.dropdown.Option("Tripura"),
                ft.dropdown.Option("Uttar Pradesh"),
                ft.dropdown.Option("Uttarakhand"),
                ft.dropdown.Option("West Bengal")
            ],
        )
        self.zip_code = ft.TextField(label="Zip Code",
                                     hint_text="Enter your zip code")
        self.otp = ft.TextField(
            hint_text="Enter OTP")

    async def submit(self, e):
        route = f"/{e.control.data.url}"
        if route == "/otp":
            request_obj = dict(
                mobile=self.phone.value
            )
            API.send_otp(request_obj)

        elif route == "/user_profile":
            user_profile_obj = dict(
                first_name=self.first_name.value,
                last_name=self.last_name.value,
                phone_number=self.phone.value,
                email=self.email.value,
                phone=self.phone.value,
                address=self.address.value,
                city=self.city.value,
                state=self.state.value,
                zip_code=self.zip_code.value
            )
            API.user_profle(user_profile_obj)

        await self.page.go_async(route)

    async def otp_validation(self, e):
        route = f"/user_profile"
        request_obj = dict(
            mobile=self.phone.value,
            otp=self.otp.value
        )
        response_obj = API.otp_validation(request_obj)
        self.page.session.set("user", {
            "name": "test",
            "mobile": "1234567890",
            "email": ""
        })
        await self.page.go_async(route)

    def otp_page(self):
        signup_page = ft.Container(
            width=self.page.window_width,
            height=self.page.window_height,
            # bgcolor=ft.colors.SECONDARY_CONTAINER,
            content=ft.Column(
                [
                    self.otp,
                    ft.FilledButton(
                        width=self.page.window_width,
                        height=50,
                        style=ft.ButtonStyle.shape,
                        text="Submit OTP",
                        # font_size=ft.FontSize.SMALL,
                        # font_weight=ft.FontWeight.BOLD,
                        # text_color=ft.TextColor.PRIMARY,
                        on_click=self.otp_validation,
                        data=OnClickRedirectPage(url='user_profile'),
                    ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.bottom_center,
        )
        return signup_page

    def signup_page(self):
        signup_page = ft.Container(
            width=self.page.window_width,
            height=self.page.window_height,
            # bgcolor=ft.colors.SECONDARY_CONTAINER,
            content=ft.Column(
                [
                    self.phone,
                    ft.FilledButton(
                        width=self.page.window_width,
                        height=50,
                        style=ft.ButtonStyle.shape,
                        text="SignUp/Login",
                        # font_size=ft.FontSize.SMALL,
                        # font_weight=ft.FontWeight.BOLD,
                        # text_color=ft.TextColor.PRIMARY,
                        on_click=self.submit,
                        data=OnClickRedirectPage(url="otp"),
                    ),

                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            alignment=ft.alignment.bottom_center,
        )
        return signup_page

    def login_page(self):
        login_page = ft.Container(
            content=ft.Column(
                [
                    self.signup_page()
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            alignment=ft.alignment.bottom_center,
        )
        return login_page

    async def handle_loaded_file(self, e: ft.FilePickerResultEvent):
        self.profile_image.visible = True
        with open(e.files[0].path, "rb") as f:
            self.profile_image.src_base64 = base64.b64encode(
                f.read()).decode('utf-8')
        await self.profile_image.update_async()

    def user_profile(self):
        self.phone.disabled = True
        file_picker = ft.FilePicker(
            on_result=self.handle_loaded_file
        )
        self.page.overlay.append(file_picker)

        container = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.profile_image,
                            ]
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    height=50,
                                    style=ft.ButtonStyle.shape,
                                    text="Upload Profile Picture",
                                    on_click=file_picker.pick_files_async,
                                    data=OnClickRedirectPage(url="home"),
                                )
                            ]
                        ),
                        alignment=ft.alignment.center,
                    ),
                    self.first_name,
                    self.last_name,
                    self.email,
                    self.phone,
                    self.address,
                    self.city,
                    self.state,
                    self.zip_code,
                    ft.FilledButton(
                        width=self.page.window_width,
                        height=50,
                        style=ft.ButtonStyle.shape,
                        text="Save Profile",
                        on_click=self.submit,
                        data=OnClickRedirectPage(url="home"),
                    ),
                ]
            )
        )
        return container
