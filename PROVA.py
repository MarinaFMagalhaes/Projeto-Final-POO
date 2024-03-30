import tkinter as tk
from tkinter import simpledialog, messagebox

class Livro:
    def __init__(self, titulo, autor, ID):
        self.titulo = titulo
        self.autor = autor
        self.ID = ID
        self.emprestado = False

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.registro_membros = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.registro_membros.append(membro)

    def emprestar_livro(self, livro, membro):
        for livro_emprestado in self.catalogo:
            if livro_emprestado == livro:
                if livro_emprestado.emprestado:
                    messagebox.showinfo("Erro", "Livro já emprestado.")
                    return
                else:
                    livro_emprestado.emprestado = True
                    membro.historico_emprestimos.append(livro_emprestado)
                    messagebox.showinfo("Sucesso", "Livro emprestado com sucesso.")
                    return
        messagebox.showinfo("Erro", "Livro não encontrado.")

    def devolver_livro(self, livro, membro):
        for livro_devolvido in membro.historico_emprestimos:
            if livro_devolvido == livro:
                livro_devolvido.emprestado = False
                membro.historico_emprestimos.remove(livro_devolvido)
                messagebox.showinfo("Sucesso", "Livro devolvido com sucesso.")
                return
        messagebox.showinfo("Erro", "Este livro não está registrado como emprestado por este membro.")

    def pesquisar_livro(self, termo_pesquisa):
        resultados = []
        for livro in self.catalogo:
            if termo_pesquisa.lower() in livro.titulo.lower() or termo_pesquisa.lower() in livro.autor.lower() or termo_pesquisa == livro.ID:
                resultados.append(livro)
        return resultados

class BibliotecaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciamento de Biblioteca")

        self.biblioteca = Biblioteca()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Bem-vindo à Biblioteca")
        self.label.grid(row=0, columnspan=2)

        self.btn_add_livro = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.btn_add_livro.grid(row=1, column=0, pady=5)

        self.btn_add_membro = tk.Button(self.frame, text="Adicionar Membro", command=self.adicionar_membro)
        self.btn_add_membro.grid(row=1, column=1, pady=5)

        self.btn_emprestar_livro = tk.Button(self.frame, text="Emprestar Livro", command=self.emprestar_livro)
        self.btn_emprestar_livro.grid(row=2, column=0, pady=5)

        self.btn_devolver_livro = tk.Button(self.frame, text="Devolver Livro", command=self.devolver_livro)
        self.btn_devolver_livro.grid(row=2, column=1, pady=5)

        self.entry_pesquisa = tk.Entry(self.frame)
        self.entry_pesquisa.grid(row=3, column=0, columnspan=2, pady=5)

        self.btn_pesquisar = tk.Button(self.frame, text="Pesquisar", command=self.pesquisar)
        self.btn_pesquisar.grid(row=4, column=0, columnspan=2, pady=5)

    def adicionar_livro(self):
        titulo = simpledialog.askstring("Adicionar Livro", "Digite o título do livro:")
        autor = simpledialog.askstring("Adicionar Livro", "Digite o autor do livro:")
        ID = simpledialog.askstring("Adicionar Livro", "Digite o ID do livro:")
        livro = Livro(titulo, autor, ID)
        self.biblioteca.adicionar_livro(livro)
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso.")

    def adicionar_membro(self):
        nome = simpledialog.askstring("Adicionar Membro", "Digite o nome do membro:")
        numero_membro = simpledialog.askstring("Adicionar Membro", "Digite o número de membro:")
        membro = Membro(nome, numero_membro)
        self.biblioteca.adicionar_membro(membro)
        messagebox.showinfo("Sucesso", "Membro adicionado com sucesso.")

    def emprestar_livro(self):
        titulo = simpledialog.askstring("Emprestar Livro", "Digite o título do livro:")
        membro_nome = simpledialog.askstring("Emprestar Livro", "Digite o nome do membro:")
        
        livro_encontrado = None
        membro_encontrado = None

        for livro in self.biblioteca.catalogo:
            if livro.titulo.lower() == titulo.lower():
                livro_encontrado = livro
        for membro in self.biblioteca.registro_membros:
            if membro.nome.lower() == membro_nome.lower():
                membro_encontrado = membro

        if livro_encontrado is None:
            messagebox.showinfo("Erro", "Livro não encontrado.")
            return
        elif membro_encontrado is None:
            messagebox.showinfo("Erro", "Membro não encontrado.")
            return
        
        self.biblioteca.emprestar_livro(livro_encontrado, membro_encontrado)

    def devolver_livro(self):
        titulo = simpledialog.askstring("Devolver Livro", "Digite o título do livro:")
        membro_nome = simpledialog.askstring("Devolver Livro", "Digite o nome do membro:")
        
        livro_encontrado = None
        membro_encontrado = None

        for livro in self.biblioteca.catalogo:
            if livro.titulo.lower() == titulo.lower():
                livro_encontrado = livro
        for membro in self.biblioteca.registro_membros:
            if membro.nome.lower() == membro_nome.lower():
                membro_encontrado = membro

        if livro_encontrado is None:
            messagebox.showinfo("Erro", "Livro não encontrado.")
            return
        elif membro_encontrado is None:
            messagebox.showinfo("Erro", "Membro não encontrado.")
            return
        
        self.biblioteca.devolver_livro(livro_encontrado, membro_encontrado)

    def pesquisar(self):
        termo_pesquisa = self.entry_pesquisa.get()
        resultados = self.biblioteca.pesquisar_livro(termo_pesquisa)
        if resultados:
            mensagem = "Livros encontrados:\n"
            for livro in resultados:
                mensagem += f"Título: {livro.titulo}, Autor: {livro.autor}, ID: {livro.ID}\n"
            messagebox.showinfo("Resultados da Pesquisa", mensagem)
        else:
            messagebox.showinfo("Resultados da Pesquisa", "Nenhum livro encontrado.")

def main():
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()