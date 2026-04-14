from singly_linked_list import SinglyLinkedList
from singly_linked_list import Node

#Class name: SplitEvensOdds
#Class purpose: To split a singly linked list into two separate lists, one containing the even values and the other containing the odd values.

class SplitEvensOdds(SinglyLinkedList):

    #Method name: split_even_odd
    #Purpose: To split the original list into two separate lists, one containing the even values and the other containing the odd values. The original list will be cleared after the split.
    #Parameters: None
    #Returns: A tuple containing the even list and the odd list as SinglyLinkedList objects.
    #Preconditions: The original list must not be empty. If the list is empty, an exception will be raised.
    #Postconditions: The original list will be cleared, and two new lists will be created containing the even and odd values, respectively.

    def split_even_odd(self):
        #Raise exception if list is empty
        if self._SinglyLinkedList__head is None:
            raise SinglyLinkedList.EmptyListException()

        #Create even_list and odd_list as SinglyLinkedList objects
        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        #Assign current cursor to list.head
        current = self._SinglyLinkedList__head

        #Clear original list
        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0

        #while (more nodes)
        while current:
            next_node = current.next
            current.next = None #(disconnect node from original list)

            #if current.data is even
            if current.data % 2 == 0:
                #if even_list.tail is None
                if even_list._SinglyLinkedList__tail is None:
                    even_list._SinglyLinkedList__head = current
                    even_list._SinglyLinkedList__tail = current
                
                else:
                    even_list._SinglyLinkedList__tail.next = current
                    even_list._SinglyLinkedList__tail = current

                even_list._SinglyLinkedList__count += 1

            else:
                #Node value is odd
                if odd_list._SinglyLinkedList__tail is None:
                    odd_list._SinglyLinkedList__head = current
                    odd_list._SinglyLinkedList__tail = current
                else:
                    odd_list._SinglyLinkedList__tail.next = current
                    odd_list._SinglyLinkedList__tail = current
                odd_list._SinglyLinkedList__count += 1

            current = next_node

        return even_list, odd_list
