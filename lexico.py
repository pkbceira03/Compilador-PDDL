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
    "action", "parameters", "precondition", "effect", 
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
    '(',')'
]

#espaco
espaco = [" ","\n","\t","\r"]

#tokens
#feitos
DELEMITADOR = [] #delimiter
COMENTARIO = [] #comment
IDENTIFICADOR = [] #identifier
VARIAVEL = [] #varialvel ? + identificador
PALAVRAS_RESERVADAS = [] #heyword
OPERADORES_LOGICO = [] #logical operator
OPERADORES_QUANTIFICADORES = [] #quantifier operator
OPERADORES_CONDICIONAIS = [] #conditional operator
OPERADORES_DE_MODIFICACAO = [] #modifier operator
OPERADORES_TEMPORAIS = [] #temporal operador 
OPERADORES_DE_OTIMIZACAO = [] #optimization operator
NUMERO = [] #number
OPERADORES_ARITMETICO = [] #arithmetic logical 
NAO_RECONHECE = [] #unknow


#armazena todos os tokens
token = []

#função principal
def lexico(codigo):
    posicao = 0

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

        #encontra comentarios
        if proximo(posicao) == ';':
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
            token.append(f"COMENTARIO = {comentario}")
            posicao = posicao_aux
        elif proximo(posicao) == ':':
            DELEMITADOR.append(proximo(posicao))
            token.append(f"DELIMITATOR = {proximo(posicao)}")
            posicao += 1
            while proximo(posicao) is not None and proximo(posicao) not in espaco and (proximo(posicao) in letra_digitos or proximo(posicao) == '-'):
                palavra += proximo(posicao)
                posicao += 1
            PALAVRAS_RESERVADAS.append(palavra)
            token.append(f"PALAVRA_RESERVADA = {palavra}")
            palavra =''
            
        elif proximo(posicao) in delimitador:
            #encontra os delimitadores
            DELEMITADOR.append(proximo(posicao))
            token.append(f"DELIMITATOR = {proximo(posicao)}")
            #print(proximo(posicao))
            posicao += 1
        #encontra as variaveis
        elif proximo(posicao) == '?':
            aux_variavel = ''
            aux_variavel += proximo(posicao)
            posicao += 1
            if proximo(posicao) in digitos:
                palavra += proximo(posicao-1)
                while proximo(posicao) not in espaco:
                    palavra += proximo(posicao)
                    aux_variavel += proximo(posicao)
                    posicao += 1
                NAO_RECONHECE.append(palavra)
                token.append(f"NAO_RECONHECE = {palavra}")
                posicao += 1
                palavra = ''
            else:
                while proximo(posicao) not in espaco and proximo(posicao) in letra_digitos:
                    palavra += proximo(posicao)
                    aux_variavel += proximo(posicao)
                    posicao += 1

                IDENTIFICADOR.append(palavra)
                VARIAVEL.append(aux_variavel)
                token.append(f"IDENTIFICADOR = {palavra}")
                token.append(f"VARIAVEL = {aux_variavel}")
                palavra = ''
                aux_variavel = ''
                posicao += 1
            
        elif proximo(posicao) in letra:
            palavra += proximo(posicao)
            posicao+=1
            while proximo(posicao) is not None and proximo(posicao) not in espaco and (proximo(posicao) in letra_digitos or proximo(posicao) == '-'):
                palavra += proximo(posicao)
                posicao += 1
            
            if palavra in palavras_reservadas:
                PALAVRAS_RESERVADAS.append(palavra)
                token.append(f"PALAVRA_RESERVADA = {palavra}")
            elif palavra in logicos:
                OPERADORES_LOGICO.append(palavra)
                token.append(f"OPERADOR_LOGICO = {palavra}")
            elif palavra in quantificador:
                OPERADORES_QUANTIFICADORES.append(palavra)
                token.append(f"OPERADOR QUATIFICADOR = {palavra}")
            elif palavra in condicional:
                OPERADORES_CONDICIONAIS.append(palavra)
                token.append(f"OPERADOR CONDICIONAL = {palavra}")
            elif palavra in temporal:
                OPERADORES_TEMPORAIS.append(palavra)
                token.append(f"OPERADOR TEMPORAL = {palavra}")
            elif palavra in otimizacao:
                OPERADORES_DE_OTIMIZACAO.append(palavra)
                token.append(f"OPERADOR DE OTIMIZACAO = {palavra}")
            elif palavra in modificador:
                OPERADORES_DE_MODIFICACAO.append(palavra)
                token.append(f"OPERADOR DE MODIFICACAO = {palavra}")
            else:
                IDENTIFICADOR.append(palavra)
                token.append(f"IDENTIFICADOR = {palavra}")
            
            palavra=''
        elif proximo(posicao) in aritmeticas:
            OPERADORES_ARITMETICO.append(proximo(posicao))
            token.append(f"OPERADOR ARITMETICO = {proximo(posicao)}")
            posicao +=1
        #pega os numeros
        elif proximo(posicao) in digitos:
            palavra += proximo(posicao)
            posicao += 1
            while proximo(posicao) not in espaco:
                conta=0
                palavra += proximo(posicao)
                if proximo(posicao) in letra:
                    conta +=1
            if conta > 0:
                NAO_RECONHECE.append(palavra)
                token.append(f"NAO_RECONHECE = {palavra}")
                
            else:
                NUMERO.append(palavra)
                token.append(f"NUMERO = {palavra}")
            palavra = ''
            

        else:
            #print('pula')
            #print(proximo(posicao))
            if proximo(posicao):
                NAO_RECONHECE.append(proximo(posicao))
                token.append(f"NAO_RECONHECE = {proximo(posicao)}")
            posicao+=1
                
import sys
import os

if len(sys.argv) < 3:
    sys.exit(1)

arq1 = sys.argv[1]
arq2 = sys.argv[2]

with open(arq1, mode='r', encoding='utf-8') as file:
    codigo1 = file.read()

with open(arq2, mode='r', encoding='utf-8') as file:
    codigo2 = file.read()    

lexico(codigo1)
lexico(codigo2)

###como rodar 
##============================================================##
##python3 lexico.py exemplomojproblem.pddl exemplomojdomain.pddl

print('KEYWORD: ',len(PALAVRAS_RESERVADAS))
# print(PALAVRAS_RESERVADAS)
print('IDENTIFIER: ',len(IDENTIFICADOR))
#print(IDENTIFICADOR)
print('VARIABLES: ',len(VARIAVEL))
#print(VARIAVEL)
print('NUMBER: ',len(NUMERO))
#print(NUMERO)
print('ARITHMETIC_OPERATOR: ', len(OPERADORES_ARITMETICO))
# print(OPERADORES_ARITMETICO)
print('LOGICAL_OPERATOR: ',len(OPERADORES_LOGICO))
#print(OPERADORES_LOGICO)
print('QUANTIFIER_OPERATOR: ',len(OPERADORES_QUANTIFICADORES))
#print(OPERADORES_QUANTIFICADORES)
print('CONDITIONAL_OPERATOR: ',len(OPERADORES_CONDICIONAIS))
#print(OPERADORES_CONDICIONAIS)
print('MODIFIER_OPERATOR: ',len(OPERADORES_DE_MODIFICACAO))
#print(OPERADORES_DE_MODIFICACAO)
print('TEMPORAL_OPERATOR: ',len(OPERADORES_TEMPORAIS))
#print(OPERADORES_TEMPORAIS)
print('OPTIMIZATION_OPERATOR: ',len(OPERADORES_DE_OTIMIZACAO))
#print(OPERADORES_DE_OTIMIZACAO)
print('DELIMITER: ',len(DELEMITADOR))
# print(DELEMITADOR)
print('COMMENTS: ',len(COMENTARIO))
#print(COMENTARIO)
print('UNKNOWN: ',len(NAO_RECONHECE))
#print(NAO_RECONHECE)

# print('token')
# print(token)

