def juros_simples():
    print("Teste juro simples")
    C = float(input("Capital inicial: "))
    i = float(input("Taxa de juros mensal: "))
    t = float(input("Tempo(meses): "))

    J = C * i * t
    M = C + J

    print(f"\n Juros acumulados: R${J:.2f}")
    print(f"Montante final: R${M:.2f}") 

juros_simples()