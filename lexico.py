import os

letra = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Lista de dígitos
digitos = ['0','1','2','3','4','5','6','7','8','9']

# Combinação de letras e dígitos
letra_digitos = letra + digitos

#lista de palavras reservadas
palavras_reservadas = [
    "define", "domain", "requirements", "types", 
    "constants", "predicates", "functions", "constraints", 
    "action" "parameters", "precondition", "effect", 
    "durative-action", "duration", "condition", "derived", 
    "problem", "objects", "init", "goal", "metric", 
    "total-time", "lenght", "serial", "parallel"
]

#operadores
#logicos
logicos = [
    'and', 'or', 'not', 'imply'
]
#aritmeticas
aritmeticas = [
    '+', '-', '*', '/', '<', '>', '=', '<=', '>='
]

#qualificador
quantificador = [
    'forall', 'exists'
]

#condicional
condicional = [
    'when'
]

#modificador
modificador = [
    'assign', 'scale-up', 'scale-down', 'increase', 'decrease'
]

#temporal
temporal = [
    'at', 'over', 'start', 'end'
]

#otimizacao
otimizacao = [
    'minimize', 'maximize'
]

#delimitador
delimitador = [
    '(',')', ':'
]

#simbolos
simbolos = [
    '-',';','?'
]

#Caracteres aceitos
caracter = digitos + delimitador + simbolos

#espaco
espaco = [" ","\n","\t","\r"]
#tokens
DELEMITADOR = [] #delimiter
PALAVRAS_RESERVADAS = [] #heyword
COMENTARIO = [] #comment
NUMERO = [] #number
IDENTIFICADOR = [] #identifier
VARIAVEL = [] #varialvel ? + identificador
OPERADORES_LOGICO = [] #logical operator
OPERADORES_ARITMETICO = [] #arithmetic logical 
OPERADORES_QUANTIFICADORES = [] #quantifier operator
OPERADORES_CONDICIONAIS = [] #conditional operator
OPERADORES_DE_MODIFICACAO = [] #modifier operator
OPERADORES_TEMPORAIS = [] #temporal operador 
OPERADORES_DE_OTIMIZACAO = [] #optimization operator


#armazena todos os tokens
token = []

#função principal
def lexico(codigo):
    posicao = 0
    
    #remove os comentarios
    def tira_comentario(posicao):
        posicao_aux = posicao
        comentario = []
        #ir ate o fim da linha que é o \n
        #adicionar no token 
        #continuar o while passado na proxima linha 
        comentario.append(codigo[posicao_aux])
        posicao_aux += 1
        while posicao_aux<len(codigo):
            caracter = codigo[posicao_aux]
            if caracter == '\n':
                posicao_aux +=1
                break
            comentario.append(codigo[posicao_aux])
            posicao_aux += 1

        #print(f"Conteudo do comentario -> {comentario}")
        COMENTARIO.append(codigo[posicao:posicao_aux])
        token.append(f"COMENTARIO = {COMENTARIO}")
        posicao = posicao_aux

        return posicao

    #função para ver o proximo caracter
    def proximo(posicao):
        if posicao < len(codigo):
            return codigo[posicao]
        else:
            return None

    #percorre o arquivo inteiro  
    while posicao < len(codigo):
        palavra = ""
        linha = 0
        #print(proximo(posicao))
        #ignora os espaço em brando
        while proximo(posicao) in espaco:
            if proximo(posicao) == '\n':
                linha += 1
            posicao += 1

        #tira comentarios
        if proximo(posicao) == ';':
            posicao = tira_comentario(posicao)
            posicao += 1
            continue
        elif proximo(posicao) in delimitador:
            #encontra os delimitadores
            DELEMITADOR.append(proximo(posicao))
            token.append(f"DELIMITATOR = {proximo(posicao)}")
            #print(proximo(posicao))
            posicao += 1
        else:
            # print('pula')
            # print(proximo(posicao))
            posicao+=1
                
        

caminho = os.path.abspath("problem.pddl")
print (caminho)

with open('/home/pedro/unb/Compiladores/Trabalho/Compilador-PDDL/domain.pddl', mode='r', encoding='utf-8')as file:
    codigo = file.read()    

lexico(codigo)

print('comentario')
print(len(COMENTARIO))
print(COMENTARIO)
print('delimitador')
print(len(DELEMITADOR))



# print('token')
# print(token)

