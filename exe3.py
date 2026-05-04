import json

lista_alunos = []

def cadastrar():
    nome = input("Digite o nome do aluno: ")
    
    while True:
        try:
            nota = float(input("Digite a nota (de 0 até 10): "))
            if nota >= 0 and nota <= 10:
                break # Nota está certa! Pode sair do aviso
            else:
                print("A nota precisa ser entre 0 e 10!")
        except:
            print("Isso não é um número! Digite a nota com números.")
    
    aluno = {"nome": nome, "nota": nota}
    lista_alunos.append(aluno)
    print("Aluno salvo!")


def ver_aprovados():
    print("--- QUEM PASSOU (Nota 7 ou mais) ---")
    for item in lista_alunos:
        if item["nota"] >= 7:
            print("Nome:", item["nome"])

def ver_reprovados():
    print("--- QUEM REPROVOU (Nota menor que 7) ---")
    for item in lista_alunos:
        if item["nota"] < 7:
            print("Nome:", item["nome"])

def salvar_no_arquivo():
    arquivo = open("turma.json", "w")
    json.dump(lista_alunos, arquivo)
    arquivo.close()
    print("Arquivo criado com sucesso!")

# --- O MENU DO PROGRAMA ---
while True:
    print("\nO QUE VOCÊ DESEJA FAZER?")
    print("1 - Cadastrar Aluno")
    print("2 - Ver Aprovados")
    print("3 - Ver Reprovados")
    print("4 - Salvar no Computador")
    print("5 - Sair")
    
    escolha = input("Escolha o número: ")

    if escolha == "1":
        cadastrar()
    elif escolha == "2":
        ver_aprovados()
    elif escolha == "3":
        ver_reprovados()
    elif escolha == "4":
        salvar_no_arquivo()
    elif escolha == "5":
        print("Tchau! Até a próxima.")
        break
    else:
        print("Opção não existe, tente de novo.")