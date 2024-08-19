
nome_produtos =["Cabo-USB","Teclado","Monitor"]
valor = ["10.00","60.00","500.00"]
quantidade = ["5","10","25"]

menu = """
        1 - Print lista
        2 - Retirar item 
        3 - Adicionar item
        """


while True:
    print(menu)
    entrada = input("___Digite a opção: ")
    if entrada == "0":
        print("sair")
        break
    
    if entrada == "1":
        for i in range(len(nome_produtos)):
            print(f"{i} - Produto: {nome_produtos[i]} - Valor: {valor[i]} - Quantidade: {quantidade[i]}  ")
    
    if entrada == "2":
        retirar =  int(input( "Digite o numero a retirar: "))
        iten_removido = nome_produtos.pop(retirar)
        print(f"Item Retirado da lista - {iten_removido}")
    
    if entrada =="3":
        prod = input("Digite o produto: ")
        val = float(input("Digite o valor: "))
        qtd = int(input("Digite a quantidade: "))
        nome_produtos.append(prod)
        valor.append(val)
        quantidade.append(qtd)

        
       
    
    
    
   

    
nome_produtos =["Cabo-USB","Teclado","Monitor"]
valor = ["10.00","60.00","500.00"]
quantidade = ["5","10","25"]








