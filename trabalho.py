i=0
while i!=5:
    arquivo = open("cadastros.txt", "r")
    conteu = arquivo.read()
    arquivo.close()
    arquivo = open("cadastros.txt", "w")
    arquivo.write(conteu)
    arquivo.close()
    print("MENU")
    opcao=float(input( "1 - Cadastrar \n2 - Ler \n3 - Atualizar \n4 - Deletar \n5 - Sair\n" ))
    if opcao == 1:
        arquivo = open("cadastros.txt", "w")
        print(" Insira seus dados: ")
        nome = (input("\nNome: "))
        cpf = (input("\nCPF: "))
        endereco = (input("\nEndereço: "))
        celular = (input("\nCelular: "))
        email = (input("\nE-mail: "))
        senha = (input("\nSenha: "))
        arquivo.write("%s\n" %nome)
        arquivo.write("%s\n" %cpf)
        arquivo.write("%s\n" %endereco)
        arquivo.write("%s\n" %celular)
        arquivo.write("%s\n" %email)
        arquivo.write("%s\n" %senha)
    arquivo.close()
    if opcao ==2:
        arquivo = open('cadastros.txt', 'r')
        string = arquivo.read()
        print(string)
    arquivo.close()
    if opcao == 3: 
        print("Qual campo você deseja atualizar?:")
        opcao=float(input("Escolha uma opção: \n1 - Nome \n2 - CPF  \n3 - Endereço \n4 - Celular \n5 - E-mail \n6 - Senha \n7 - Todas as opções\n"))
        if opcao==1:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[0]=input("Novo nome: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==2:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[1]=input("Novo CPF: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==3:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[2]=input("Novo endereço: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==4:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[3]=input("Novo celular: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==5:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[4]=input("Novo e-mail: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==6:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[5]=input("Novo senha: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==7:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[0]=input("Novo nome: ")
            lista[1]=input("Novo CPF: ")
            lista[2]=input("Novo endereço: ")
            lista[3]=input("Novo celular: ")
            lista[4]=input("Novo e-mail: ")
            lista[5]=input("Novo senha: ")
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
    if opcao==4:
        print("Qual campo você deseja deletar?:")
        opcao=float(input("Escolha uma opção: \n1 - Nome \n2 - CPF  \n3 - Endereço \n4 - Celular \n5 - E-mail \n6 - Senha \n7 - Todas as opções\n"))
        if opcao==1:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[0]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==2:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[1]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==3:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[2]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==4:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[3]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==5:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[4]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==6:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[5]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
        if opcao==7:
            arquivo = open("cadastros.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()
            lista=[s.replace("\n","") for s in lista]
            lista[0]=""
            lista[1]=""
            lista[2]=""
            lista[3]=""
            lista[4]=""
            lista[5]=""
            arquivo = open("cadastros.txt", "w")
            for i in lista:
                arquivo.write("%s\n"%i)
            arquivo.close()
    if opcao==5:
        arquivo = open("cadastros.txt", "r")
        conteu = arquivo.read()
        arquivo.close()
        arquivo = open("cadastros.txt", "w")
        arquivo.write(conteu)
        opcao=float(input("Você deseja sair do sistema? \n 1 - SIM\n 2 - NÃO\n"))
        if opcao==1:
            print("Programa finalizado")
            i=5
        else:
            i=i+0
    arquivo.close()