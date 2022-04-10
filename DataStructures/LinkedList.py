class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + " => "
            itr = itr.next

        print(llstr);

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next

        return length

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid index")
            return
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            print("Invalid index")
            return

        if index == 0:
            self.insert_at_beginning(value);
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = Node(value, itr.next)
                break

            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            self.head = Node(data_to_insert, None)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return

            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return

            itr = itr.next

if __name__ == "__main__":
    ll = LinkedList();
    # ll.insert_at_beginning(5);
    # ll.insert_at_beginning(89);
    # ll.insert_at_end(50);
    ll.insert_values([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll.print()
    ll.remove_by_value(4)
    # print("Length of linked list : ", ll.get_length())
    ll.print()
