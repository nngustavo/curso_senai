import queue 

#Criar fila vazia
fila = queue.Queue()

fila.put("A")
fila.put("B")
fila.put("C")

#tamanho

tamanho = fila.qsize()
print("Tamanho da fila: ", tamanho)

#remover 

item = fila.get()
print("Elemento removido: ", item)

#sera que removeu

tamanho = fila.qsize()
print("Tamanho da fila: ", tamanho)


#verificar se a fila está vazia

vazia = fila.empty()
print("A fila está vazia?", vazia)