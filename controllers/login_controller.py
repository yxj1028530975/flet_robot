import flet as ft
from views.login_view import LoginView


class LoginController:
    def __init__(self, page: ft.Page, app):   
        self.page = page
        self.app = app
        self.view = LoginView(page, self.handle_login, self.go_to_signup, self.app.go_back)

    def handle_login(self, username, password):
        print(username, password)
        if username == "" or password == "":
            print("请输入账号或密码")
        elif username == "admin" and password == "admin":
            print("登录成功")
            self.app.navigate("/main")
        else:
            print("登录失败")
       
    def go_to_signup(self):
        self.app.navigate("/signup")
        print("Você foi pra tela Signup")

    def on_back(self, event):
        # Logic to navigate back
        self.app.navigate()
        print("voce clicou para voltar")