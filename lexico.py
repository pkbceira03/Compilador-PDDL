#variaveis
variaveis = r"\?[a-zA-Z][a-zA-Z0-9]*"

#constantes
constantes = r"\[a-zA-Z0-9]*"

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

#simbolos que são usados
simbolos = [
    '(',')','-'
]
