import flet as ft
from utils.utils import create_app_bar

class MainView:
    def __init__(self, page: ft.Page, on_login, on_signup, go_back):
        self.page = page
        self.page.window_width = 1650
        self.page.window_height = 1700
        self.on_login = on_login
        self.on_signup = on_signup
        self.on_back = go_back
        self.setup_page()
        self.main_page_ui()
        self.app_bar = create_app_bar("主页", go_back)
        #print(create_app_bar("Login", on_back))
        self.page.add(self.app_bar)

    def setup_page(self):
        self.page.controls.clear()
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 1650
        self.page.window_height = 1700
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = '主页'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
        self.page.update()
        
    def main_page_ui(self):
        lb_login = ft.Text(
            "用户身份验证",
            size=12,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )

        tf_usuario = ft.TextField(
            label='用户名',
            hint_text='密码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
        )

        tf_senha = ft.TextField(
            label='密码',
            hint_text='密码',
            text_size=12,
            height=40,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )

        bt_login = ft.ElevatedButton(
            "登陆",
            on_click=lambda e: self.on_login(tf_usuario.value, tf_senha.value),
            width=100,
            height=40,
        )

        bt_criar = ft.TextButton(
            "注册",
            on_click=lambda _: self.on_signup(),
            width=120,
            height=40
        )

        self.page.add(lb_login, tf_usuario, tf_senha, bt_login, bt_criar)
        self.page.update()
