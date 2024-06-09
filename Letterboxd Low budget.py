class Filme:

    def __init__(self, usuario, nome, nota, review):
        self.usuario = usuario
        self.nome = nome
        self.nota = nota
        self.review = review

    @staticmethod
    def msg1():
        print("Cadastro de Filmes")

    @staticmethod
    def msg2():
        print("Encerramento de sessão.")

    @staticmethod
    def menu():
        print("\nMenu de Opções:")
        print("1. Cadastrar Filme")
        print("2. Lista de Filmes")
        print("3. Remover Filme")
        print("4. Atualizar Nota")
        print("5. Buscar Filme")
        print("6. Exibir Estatísticas")
        print("7. Salvar Lista de Filmes")
        print("8. Modificar Review")
        print("9. Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def cadfilm(filmes, usuario):
        nome = input("Digite o nome do filme: ")
        nota = int(input("Digite a nota para o filme (1 a 10): "))
        while nota < 1 or nota > 10:
            nota = int(input("Nota inválida. Digite uma nota de 1 a 10: "))
        review = input("Digite a review do filme: ")
        filmes.append(Filme(usuario, nome, nota, review))
        print("Filme cadastrado.")

    @staticmethod
    def lista(filmes):
        print("\nLista de Filmes Cadastrados:")
        if not filmes:
            print("Nenhum filme cadastrado.")
        else:
            for i, filme in enumerate(filmes, start=1):
                print(
                    f"{i}. Usuário: {filme.usuario}, Filme: {filme.nome}, Nota: {filme.nota}, Review: {filme.review}"
                )

    @staticmethod
    def remover_filme(filmes):
        indice = int(input("Digite o índice do filme a ser removido: "))
        if 1 <= indice <= len(filmes):
            filmes.pop(indice - 1)
            print("Filme removido com sucesso!")
        else:
            print("Índice inválido.")

    @staticmethod
    def atualizar_nota(filmes):
        indice = int(input("Digite o índice do filme para atualizar a nota: "))
        if 1 <= indice <= len(filmes):
            nova_nota = int(
                input("Digite a nova nota para o filme (1 a 10): "))
            while nova_nota < 1 or nova_nota > 10:
                nova_nota = int(
                    input("Nota inválida. Digite uma nota de 1 a 10: "))
            filmes[indice - 1].nota = nova_nota
            print("Nota atualizada com sucesso!")
        else:
            print("Índice inválido.")

    @staticmethod
    def atualizar_review(filmes):
        indice = int(
            input("Digite o índice do filme para atualizar a review: "))
        if 1 <= indice <= len(filmes):
            nova_review = input("Digite a nova review para o filme: ")
            filmes[indice - 1].review = nova_review
            print("Review atualizada com sucesso!")
        else:
            print("Índice inválido.")

    @staticmethod
    def buscar_filme(filmes):
        nome = input("Digite o nome do filme para buscar: ")
        encontrado = False
        for filme in filmes:
            if filme.nome.lower() == nome.lower():
                print(
                    f"Usuário: {filme.usuario}, Filme: {filme.nome}, Nota: {filme.nota}, Review: {filme.review}"
                )
                encontrado = True
        if not encontrado:
            print("Filme não encontrado.")

    @staticmethod
    def exibir_estatisticas(filmes):
        if not filmes:
            print("Nenhum filme cadastrado.")
            return

        soma_notas = sum(filme.nota for filme in filmes)
        maior_nota = max(filmes, key=lambda filme: filme.nota)
        menor_nota = min(filmes, key=lambda filme: filme.nota)
        media_notas = soma_notas / len(filmes)

        print(f"Média das notas: {media_notas:.2f}")
        print(f"Filme com maior nota: {maior_nota.nome} ({maior_nota.nota})")
        print(f"Filme com menor nota: {menor_nota.nome} ({menor_nota.nota})")

    @staticmethod
    def salvar_lista(filmes):
        with open("filmes.txt", "w") as arquivo:
            for filme in filmes:
                arquivo.write(
                    f"Usuário: {filme.usuario}, Filme: {filme.nome}, Nota: {filme.nota}, Review: {filme.review}\n"
                )
        print("Lista de filmes salva com sucesso em 'filmes.txt'.")

    @staticmethod
    def executar_sistema():
        print("Digite seu nome:")
        usuario = input()
        print(
            f"Olá, {usuario}. bem-vindo ao novissímo e inovador sistema de cadastro de filmes, carinhosamente chamado de Letterboxd Low budget!"
        )

        filmes = []

        executando = True
        while executando:
            opcao = Filme.menu()

            menu_opcoes = {
                1: lambda: Filme.cadfilm(filmes, usuario),
                2: lambda: Filme.lista(filmes),
                3: lambda: Filme.remover_filme(filmes),
                4: lambda: Filme.atualizar_nota(filmes),
                5: lambda: Filme.buscar_filme(filmes),
                6: lambda: Filme.exibir_estatisticas(filmes),
                7: lambda: Filme.salvar_lista(filmes),
                8: lambda: Filme.atualizar_review(filmes),
                9: lambda: Filme.encerrar_sessao()
            }

            funcao_escolhida = menu_opcoes.get(
                opcao, lambda: print("Digite uma opção válida (1-9)."))
            funcao_escolhida()

            if opcao == 9:
                executando = False

            if executando:
                continuar = input(
                    "Deseja continuar no sistema? (s/n): ").strip().lower()
                if continuar != 's':
                    executando = False
                    Filme.encerrar_sessao()

    @staticmethod
    def encerrar_sessao():
        print("Sessão encerrada.")


if __name__ == "__main__":
    Filme.executar_sistema()
