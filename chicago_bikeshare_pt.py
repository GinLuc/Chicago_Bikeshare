# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])

# É o cabeçalho dos dados, para que possamos identificar as colunas.
data_columns = data_list[0]

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras\n")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]



for index in data_list:    
    if data_list.index(index) < 20:
        print("Amostra", (data_list.index(index) + 1), ": ", index, "\n")
        
    
    else:
        break
# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
#print(len(data_list_20))

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

#Variável criada para armazenar o índice do campo "Gender"
indice_genero = data_columns.index("Gender")

for i in range(0,len(data_list[:20])):
    print("Amostra", (i+1), ":", data_list[i][indice_genero])
    
input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
   
    for i in data:
        column_list.append(i[index])
            
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

male = 0
female = 0

#Variável vaizo armazena os espaços NULL presentes no campo Gender
vazio = 0

#Método de usar o .count para matrizes!!! 
for i in range(0, len(data_list)):
    male += data_list[i][indice_genero].count('Male')
    female += data_list[i][indice_genero].count('Female')
    vazio += data_list[i][indice_genero].count('')
    
#Por que que a variável VAZIO com auto incremental retorna uma valor muito grande, porém com atribuição simples
#ela retorna o valor corretamente, enquanto que as variáveis MALE e FEMALE usam auto incremento pois a atribuição simples
#não funciona?? (usado amostra de até 20 para essa análise)


     
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female, "\nVazios: ", vazio)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0
 
    for i in range(0, len(data_list)):
        if data_list[i][indice_genero] == 'Male' or data_list[i][indice_genero] == 'male':
            male += 1
        elif data_list[i][indice_genero] == 'Female' or data_list[i][indice_genero] == 'female':  
            female += 1
            
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    answer = ""
    generos = count_gender(data_list)
   
    # Checagem de Qunatidade de vezes que aparecem cada Gênero
    if generos[0] > generos[1]:
        answer = "Masculino"
    elif generos[0] < generos[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

#Variável semelhante ao indice_genero, porém para armazenar o índice do User Type
indice_usertype = data_columns.index("User Type")


#Função semelhante ao "count_gender", porém para contar os User types
def count_usertype(data_list):
    subscriber = 0
    customer = 0
    for i in range(0, len(data_list)):
        if data_list[i][indice_usertype] == 'Subscriber' or data_list[i][indice_genero] == 'subscriber':
            subscriber += 1
        elif data_list[i][indice_usertype] == 'Customer' or data_list[i][indice_genero] == 'customer':  
            customer += 1
    return [subscriber, customer]


print("\nTAREFA 7: Verifique o gráfico!")
gender_list = column_to_list(data_list, indice_usertype)
types = ["Subscriber", "Customer"]
quantity = count_usertype(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Type')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Essa resposta é invalida pois há espaços que não possuem resposta alguma, contendo apenas o NULL.\n" + \
"Portanto, a soma das respostas 'Male','Female' e os espaços que contém NULL dá o total do tamanho do data_list"

print("resposta:", answer, "\n\nmale + female + vazio == len(data_list):", male + female + vazio == len(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().

#Variável responsável por armazenar a posição do campo "Trip Duration"
indice_trip = data_columns.index('Trip Duration')

#Função para poder pegar e retornar o valor máximo de uma lista
def get_max(data_list):
    max_trip = 0
    
    for i in data_list:
        if int(i) > max_trip:
            max_trip = int(i)
            
    return max_trip

#Função para poder pegar e retornar o valor mínimo de uma lista
def get_min(data_list):
    #Captura do maior valor para que a condição seja verdadeira
    min_trip = get_max(data_list)

    for i in data_list:    
        if int(i) < min_trip:
            min_trip = int(i)
            
    return min_trip

#Função para retornar a média entre os valores de uma lista
def get_mean(data_list):
    mean_trip = 0.
    sum_trip = 0
    
    for i in data_list:
        sum_trip += int(i)
    
    mean_trip = sum_trip / len(data_list)
    
    return int(mean_trip)

#Função para retornar a mediana entre os valores de uma lista
def get_median(data_list):
    median_trip = 0.
    center = 0
    
    #Verificando se a lista é par
    if len(data_list) % 2 == 0:
        
        #variavel para a localização de um dos termos próximos à posição central da lista par
        c1 = len(data_list) // 2
        #Variável para a localização do outro termo próximo à posição central
        c2 = c1 + 1
        
        #Achando o termo central, sendo a média entre os dois termos próximos a ele
        center = (c1 + c2) / 2
        
        median_trip = int(data_list[center])
    
    #Caso a lista seja ímpar
    else:
        #Variável criada para pegar o termo central da lista ímpar, sendo único
        center = int((len(data_list) + 1) / 2)
        median_trip = int(data_list[center])
    
    return median_trip

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0
max_trip = 0
mean_trip = 0
median_trip = 0

min_trip = get_min(trip_duration_list)
max_trip = get_max(trip_duration_list)
mean_trip = get_mean(trip_duration_list)
median_trip = get_median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set()

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------