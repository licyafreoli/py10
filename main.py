import flet as ft

def main(page: ft.Page):
    def submit_form(e):
        name = name_input.value
        email = email_input.value
        message = message_input.value
        if name and email and message:
            confirmation_text.value = "Formulário enviado com sucesso!"
            page.update()

    name_input = ft.TextField(label="Nome", autofocus=True)
    email_input = ft.TextField(label="Email")
    message_input = ft.TextField(label="Mensagem", multiline=True)
    submit_button = ft.ElevatedButton("Enviar", on_click=submit_form)
    confirmation_text = ft.Text()

    page.add(name_input, email_input, message_input, submit_button, confirmation_text)

ft.app(target=main)
