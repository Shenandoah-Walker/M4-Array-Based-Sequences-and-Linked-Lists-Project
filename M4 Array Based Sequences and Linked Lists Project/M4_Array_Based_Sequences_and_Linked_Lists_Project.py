#Singly Linked List Test Program

from singly_linked_list import SinglyLinkedList

#Forward list
print("---- Build a forward list ----")
my_list = SinglyLinkedList()
my_list.build_forward_list([10, 20, 30, 40, 50])
print("Head ->", " -> ".join(str(x) for x in my_list), "-> None")

#Delete the first node
my_list.remove(10)
print("Delete the first node: Head ->", " -> ".join(str(x) for x in my_list), "-> None")

#Delete the last node
my_list.remove(50)
print("Delete the last node: Head ->", " -> ".join(str(x) for x in my_list), "-> None")

#Delete the interior node
my_list.remove(30)
print("Delete the interior node: Head ->", " -> ".join(str(x) for x in my_list), "-> None")

#Backward list
print()
print("---- Build a backward list ----")
my_list2 = SinglyLinkedList()
my_list2.build_backward_list([10, 20, 30, 40, 50])
print("Head ->", " -> ".join(str(x) for x in my_list2), "-> None")

#Delete the first node
my_list2.remove(50)
print("Delete the first node: Head ->", " -> ".join(str(x) for x in my_list2), "-> None")

#Delete the last node
my_list2.remove(10)
print("Delete the last node: Head ->", " -> ".join(str(x) for x in my_list2), "-> None")

#Delete the interior node
my_list2.remove(30)
print("Delete the interior node: Head ->", " -> ".join(str(x) for x in my_list2), "-> None")

#Remove all test
print()
print("---- Remove all test ----")
my_list3 = SinglyLinkedList()
my_list3.build_forward_list([1, 2, 4, 6, 1, 3, 6])
print("Head ->", " -> ".join(str(x) for x in my_list3), "-> None")

#Remove all the occurrences of 1 in the list. (There should be 2)
my_list3.remove_all(1)
print("Removing 1 and all duplicates: Head ->", " -> ".join(str(x) for x in my_list3), "-> None")

#Remove all the occurrences of 6 in the list. (There should be 2)
my_list3.remove_all(6)
print("Removing 6 and all duplicates: Head ->", " -> ".join(str(x) for x in my_list3), "-> None")

#Non-recursive reverse display test
print()
print("---- Non-recursive reverse display test ----")

my_list4 = SinglyLinkedList()
my_list4.build_forward_list([10, 20, 30, 40, 50])

#Insertion order
print("Insertion order: Head ->", " -> ".join(str(x) for x in my_list4), "-> None")

#Reverse order (recursive)
print("Reverse order (recursive): None <-", end= ' ')
my_list4.display_reverse()
print(" <- Head")

#Reverse order (non-recursive)
my_list4.display_reverse_nr()
