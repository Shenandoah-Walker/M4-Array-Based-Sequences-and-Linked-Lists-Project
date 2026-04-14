from singly_linked_list import SinglyLinkedList
from singly_linked_list import Node

class SplitEvensOdds(SinglyLinkedList):
    def split_even_odd(self)):
        #Raise exception if list is empty
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()

        #Create even_list and odd_list as SinglyLinkedList objects