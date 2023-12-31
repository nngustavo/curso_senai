class Fila:
    #definição de um fila sem tamanho e sem elementos
    def __init__(self):
        self.itens = []

    #tamando da fila
    def tamanho(self):
        return len(self.itens)

    #definindo função enfileirar
    def enfileirar(self, elemento):
        self.itens.append(elemento)
    
    #valida vazia
    def esta_vazia(self):
        return len(self.itens) == 0

    #funcao desenfileirar
    def desenfileirar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0) #remoção da fila

#como se fosse ponteiro
fila = Fila()

fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")
fila.enfileirar("D")

tamanho = fila.tamanho()
print("Tamanho da fila: ", tamanho)

valor = fila.desenfileirar()
print("item removido: ", valor)

tamanho = fila.tamanho()
print("Tamanho da Fila: ", tamanho)

valor = fila.desenfileirar()
print("item removido: ", valor)

fila_vazia = fila.esta_vazia()
print("A fila está vazia? ", fila_vazia)