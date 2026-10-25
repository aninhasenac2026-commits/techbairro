"""
TechBairro — aplicativo desktop para cadastro de clientes.
Execute no terminal: python techbairro.py
"""

import os
import sqlite3
import tkinter as tk
from tkinter import messagebox

from banco import GerenciadorClientes
from cliente import Cliente
from validacao import ValidadorCliente

VERSAO = "3.3.1"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(BASE_DIR, "techbairro.db")


class TechBairroApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title(f"TechBairro v{VERSAO} — Cadastro de Clientes")
        self.raiz.geometry("650x410")
        self.raiz.minsize(590, 380)
        self.gerenciador = GerenciadorClientes(CAMINHO_BANCO)
        self.validador = ValidadorCliente()
        self.id_em_edicao = None
        self.entradas = {}

        tk.Label(raiz, text=f"TechBairro — v{VERSAO}",
                 font=("Arial", 16, "bold")).pack(pady=(10, 3))

        formulario = tk.Frame(raiz)
        formulario.pack(padx=16, fill="x")
        for linha, campo in enumerate(("Nome", "Telefone", "E-mail", "Endereço")):
            tk.Label(formulario, text=campo, width=12, anchor="w").grid(
                row=linha, column=0, padx=4, pady=4, sticky="w")
            entrada = tk.Entry(formulario)
            entrada.grid(row=linha, column=1, padx=4, pady=4, sticky="ew")
            self.entradas[campo] = entrada
        formulario.columnconfigure(1, weight=1)

        botoes = tk.Frame(raiz)
        botoes.pack(pady=8)
        self.botao_salvar = tk.Button(botoes, text="Salvar", width=13, command=self.salvar)
        self.botao_salvar.grid(row=0, column=0, padx=4)
        tk.Button(botoes, text="Cancelar/Limpar", command=self.cancelar).grid(
            row=0, column=1, padx=4)
        tk.Button(botoes, text="Consultar clientes", command=self.abrir_consulta).grid(
            row=0, column=2, padx=4)

        self.status = tk.Label(raiz, text="Formulário pronto", fg="gray")
        self.status.pack(pady=4)
        self.contador = tk.Label(raiz, text="")
        self.contador.pack()
        self.atualizar_contador()

    def atualizar_contador(self):
        try:
            self.contador.config(text=f"Clientes cadastrados: {self.gerenciador.total()}")
        except sqlite3.Error as erro:
            self.contador.config(text="Não foi possível contar os clientes.")
            messagebox.showerror("Erro no banco", str(erro), parent=self.raiz)

    def obter_cliente_formulario(self):
        valores = {campo: entrada.get().strip()
                   for campo, entrada in self.entradas.items()}
        cliente = Cliente(valores["Nome"], valores["Telefone"],
                          valores["E-mail"], valores["Endereço"])
        erro = self.validador.validar(cliente)
        if erro:
            raise ValueError(erro)
        return cliente

    def salvar(self):
        try:
            cliente = self.obter_cliente_formulario()
            if self.id_em_edicao is None:
                self.gerenciador.cadastrar(cliente)
                self.status.config(
                    text=f"Cliente '{cliente.nome}' cadastrado com sucesso!", fg="green")
            else:
                alterou = self.gerenciador.atualizar(self.id_em_edicao, cliente)
                if not alterou:
                    self.status.config(
                        text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                        fg="red")
                    self.limpar_campos()
                    self.atualizar_contador()
                    return
                self.status.config(
                    text=f"Cliente '{cliente.nome}' atualizado com sucesso!", fg="green")
            self.limpar_campos()
            self.atualizar_contador()
        except ValueError as erro:
            messagebox.showwarning("Verifique os dados", str(erro), parent=self.raiz)
        except sqlite3.Error as erro:
            messagebox.showerror("Erro no banco",
                                 f"Não foi possível salvar o cliente.\n{erro}",
                                 parent=self.raiz)

    def limpar_campos(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.id_em_edicao = None
        self.botao_salvar.config(text="Salvar")

    def cancelar(self):
        estava_editando = self.id_em_edicao is not None
        self.limpar_campos()
        self.status.config(
            text="Edição cancelada. Nada foi alterado." if estava_editando else "Formulário limpo",
            fg="gray")

    def abrir_consulta(self):
        consulta = tk.Toplevel(self.raiz)
        consulta.title("Consulta de clientes")
        consulta.geometry("760x430")
        consulta.transient(self.raiz)

        tk.Label(consulta, text="Pesquise por nome ou selecione um cliente").pack(pady=(8, 3))
        barra = tk.Frame(consulta)
        barra.pack(fill="x", padx=10)
        tk.Label(barra, text="Nome:").pack(side="left")
        busca = tk.Entry(barra)
        busca.pack(side="left", fill="x", expand=True, padx=5)

        lista = tk.Listbox(consulta, height=13, exportselection=False)
        lista.pack(padx=10, pady=7, fill="both", expand=True)
        clientes_na_tela = []

        def atualizar_lista(clientes=None):
            lista.delete(0, tk.END)
            clientes_na_tela.clear()
            try:
                if clientes is None:
                    clientes = self.gerenciador.listar()
                for cliente in clientes:
                    lista.insert(tk.END, cliente.resumo())
                    clientes_na_tela.append(cliente)
                if not clientes:
                    lista.insert(tk.END, "Nenhum cliente cadastrado")
            except sqlite3.Error as erro:
                messagebox.showerror("Erro no banco", str(erro), parent=consulta)

        def pesquisar():
            termo = busca.get().strip()
            if not termo:
                atualizar_lista()
            else:
                atualizar_lista(self.gerenciador.buscar_por_nome(termo))

        def cliente_selecionado(acao):
            selecionado = lista.curselection()
            if not selecionado or selecionado[0] >= len(clientes_na_tela):
                messagebox.showwarning("Atenção", f"Selecione um cliente antes de {acao}.",
                                       parent=consulta)
                return None
            return clientes_na_tela[selecionado[0]]

        def editar_cliente(evento=None):
            cliente = cliente_selecionado("editar")
            if cliente is None:
                return
            self.id_em_edicao = cliente.id
            for campo, valor in (("Nome", cliente.nome), ("Telefone", cliente.telefone),
                                 ("E-mail", cliente.email), ("Endereço", cliente.endereco)):
                self.entradas[campo].delete(0, tk.END)
                self.entradas[campo].insert(0, valor)
            self.status.config(text=f"Editando cliente: {cliente.nome}", fg="blue")
            self.botao_salvar.config(text="Salvar edição")
            consulta.destroy()

        def excluir_cliente():
            cliente = cliente_selecionado("excluir")
            if cliente is None:
                return
            confirmar = messagebox.askyesno(
                "Confirmar exclusão",
                f"Tem certeza que deseja excluir este cliente?\n\n"
                f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n"
                f"E-mail: {cliente.email}\n\nEssa ação não pode ser desfeita.",
                parent=consulta)
            if not confirmar:
                return
            try:
                removeu = self.gerenciador.remover(cliente.id)
            except sqlite3.Error as erro:
                messagebox.showerror("Erro no banco",
                                     f"Não foi possível excluir o cliente.\n{erro}",
                                     parent=consulta)
                return
            if not removeu:
                messagebox.showwarning("Cliente não encontrado",
                                       "O cadastro já não existe. A lista será atualizada.",
                                       parent=consulta)
            else:
                self.status.config(
                    text=f"Cliente '{cliente.nome}' excluído com sucesso!", fg="green")
            atualizar_lista()
            self.atualizar_contador()

        botoes_consulta = tk.Frame(consulta)
        botoes_consulta.pack(pady=8)
        tk.Button(botoes_consulta, text="Buscar", command=pesquisar).grid(
            row=0, column=0, padx=4)
        tk.Button(botoes_consulta, text="Mostrar todos",
                  command=lambda: (busca.delete(0, tk.END), atualizar_lista())).grid(
            row=0, column=1, padx=4)
        tk.Button(botoes_consulta, text="Editar selecionado", command=editar_cliente).grid(
            row=0, column=2, padx=4)
        tk.Button(botoes_consulta, text="Excluir selecionado", command=excluir_cliente).grid(
            row=0, column=3, padx=4)
        tk.Button(botoes_consulta, text="Atualizar lista", command=atualizar_lista).grid(
            row=0, column=4, padx=4)
        lista.bind("<Double-Button-1>", editar_cliente)
        lista.bind("<Delete>", lambda evento: excluir_cliente())
        atualizar_lista()


if __name__ == "__main__":
    print(f"Banco em uso: {CAMINHO_BANCO}")
    try:
        janela = tk.Tk()
        TechBairroApp(janela)
        janela.mainloop()
    except sqlite3.Error as erro:
        print(f"Erro ao acessar o banco: {erro}")
        try:
            messagebox.showerror("Erro no banco", str(erro))
        except tk.TclError:
            pass
    except tk.TclError as erro:
        print(f"Não foi possível iniciar a interface gráfica: {erro}")
