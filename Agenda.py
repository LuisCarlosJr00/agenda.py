
#AGENDA TELEFONICA 
''' 
  Dados:
        nome, telefone, email    
  ->> Menu
        1 - Cadastrar um contato
        2 - Pesquisar um contato (nome ou telefone)
        3 - Listar todos os contatos
        4 - Editar um contato
        5 - Excluir um contato
        6 - Sair
'''

#Funções para as opções abaixo: 
dados={}
lista_dados = []       #Cria uma lista pra adicionar os dados do cadastro em cada ítem dela.
def cadastrar():#tudo ok
    print("-="*30)
    dados["nome"] = input("Nome: ")
    dados["telefone"] = int(input("Telefone: "))
    dados["email"] = input("E-mail: ")
    lista_dados.append(dados.copy())
    
def pesquisar():# +_
        while True:
            pesquisa = input("Digite sua pesquisa(nome ou telefone): ")
            for i in range (0,len(lista_dados)):
                        if pesquisa == (lista_dados[i]['nome']):
                            print(f' Dados: \n Nome: {lista_dados[i]["nome"]}, Telefone: {lista_dados[i]["telefone"]}, Email: {lista_dados[i]["email"]}')
                        elif int(pesquisa) == (lista_dados[i]['telefone']): 
                            print(f' Dados: \n Nome: {lista_dados[i]["nome"]}, Telefone: {lista_dados[i]["telefone"]}, Email: {lista_dados[i]["email"]}')
                        else: 
                            print("ERRO! Digite um número ou telefone válido!")
            break

def listar():#tudo ok
    for i in range (0,len(lista_dados)):
        if i <= (len(lista_dados[i])):
            print("-="*30)
            print(f' Dados: \n Nome: {lista_dados[i]["nome"]}, Telefone: {lista_dados[i]["telefone"]}, Email: {lista_dados[i]["email"]}')
            i+=1
           
def editar(): #tudo ok 
    print(listar())
    edita = input("Escolha o NOME do contato que deseja editar de acordo com a lista acima: ")
    for i in range (0,len(lista_dados)):
                if edita == (lista_dados[i]['nome']):
                    lista_dados[i]["nome"] = input("Nome: ")
                    lista_dados[i]["telefone"] = int(input("Telefone: "))
                    lista_dados[i]["email"] = input("E-mail: ")
                    print(f' Modificação: \n Nome: {lista_dados[i]["nome"]}, Telefone: {lista_dados[i]["telefone"]}, Email: {lista_dados[i]["email"]}')
                    opcao = str(input("Deseja salvar a edição[S/N]: ")).upper()[0]
                    if opcao == 'S':
                        print("-="*30)
                        print("Edição salva!")
                        print(listar())
                        print("-="*30)
                    else: 
                        print("-="*30)
                        print("Edição não salva!")
                        print("-="*30)
                        break
                        
def excluir(): #todo ok
    print("-="*30)
    print(listar())
    excluir = input("Defina o NOME contato deseja excluir: ")     
    for i in range (0,len(lista_dados)):
        if excluir == lista_dados[i]['nome']:
            del(lista_dados[i])
    print("-="*30)
    print(listar())
    print("-="*30)
      
def menu():#ok
    print("-="*30)
    print("      Menu        ")
    print("-="*30)
    print('''1 - Cadastrar um contato
2 - Pesquisar um contato (nome ou telefone)
3 - Listar todos os contatos
4 - Editar um contato
5 - Excluir um contato
6 - Sair ''')

def fim():  #ok  
    print("="*30)
    print("      OPERAÇÃO FINALIZADA        ")
    print("="*30)

#Menu opções:

print (menu())
escolha = 0
while escolha !=6: 
    escolha = int(input("Escolha uma das opções acima: "))
    if escolha == 1:
        cadastrar()
        print(menu())
    elif escolha ==2:
        pesquisar()
        print(menu())
    elif escolha == 3:
        listar()
        print(menu())
    elif escolha ==4:
        editar()
        print(menu())
    elif escolha == 5:
        excluir()
        print(menu())
    elif escolha ==6:
        print (fim())
        break
    


