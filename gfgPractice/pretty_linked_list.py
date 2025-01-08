class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(val , head):
        node = Node(val)
        if(head == None):
            return node
       
        trav = head
        while(trav.next):
            trav = trav.next
        trav.next = node

    def display(head):
        print("[" , end = "")
        while head:
            if(head.next == None):
                print(f"{head.val}" ,end = "")
            else:    
                print(f"{head.val} ,",end = " ")
            head = head.next    
        print("]")


if __name__  == "__main__":
    head = None
    head = Node.add(1 , head )
    Node.add(2 ,head )
    Node.add(3 , head )
    Node.add(4 , head )
    Node.display(head)

