class elementosPlaca:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.next = None
    
class inicioLista:
    def __init__(self):
        self.head = None
    
    def insSiglaEstado (self, sigla, nomeEstado):
        newNode = elementosPlaca(sigla, nomeEstado)
        newNode.next = self.head
        self.head = newNode
        
    def listaEstado(self):
        tmp = self.head
        while (tmp):
            print(tmp.sigla, end=" ")
            tmp = tmp.next
        print ()
        
def funcaoHash(sigla):
    if sigla == "DF":
        return 7
    else:
        return (ord(sigla[0]) + ord(sigla[1])) % 10
    
tabelaHash = [inicioLista() for _ in range(10)]
estadosUF = [("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"), 
          ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"), 
          ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"), 
          ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"), 
          ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"), 
          ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"), 
          ("SE", "Sergipe"), ("TO", "Tocantins")]

for i in range(10):
    print(f"Posição {i}: ", end="")
    tabelaHash[i].listaEstado() 
print ()

for estadosUFs in estadosUF:
    index = funcaoHash(estadosUFs[0])
    tabelaHash[index].insSiglaEstado(estadosUFs[0], estadosUFs[1])
for i in range(10):
    print(f"Posição {i}: ", end="")
    tabelaHash[i].listaEstado() 
print ()

estadoFicticio = ("MO", "Marcelo Oliveira")
index = funcaoHash(estadoFicticio[0])
tabelaHash[index].insSiglaEstado(estadoFicticio[0], estadoFicticio[1])
for i in range(10):
    print(f"Posição {i}: ", end="")
    tabelaHash[i].listaEstado() 
print ()
