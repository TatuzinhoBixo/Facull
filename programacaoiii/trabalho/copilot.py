class Node:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def inserirComPrioridade(self, node):
        if not self.head or self.head.color == 'V':
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next and current.next.color == 'A':
                current = current.next
            node.next = current.next
            current.next = node

    def inserir(self):
        color = input("Digite a cor (A ou V): ")
        number = int(input("Digite o número: "))
        node = Node(number, color)
        if not self.head:
            self.head = node
        elif color == 'V':
            self.inserirSemPrioridade(node)
        elif color == 'A':
            self.inserirComPrioridade(node)

    def imprimirListaEspera(self):
        current = self.head
        while current:
            print(f"Cartão: {current.color}, Número: {current.number}")
            current = current.next

    def atenderPaciente(self):
        if self.head:
            print(f"Atendendo paciente com cartão {self.head.color} número {self.head.number}")
            self.head = self.head.next

def menu():
    lista = LinkedList()
    while True:
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            lista.inserir()
        elif opcao == 2:
            lista.imprimirListaEspera()
        elif opcao == 3:
            lista.atenderPaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

#######################################                                                                                                                          


class Node:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def printList(self):
        current = self.head
        while current:
            print(f"Card Number: {current.number}, Color: {current.color}")
            current = current.next

    def attendPatient(self):
        if self.head:
            print(f"Calling patient with card number {self.head.number} for attendance")
            self.head = self.head.next

def menu():
    yellow_list = LinkedList()
    green_list = LinkedList()
    while True:
        print("1 - Add patient to queue, 2 - Show patients in queue, 3 - Call patient, 4 - Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            color = input("Enter color (A or V): ")
            number = int(input("Enter number: "))
            node = Node(number, color)
            if color == 'A':
                yellow_list.insert(node)
            else:
                green_list.insert(node)
        elif option == 2:
            yellow_list.printList()
            green_list.printList()
        elif option == 3:
            if yellow_list.head:
                yellow_list.attendPatient()
            else:
                green_list.attendPatient()
        elif option == 4:
            break
        else:
            print("Invalid option. Please choose again.")

menu()



def menu():
    lista = LinkedList()
    while True:
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            lista.inserir()
        elif opcao == 2:
            lista.imprimirListaEspera()
        elif opcao == 3:
            lista.atenderPaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

