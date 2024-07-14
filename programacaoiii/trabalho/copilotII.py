class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, sigla, nomeEstado):
        newNode = Node(sigla, nomeEstado)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.sigla, end=" ")
            temp = temp.next
        print()

def hashFunction(sigla):
    if sigla == "DF":
        return 7
    else:
        return (ord(sigla[0]) + ord(sigla[1])) % 10

hashTable = [LinkedList() for _ in range(10)]
states = [("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"), 
          ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"), 
          ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"), 
          ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"), 
          ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"), 
          ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"), 
          ("SE", "Sergipe"), ("TO", "Tocantins"), ("BK", "Bruno Kostiuk")]

for state in states:
    index = hashFunction(state[0])
    hashTable[index].insert(state[0], state[1])

for i in range(10):
    print(f"Posição {i}: ", end="")
    hashTable[i].printList()
