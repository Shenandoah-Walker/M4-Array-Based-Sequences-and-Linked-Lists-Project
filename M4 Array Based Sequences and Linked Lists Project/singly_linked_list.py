class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    class EmptyListException(Exception):
        pass

    class NodeNotFoundException(Exception):
        pass

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def build_forward_list(self, iterable):
        for item in iterable:
            self.__append(item)

    def build_backward_list(self, iterable):
        for item in iterable:
            self.__prepend(item)

    def __append(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    def __prepend(self, value):
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
        self.__count += 1

    def insert_after(self, after_value, new_value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        current = self.__head
        while current and current.data != after_value:
            current = current.next
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        if current == self.__tail:  # if inserted at end of list
            self.__tail = new_node   # re-route the tail pointer
        self.__count += 1

    def remove(self, value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        current = self.__head
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        if previous is None:
            self.__head = current.next  # remove first node
        else:
            previous.next = current.next  # remove an interior node
        if current == self.__tail:
            self.__tail = previous  # remove the last node
        self.__count -= 1

    def display(self):
        current = self.__head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def display_reverse(self):
        def _reverse_recursive(node):
            return _reverse_recursive(node.next) + [node.data] if node else []
        print(" <- ".join(map(str, _reverse_recursive(self.__head))))

    def __iter__(self):
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.__count


    #remove_all function created by me:
    def remove_all(self, value):
        #If the list is empty, raise an exception
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        #Set current and previous pointers to traverse the list. The current pointer starts at the head of the list, and the previous pointer starts as None (because there is no previous node at the beginning of a list)
        current = self.__head
        previous = None
        #Loop through the list. If the current node's data matches the value to be removed, remove the node. 
        #If the current node is the head, update the head pointer. If the current node is the tail, update the tail pointer. 
        #If the current node is an interior node, update the previous node's next pointer to skip the current node. 
        #After removing a node, update the current pointer to continue checking for more occurrences of the value.
        while current:
            if current.data == value:
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next
                if current == self.__tail:
                    self.__tail = previous
                self.__count -= 1
                current = current.next if previous is None else previous.next
            else:
                previous = current
                current = current.next


    #display_reverse_nr function created by me:
    def display_reverse_nr(self):
        #If the list is empty, raise an exception
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        #Create an empty stack that will hold the elements of the list
        stack = []
        #Set current to the head of the list. previous is not needed for this function because the previous node is not required to display the list in reverse order.
        current = self.__head

        #Loop through the list and push each node's data onto the stack. After the loop, the stack will contain all the elements of the list in reverse order (because a stack has LIFO behavior).
        while current:
            stack.append(str(current.data))
            current = current.next

        #Join the elements in the stack into a string with " -> " as a separator and reverse the stack.
        number_part_of_output  = " -> ".join(stack[::-1])

        #Outer part of output to match sample output in Canvas
        print(f"Reverse order (non-recursive): None <- {number_part_of_output} <- Head")
        
