import flet as ft
from views.main_view import MainView


class MainController:
    def __init__(self, page: ft.Page, app):   
        self.page = page
        self.app = app
        self.view = MainView(page, self.handle_login, self.go_to_signup, self.app.go_back)

    def handle_login(self, username, password):
       if username == "" or password == "":
        print("请输入账号或密码")
       
    def go_to_signup(self):
        self.app.navigate("/signup")
        print("Você foi pra tela Signup")

    def on_back(self, event):
        # Logic to navigate back
        self.app.navigate("/")
        print("voce clicou para voltar")