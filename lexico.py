import os

letra = r"\?[a-zA-Z]"

digitos = r"\[0-9]*"

letras_digitos = letra + digitos

#lista de palavras reservadas
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

#espaco
espaco = [" ","\n","\t","\r"]

#tokens
DELEMITADOR = []
SIMBOLO =[]
OPRADORES = []
PALAVRAS_RESERVADAS = []
COMENTARIO = []
VARIAVEL = []
CONSTANTE = []
FUNCAO = []
TIPO = []

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
        #print(proximo(posicao))
        #ignora os espaço em brando
        while proximo(posicao) in espaco:
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
        elif proximo(posicao) in simbolos:
            simbolo_aux = proximo(posicao)
            #print(simbolo_aux)
            if simbolo_aux == ':':
                #token do simbolo
                SIMBOLO.append(proximo(posicao))
                token.append(f"SIMBOLO = {proximo(posicao)}")

                # os proximos caracteres são uma palavra chave
                posicao += 1
                while proximo(posicao) not in espaco:
                    palavra += proximo(posicao)
                    posicao += 1
                #print(palavra)
                #coloca palavra no token e zera a variável
                PALAVRAS_RESERVADAS.append(palavra)
                token.append(f"PALAVRA_RESERVADA = {palavra}")
                #print(proximo(posicao))
                posicao += 1
                palavra=""
                
            elif simbolo_aux == '-':
                # é uma atribuição de variavel
                if proximo(posicao+1) == ' ':
                    posicao += 2
                    while proximo(posicao) not in espaco and proximo(posicao) not in delimitador:
                        palavra += proximo(posicao)
                        posicao +=1

                    print(palavra)
                    TIPO.append(palavra)
                    token.append(f"TIPO_VARIAVEL = {palavra}")
                    palavra = ""
                    posicao += 1
                else:
                    posicao += 1

        elif proximo(posicao) in letra:
            #print('letra')
            posicao += 1
        else:
            posicao+=1
                
        

caminho = os.path.abspath("problem.pddl")
print (caminho)

with open('/home/pedro/unb/Compiladores/Trabalho/Compilador-PDDL/problem.pddl', mode='r', encoding='utf-8')as file:
    codigo = file.read()    

lexico(codigo)
# print('comentario')
# print(COMENTARIO)
# print('delimitador')
# print(DELEMITADOR)
# print('palavras reservadas')
# print(PALAVRAS_RESERVADAS)
print('tipo')
print(TIPO)
# print('token')
# print(token)

