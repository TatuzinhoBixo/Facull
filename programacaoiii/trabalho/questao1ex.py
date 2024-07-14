#ExercícioUninter
#Criar os elementos da lista
class ElementoDaListaSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

#__repr__ é um método especial do Python
    def __repr__(self):
        return self.dado
    
#Criar uma lista encadeada simples
class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            nodo = ElementoDaListaSimples (dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples (dado=elem)
                nodo = nodo.proximo
        
    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos = self.head
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)
        