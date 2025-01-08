class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def add(head , data):
        node = Node(data)
        if head == None:
            return node
        trav = head
        while trav.next:
            trav = trav.next   
        trav.next = node

    def display(head):
        trav = head
        while trav:
            print(trav.data , end = " ")
            trav = trav.next
        print()
    def findMid(head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)    

if __name__ == "__main__":
    head = None 
    head = Node.add(head , 1)
    Node.add(head , 2)
    Node.add(head , 3)
    Node.add(head , 4)
    # Node.add(head , 5)
    Node.display(head)
    Node.findMid(head)