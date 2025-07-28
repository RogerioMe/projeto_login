import customtkinter as ctk

ctk.set_appearance_mode('dark')


def centralizar_janela(janela, largura, altura):
    janela_width = largura
    janela_height = altura

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    pos_x = int((screen_width / 2) - (janela_width / 2))
    pos_y = int((screen_height / 2) - (janela_height / 2))

    janela.geometry(f"{janela_width}x{janela_height}+{pos_x}+{pos_y}")

# Tela principal após login
def abrir_tela_principal():
    tela_principal = ctk.CTk()
    tela_principal.title("Tela Principal")
    centralizar_janela(tela_principal, 400, 300)

    mensagem = ctk.CTkLabel(tela_principal, text="🎉 Bem-vindo à Tela Principal!", font=("Arial", 16))
    mensagem.pack(pady=40)

    botao_sair = ctk.CTkButton(tela_principal, text="Sair", command=tela_principal.destroy)
    botao_sair.pack(pady=10)

    tela_principal.mainloop()


def validar_login():
    usuario = campo_usuario.get().strip().lower()
    senha = campo_senha.get()

    usuario_correto = 'antonio'
    senha_correta = '123456'

    if usuario == usuario_correto and senha == senha_correta:
        resultado_login.configure(text='Login feito com sucesso!!', text_color='green')
        app.after(1000, lambda: [app.destroy(), abrir_tela_principal()])
    else:
        if usuario != usuario_correto and senha != senha_correta:
            resultado_login.configure(text='Usuário e senha incorretos', text_color='red')
        elif usuario != usuario_correto:
            resultado_login.configure(text='Usuário digitado de forma incorreta', text_color='red')
        else:
            resultado_login.configure(text='Senha digitada de forma incorreta', text_color='red')
        
        campo_usuario.delete(0, 'end')
        campo_senha.delete(0, 'end')
        campo_usuario.focus()


app = ctk.CTk()
app.title('Sistema de Login')
centralizar_janela(app, 300, 300)

label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu Usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

app.mainloop()
