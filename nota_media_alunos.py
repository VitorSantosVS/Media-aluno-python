#Exercicio da Lista

lista_da_turma = [] #Lista criada para armazenar os dados que serão inseridos pelo usuário

#Função que retorna os dados registrados na lista
def registro_de_aluno(nome, nota, endereco):
    return {"nome": nome, "nota": nota, "endereco": endereco}
#Função que registra os alunos na lista criada

def grava_registro_de_aluno(nome, nota, endereco):
    lista_da_turma.append(registro_de_aluno(nome, nota, endereco))    

#Função que pega o tamanho da lista
def tamanho():
     return len(lista_da_turma) #a função len(), que é do próprio Python, calcula o numero de ELEMENTOS presentes na lista/string/vetor (serve para tamanho kkk)

soma_notas=0 #Variável responsável por somar quantas notas foram publícadas

tam=0 #Variável responsável por por pegar o tamanho

resp=1 #Variável responsável por controlar o while abaixo. Ela começa recebendo 1 para que o While funcione desde a primeira tentativa.

#Condição que faz com que o usuário insira os dados e, ao final, pergunte se ele gostaria de continuar. Enquanto a resposta for 1, ele irá repetir o loop
while (resp==1):
    #comandos para o usuario adicionar os dados 
    nome2= input("adicione o nome: ")
    nota2= float(input("adicione a nota: "))
    soma_notas+=nota2 #Variável responsável por somar as notas dos alunos
    #Condição que garante que a nota não será maior que 10 ou menor que 0
    while(nota2>10 or nota2<0):
        nota2= float(input("Nota inválida! Por favor, tente novamente. \n Adicione a nota: "))
    endereco2 = input("adicione o endereco: ")
    
    #comando para passar os parametros ao metodo e a lista
    grava_registro_de_aluno(nome2,nota2,endereco2)
    resp=int(input("Continuar? [1/0]")) #A variavel recebe a nova entrada do usuário perguntando se ele quer continuar adicionando dados à lista
    tam = tamanho() #Variável responsável por por pegar o tamanho da lista

#Sessão dos Prints, onde a 1ª linha printa o nº de alunos cadastrados e a 2ª printa os elementos da lista
print("o numero de alunos cadastrados é: ",tamanho()) #Aqui se faz a chamada do método tamanho(), que retorna o numero de ELEMENTOS presentes na lista
print(lista_da_turma)

#teste de media
print("A média da turma é: ",soma_notas/tam) #Print da media de todas as notas da turma
