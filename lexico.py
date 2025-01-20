import os

letra = r"\?[a-zA-Z]"

digitos = r"\[0-9]*"

letras_digitos = letra + digitos

#lista de palavras reservadas
#acho que o problem entra em outra categario pois não começa com o:
#no arquivo de Domain (onde colocamos as ações) a palavra domain não começa com o : mas no outro arquivo começa com :
palavras_reservadas = [
    'domain', 'requirements', 'types','predicates',
    'action', 'parameters','precondition', 'effect', 
    'init', 'functions','problem', 'objects', 
    'define', 'goal','derived', 'extends', 'constants',
    'timeless', 'axiom', 'context', 'implies'
]

#operadores
operadores = [
    'and', 'forAll', 'when', 'not', 'or',
    'increse','imply'
]

#delimitador
delimitador = [
    '(',')'
]

#simbolos
simbolos = [
    '-', ':',';'
]

#tokens
DELEMITADOR = []
SIMBOLO =[]
OPRADORES = []
PALAVRAS_RESERVADAS = []
COMENTARIO = []
VARIAVEL = []
CONSTANTE = []
FUNCAO = []

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

        print(f"Conteudo do comentario -> {comentario}")
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
        if proximo(posicao) == ';':
            posicao = tira_comentario(posicao)
            continue
        posicao += 1

caminho = os.path.abspath("problem.pddl")
print (caminho)

with open('/home/pedro/unb/Compiladores/Trabalho/Compilador-PDDL/problem.pddl', mode='r', encoding='utf-8')as file:
    codigo = file.read()    

lexico(codigo)

