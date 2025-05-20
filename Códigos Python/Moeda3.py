class Moeda:
    def __init__(self, nome, simbolo, valor_inicial=0):
        self.nome = nome
        self.simbolo = simbolo
        self.saldo = valor_inicial

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            print(f"Depositado {quantia} {self.simbolo}. Novo saldo: {self.saldo} {self.simbolo}")
        else:
            print("A quantia para depósito deve ser maior que zero.")

    def sacar(self, quantia):
        if quantia > 0 and quantia <= self.saldo:
            self.saldo -= quantia
            print(f"Sacado {quantia} {self.simbolo}. Novo saldo: {self.saldo} {self.simbolo}")
        elif quantia <= 0:
            print("A quantia para saque deve ser maior que zero.")
        else:
            print(f"Saldo insuficiente. Você tem {self.saldo} {self.simbolo}.")

    def get_saldo(self):
        return self.saldo

    def __str__(self):
        return f"{self.nome} ({self.simbolo})"

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco

    def __str__(self):
        return f"{self.nome} - {self.preco}"

class Mercado:
    def __init__(self, moeda):
        self.moeda = moeda
        self.produtos = {}

    def adicionar_produto(self, produto, quantidade=1):
        if produto in self.produtos:
            self.produtos[produto] += quantidade
        else:
            self.produtos[produto] = quantidade
        print(f"{quantidade} unidade(s) de '{produto.nome}' adicionada(s) ao mercado.")

    def listar_produtos(self):
        print("\n--- Produtos Disponíveis ---")
        if not self.produtos:
            print("Nenhum produto à venda.")
            return
        for produto, quantidade in self.produtos.items():
            print(f"- {produto} (Quantidade: {quantidade}) {self.moeda.simbolo}{produto.get_preco()}")
        print("----------------------------")

    def comprar_produto(self, cliente_carteira, produto_nome, quantidade=1):
        produto_encontrado = None
        for prod, quant in self.produtos.items():
            if prod.nome.lower() == produto_nome.lower():
                produto_encontrado = prod
                break

        if not produto_encontrado:
            print(f"Produto '{produto_nome}' não encontrado no mercado.")
            return

        if self.produtos[produto_encontrado] < quantidade:
            print(f"Quantidade insuficiente de '{produto_nome}' em estoque.")
            return

        preco_total = produto_encontrado.get_preco() * quantidade
        if cliente_carteira.saldo >= preco_total:
            cliente_carteira.sacar(preco_total)
            self.produtos[produto_encontrado] -= quantidade
            print(f"Compra realizada: {quantidade} unidade(s) de '{produto_encontrado.nome}' por {self.moeda.simbolo}{preco_total}.")
            if self.produtos[produto_encontrado] == 0:
                del self.produtos[produto_encontrado]
        else:
            print(f"Saldo insuficiente para comprar {quantidade} unidade(s) de '{produto_encontrado.nome}'.")

class Cliente:
    def __init__(self, nome, carteira):
        self.nome = nome
        self.carteira = carteira

# Inicialização
dindim = Moeda("Dindim", "DD", 100)
mercado_central = Mercado(dindim)
cliente1 = Cliente("Você", dindim) # Agora o cliente é você

# Adicionando alguns produtos iniciais ao mercado
mercado_central.adicionar_produto(Produto("Café", 3.00), 15)
mercado_central.adicionar_produto(Produto("Pão", 1.50), 30)
mercado_central.adicionar_produto(Produto("Suco", 5.00), 10)

# Loop de interação
while True:
    print("\n--- Interação com o Mercado ---")
    print("Comandos disponíveis:")
    print("  listar  - Listar os produtos disponíveis")
    print("  comprar <produto> <quantidade> - Comprar um produto (ex: comprar café 2)")
    print("  saldo   - Ver seu saldo")
    print("  sair    - Encerrar a interação")
    comando = input("Digite um comando: ").lower().split()

    if not comando:
        continue

    acao = comando[0]

    if acao == "listar":
        mercado_central.listar_produtos()
    elif acao == "comprar":
        if len(comando) == 3:
            produto_nome = comando[1]
            try:
                quantidade = int(comando[2])
                if quantidade > 0:
                    mercado_central.comprar_produto(cliente1.carteira, produto_nome, quantidade)
                else:
                    print("A quantidade deve ser maior que zero.")
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro.")
        else:
            print("Uso correto: comprar <produto> <quantidade>")
    elif acao == "saldo":
        print(f"Seu saldo atual: {cliente1.carteira.get_saldo()} {cliente1.carteira.simbolo}")
    elif acao == "sair":
        print("Obrigado por interagir com o mercado!")
        break
    else:
        print("Comando inválido. Tente novamente.")
