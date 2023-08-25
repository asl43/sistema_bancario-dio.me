def menu():
    menu = ('''\n
    ==========MENU==========
[D]  - Depositar
[S]  - Sacar
[E]  - Extrato
[nc] - Nova conta
[lc] - Listar contas
[nu] - Novo usuário
[Q]  - Sair
-- ''')
    return input(menu)


def depositar(saldo, valor, extrato, /): # Regra do depósito é que os valores sejam por posição, por isso a /.
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # Regra saque: nomeada. Keywords only. Definida por * no início.
       
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não possui saldo suficiente!")

    elif excedeu_limite:
        print("Operação falou! O valor máximo para saque é de R$ 500,00.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques atingidos. Você pode realizar até três saques diários.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques +=1
        print("\n Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato): #receber argumentos positional only / e * keyword only.
    print("\n========== Extrato ==========")
    print(extrato)
    print("Não foram realizadas transações." if not extrato else extrato)
    print(f"\nSaldo final:\t\tR${saldo:.2f}")
    print("=============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse CPF já está cadastrado por um usuário!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) #adiciona como dict

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print('Usuário não encontrado!')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = LIMITE_SAQUES
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques
        
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1 # len cria uma sequência de contas.
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()