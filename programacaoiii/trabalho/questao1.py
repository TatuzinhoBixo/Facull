#ExercícioUninter-List encadeada
class ElementosDaListaSimples:
    def __init__(self, numero=None, cor=None):
        self.numero = numero
        self.cor = cor
        self.proximo = None
        
class InicioLista:
    def __init__(self):
       self.head = None

    def insSemPrioridade(self, node):
        if not self.head:
            self.head = node
        else:
            paciente = self.head
            while paciente.proximo:
                paciente = paciente.proximo
            paciente.proximo = node
        
    def insPrioridade(self, node):
        if not self.head or self.head.cor == 'V':
            node.proximo = self.head
            self.head = node
        else:
            paciente = self.head
            while paciente.proximo and paciente.proximo.cor == 'A':
                paciente = paciente.proximo
            node.proximo = paciente.proximo
            paciente.proximo = node
    
    def inserir(self):
        while True:
            cor = input("Digite a cor do cartão, V para verde ou A para amarelo: ")
            if cor in ['V', 'A']:
                break
            else:
                print("Resposta inválida, favor inserir a cor do cartão corretamete, V para verde ou A para amarelo.")
        numero = int(input("Digite o número do cartão: "))
        node = ElementosDaListaSimples(numero, cor)
        if not self.head:
            self.head = node
        elif cor == 'V':
            self.insSemPrioridade(node)
        elif cor == 'A':
            self.insPrioridade(node)
    
    def listaDeEspera(self):
        paciente = self.head
        while paciente:
            print (f"Cartão: {paciente.cor}, {paciente.numero}")
            paciente = paciente.proximo
        
    def atendePaciente(self):
        if self.head:
            print (f"Atenddimento ao paciente com o cartão {self.head.cor}, número {self.head.numero}")
            self.head = self.head.proximo
            
def menu():
    lista = InicioLista()
    while True:
        print("1 - Adicionar o paciente a fila")
        print("2 - Mostrar os pacientes que estão na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            lista.inserir()
        elif opcao == 2:
            lista.listaDeEspera()
        elif opcao == 3:
            lista.atendePaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida, favor inserir uma opção válida.")
            
menu ()
            