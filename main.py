import flet as ft

TextBoxWidth = 300

# will be transformed to a different file later
# im not gonna bother with securing it

username="Admin"
password="1234"

connectionToServer=False

def main(page: ft.Page):
    page.title = "DELL Server Control Panel"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    text = ft.Text(value="Welcome", color="red")

    def loggedIn():
        page.banner = ft.Banner(
            bgcolor=ft.colors.BLACK,
            leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
            content=ft.Text(
                "Cannot connect to server statistics! Are you sure it's even on?"
            ),
            actions=[
                ft.TextButton("Retry"),
            ],
        )

        if connectionToServer == False:
            page.banner.open=True
            page.update()

    def buttonClicked(e):
        name=ft.TextField(label="Username",autofocus=True,width=TextBoxWidth)
        passcode=ft.TextField(label="Passcode",width=TextBoxWidth)

        def buttonClick(e):
            if name.value == username and passcode.value == password:
                loginSuccess = ft.Text(value=f"Login Success, welcome {name.value}.")
                page.clean()
                page.add(loginSuccess)
                page.update()
                ft.sleep(2)
                loginSuccess.value="Getting Everything Ready.."
                page.update()
                ft.sleep(4)
                page.clean()
                page.update()
                loggedIn()
            else:
                loginFail = ft.Text(value="Login Fail.")
                loginFail.visible=True
                page.add(loginFail)
                ft.sleep(3)
                loginFail.visible=False
                page.update()
        newLogin=ft.ElevatedButton("Login",width=TextBoxWidth,on_click=buttonClick)
        page.add(name)
        page.add(passcode)
        page.add(newLogin)
        text2.visible=False
        page.update()
            

    text2 = ft.ElevatedButton(text="Login", on_click=buttonClicked)
    page.controls.append(text)
    page.add(text2)
    page.update()
    


ft.app(target=main, view=ft.WEB_BROWSER)