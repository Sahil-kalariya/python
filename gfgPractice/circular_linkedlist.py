class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def add(head ,tail,data):
        node = Node(data)
        if(head == None):
            head = node
            tail = node
        else:
            head.next = node
            head = node
            head.next = tail
        return [head , tail]    

    def display(head):
        ptr = head
        while ptr:
            print(ptr.data , end=" ")
            ptr = ptr.next
            if(ptr.next == head):
                break

    def search(tail , data):
        head = tail
        while head:
            if(tail.data == data):
                return "data found"
            if(head == tail.next):
                return "not found"
            tail = tail.next

if __name__ == "__main__":
    head = None
    tail = None
    head , tail = Node.add(head,tail,1)
    head , tail = Node.add(head,tail,3)
    head , tail = Node.add(head,tail,4)
    head , tail = Node.add(head,tail,4)
    head , tail = Node.add(head,tail,3)
    head , tail = Node.add(head,tail,56)
    head , tail = Node.add(head,tail,1)
    Node.display(tail)
    print("\n" + Node.search(tail , 56))
    print(Node.search(tail , 45))

