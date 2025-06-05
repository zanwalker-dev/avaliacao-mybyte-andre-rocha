def juros_simples():
    print("Calculo de juros simples")
    C = float(input("Capital inicial: "))
    i = float(input("Taxa de juros mensal(%): ")) / 100
    t = float(input("Tempo(meses): "))

    J = C * i * t
    M = C + J

    print(f"\nJuros acumulados: R${J:.2f}")
    print(f"Montante final: R${M:.2f}") 

def juros_composto():
    print("Calculo de Juros Compostos")
    C = float(input("Capital inicial: "))
    i = float(input("Taxa de juros mensal(%): ")) / 100
    t = float(input("Tempo(meses): "))

    M = C * (1 + i) ** t
    J = M - C

    print(f"\nJuros acumulados: R$ {J:.2f}")
    print(f"Montante final: {M:.2f}")

def valor_presente():

    VF = float(input("Valor futuro: "))
    i = float(input("Taxa de juros mensal(%): ")) / 100
    t = float(input("Tempo(meses): "))

    VP = VF / (1 + i) ** t

    print(f"\nValor presente: R$ {VP:.2f}")

def menu():
    while True:
        print("\n ==< Calculadora Financeira >==")
        print("1. Juros Simples")
        print("2. Juros Composto")
        print("3. Valor Presente")
        print("0. Sair")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            juros_simples()
        elif option == "2":
            juros_composto()
        elif option == "3":
            valor_presente()
        elif option == "0":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
