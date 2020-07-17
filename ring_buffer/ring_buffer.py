from singly_linked_list import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.storage = [None] * capacity
        

    def append(self, item):
        # entering item into the list at the index that self.size resolves to
        self.storage[self.size] = item
        # Incrementing size so that the size will point to a new index
        self.size += 1
        # check if buffer is full
        if self.size == self.capacity:
        # reset size to 0 (even though it's not) so that the incoming item replaces the oldest item in the buffer
            self.size = 0
            # self.storage[self.size] = item




    def get(self):
        a = [i for i in self.storage if i is not None]
         
        return a

# test = RingBuffer(4)
# print(test.storage)
# test.append('1')
# test.append('2')
# test.append('3')
# test.append('5')
# print(test.storage)
# test.append('6')
# print(test.storage)
# test.append('7')
# print(test.storage)