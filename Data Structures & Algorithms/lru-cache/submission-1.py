class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.latest = Node()
        self.data = {}
        self.volumn = 0
        self.latest.prev = self.dummy
        self.dummy.next = self.latest

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            # connect prev and next
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            # put the node right
            node.prev = self.latest.prev
            node.next = self.latest
            self.latest.prev.next = node
            self.latest.prev = node
            
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            # change value
            node.value = value
            # connect prev and next
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            # put the node right
            node.prev = self.latest.prev
            node.next = self.latest
            self.latest.prev.next = node
            self.latest.prev = node
            # print(self.data)
        else:
            self.data[key] = Node(value, prevNode=self.latest.prev, nextNode=self.latest, key=key)
            self.latest.prev.next = self.data[key]
            self.latest.prev = self.data[key]
            if self.volumn < self.capacity:
                self.volumn += 1
                # print(self.data)
            else:
                delete = self.dummy.next
                start = delete.next
                # print(self.dummy.key)
                del self.data[delete.key]
                self.dummy.next = start
                start.prev = self.dummy
                # print(self.data)




class Node:
    def __init__(self, value=0, prevNode=None, nextNode=None, key=-1):
        self.value = value
        self.prev = prevNode
        self.next = nextNode
        self.key = key 
