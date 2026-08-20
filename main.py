class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __repr__(self):
        return f"Prioridad: {self.priority}, Valor: {self.value}"

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, value):
        nuevo = Node(priority, value)
        self.queue.append(nuevo)
        self.queue.sort(key=lambda nodo: nodo.priority)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def mostrar(self):
        for nodo in self.queue:
            print(nodo)

def main():
    cola = PriorityQueue()

    cola.enqueue(2, "B")
    cola.enqueue(5, "D")
    cola.enqueue(1, "A")
    cola.enqueue(10, "E")
    cola.enqueue(3, "C")

    print("Cola:")
    cola.mostrar()

    print("\nElemento con mayor prioridad:")
    print(cola.peek())

    print("\nSacando elementos:")

    while len(cola.queue) > 0:
        print(cola.dequeue())

main()