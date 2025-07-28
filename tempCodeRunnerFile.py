customtkinter as ctk

ctk.set_appearance_mode('dark')


def validar_login():
    usuario = campo_usuario.get().strip().lower()
    senha = campo_senha.get()

    usuario_correto = 'antonio'
    senha_correta = '123456'
import
    if usuario == usuario_correto and senha == senha_correta:
        resultado_login.configure(text='Login feito com sucesso!!', text_color='green')
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

app =  ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu Usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha',show='*')
campo_senha.pack(pady=10)

botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

app.mainloop()
