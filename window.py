import tkinter as tk

root = tk.Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.Tela()
        self.set_frames()
        self.widgets_frame1()
        root.mainloop()

    def Tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background= 'blue')
        self.root.geometry("550x400")
        self.root.resizable(True, True)
        
    def set_frames(self):
        self.frame_1 = tk.Frame(self.root, bd = 4, bg = "lightblue", 
                                highlightbackground= "darkblue", highlightthickness= 3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)   
        self.frame_2 = tk.Frame(self.root, bd = 4, bg = "lightblue", 
                                highlightbackground= "darkblue", highlightthickness= 3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        ## Botão Limpar
        self.bt_limpar = tk.Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.19, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Buscar
        self.bt_buscar = tk.Button(self.frame_1, text="Buscar")
        self.bt_buscar.place(relx=0.32, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Novo
        self.bt_novo = tk.Button(self.frame_1, text="Novo")
        self.bt_novo.place(relx=0.55, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Alterar
        self.bt_alterar = tk.Button(self.frame_1, text="Alterar")
        self.bt_alterar.place(relx=0.68, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Apagar
        self.bt_apagar = tk.Button(self.frame_1, text="Apagar")
        self.bt_apagar.place(relx=0.81, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Labels Codigo
        self.lb_codigo = tk.Label(self.frame_1, text="Codigo", bg="lightblue")
        self.lb_codigo.place(relx=0.01, rely=0.02, relwidth=0.12, relheight=0.15)

        ## Entry Codigo
        self.input_codigo = tk.Entry(self.frame_1)
        self.input_codigo.place(relx=0.02, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Labels Nome
        self.lb_nome = tk.Label(self.frame_1, text="Nome", bg="lightblue")
        self.lb_nome.place(relx=0.0001, rely=0.35, relwidth=0.12, relheight=0.15)

        ## Entry Nome
        self.input_nome = tk.Entry(self.frame_1)
        self.input_nome.place(relx=0.02, rely=0.48, relwidth=0.5, relheight=0.15)

        ## Labels CPF
        self.lb_cpf = tk.Label(self.frame_1, text="CPF", bg="lightblue")
        self.lb_cpf.place(relx=0.52, rely=0.33, relwidth=0.12, relheight=0.15)

        ## Entry CPF
        self.input_cpf = tk.Entry(self.frame_1)
        self.input_cpf.place(relx=0.55, rely=0.48, relwidth=0.435, relheight=0.15)

        ## Labels Telefone
        self.lb_tel = tk.Label(self.frame_1, text="Telefone", bg="lightblue")
        self.lb_tel.place(relx=0.009, rely=0.65, relwidth=0.12, relheight=0.15)

        ## Entry Telefone
        self.input_tel = tk.Entry(self.frame_1)
        self.input_tel.place(relx=0.02, rely=0.78, relwidth=0.3, relheight=0.15)

        ## Labels Cidade
        self.lb_cidade = tk.Label(self.frame_1, text="Cidade", bg="lightblue")
        self.lb_cidade.place(relx=0.52, rely=0.65, relwidth=0.12, relheight=0.15)

        ## Entry Cidade
        self.input_cidade = tk.Entry(self.frame_1)
        self.input_cidade.place(relx=0.55, rely=0.78, relwidth=0.435, relheight=0.15)

Aplication()
