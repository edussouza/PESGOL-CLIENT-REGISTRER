import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from register import * 

root = tk.Tk()

class Aplication():

    client_list = []
    
    counterId = 0
    
    def __init__(self):
        self.root = root
        self.Tela()
        self.set_frames()
        self.widgets_frame1()
        self.widgets_frame2()
        root.mainloop()

    def Tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background= 'blue')
        self.root.geometry("700x500")
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
        self.bt_limpar = tk.Button(self.frame_1, text="Limpar", border=2, bg="white",
                                    fg="black", font=("Verdana", 8, "bold"), command=self.bttn_clear)
        self.bt_limpar.place(relx=0.19, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Buscar
        self.bt_buscar = tk.Button(self.frame_1, text="Buscar", border=2, bg="white",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.bt_buscar.place(relx=0.32, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Novo
        self.bt_novo = tk.Button(self.frame_1, text="Novo", border=2, bg="white",
                                    fg="black", font=("Verdana", 8, "bold"), command=self.bttn_new)
        self.bt_novo.place(relx=0.55, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Alterar
        self.bt_alterar = tk.Button(self.frame_1, text="Alterar", border=2, bg="white",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.bt_alterar.place(relx=0.68, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Botão Apagar
        self.bt_apagar = tk.Button(self.frame_1, text="Apagar", border=2, bg="white",
                                    fg="black", font=("Verdana", 8, "bold"), command=self.bttn_delete)
        self.bt_apagar.place(relx=0.81, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Labels Codigo
        self.lb_codigo = tk.Label(self.frame_1, text="Codigo", bg="lightblue",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.lb_codigo.place(relx=0.01, rely=0.02, relwidth=0.12, relheight=0.15)

        ## Entry Codigo
        self.input_codigo = tk.Entry(self.frame_1)
        self.input_codigo.place(relx=0.02, rely=0.15, relwidth=0.12, relheight=0.15)

        ## Labels Nome
        self.lb_nome = tk.Label(self.frame_1, text="Nome", bg="lightblue",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.lb_nome.place(relx=0.0001, rely=0.35, relwidth=0.12, relheight=0.15)

        ## Entry Nome
        self.input_nome = tk.Entry(self.frame_1)
        self.input_nome.place(relx=0.02, rely=0.48, relwidth=0.5, relheight=0.15)

        ## Labels CPF
        self.lb_cpf = tk.Label(self.frame_1, text="CPF", bg="lightblue",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.lb_cpf.place(relx=0.52, rely=0.33, relwidth=0.12, relheight=0.15)

        ## Entry CPF
        self.input_cpf = tk.Entry(self.frame_1)
        self.input_cpf.place(relx=0.55, rely=0.48, relwidth=0.435, relheight=0.15)

        ## Labels Telefone
        self.lb_tel = tk.Label(self.frame_1, text="Telefone", bg="lightblue",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.lb_tel.place(relx=0.009, rely=0.65, relwidth=0.12, relheight=0.15)

        ## Entry Telefone
        self.input_tel = tk.Entry(self.frame_1)
        self.input_tel.place(relx=0.02, rely=0.78, relwidth=0.3, relheight=0.15)

        ## Labels Cidade
        self.lb_cidade = tk.Label(self.frame_1, text="Cidade", bg="lightblue",
                                    fg="black", font=("Verdana", 8, "bold"))
        self.lb_cidade.place(relx=0.54, rely=0.65, relwidth=0.12, relheight=0.15)

        ## Entry Cidade
        self.input_cidade = tk.Entry(self.frame_1)
        self.input_cidade.place(relx=0.55, rely=0.78, relwidth=0.435, relheight=0.15)
        
    def widgets_frame2(self):
        ## Treeview
        self.listClient = ttk.Treeview(self.frame_2, height=3,
        columns=("col0", "col1", "col2", "col3", "col4", "col5"))
        self.listClient.heading("#0", text="")
        self.listClient.heading("#1", text="Codigo")
        self.listClient.heading("#2", text="Nome")
        self.listClient.heading("#3", text="CPF")
        self.listClient.heading("#4", text="Telefone")
        self.listClient.heading("#5", text="Cidade")

        self.listClient.column("#0", width=5)
        self.listClient.column("#1", width=50)
        self.listClient.column("#2", width=150)
        self.listClient.column("#3", width=100)
        self.listClient.column("#4", width=100)
        self.listClient.column("#5", width=150)

        self.listClient.place(relx=0.01, rely=0.1, relheight=0.85, relwidth=0.95)
        
        self.scrollLista = tk.Scrollbar(self.frame_2, orient='vertical')
        self.listClient.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

    def bttn_new(self):
        self.client_list.append(Register(self.counterId + 1, self.input_nome.get(), self.input_cpf.get(),
        self.input_tel.get(), self.input_cidade.get()))
        self.counterId += 1
        # print(self.client_list[0].__str__())
        
        tk.messagebox.showinfo(title="Aviso", message="Cliente adicionado")
        
        self.listClient.delete(*self.listClient.get_children())
        
        for client in self.client_list:
            self.listClient.insert("", tk.END, values=client)
        
    def bttn_clear(self):
        self.input_nome.delete(0, 'end')
        self.input_cidade.delete(0, 'end')
        self.input_codigo.delete(0, 'end')
        self.input_cpf.delete(0, 'end')
        self.input_tel.delete(0, 'end')

    def bttn_update(self):
        return
    
    def bttn_delete(self):
        self.selected_item = self.listClient.selection()[0]
        
        self.client_list.pop(self.selected_item)
        
        tk.messagebox.showinfo(title="Aviso", message="Cliente removido")
        
        self.listClient.delete(self.selected_item)
        for client in self.client_list:
            self.listClient.insert("", tk.END, values=client)
           
                   

Aplication()
