#Cria cada elemento da lista
class ElementoDaListaSimples:
# construtor de inicialização da classe
    def __init__(self, nodos=None):    
        self.head = None
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo
#__repr__ é um método especial do Python
#use-o para criar a maneira como o objeto
#é mosrtadofora da função print
    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(nodo.dado)
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)
    