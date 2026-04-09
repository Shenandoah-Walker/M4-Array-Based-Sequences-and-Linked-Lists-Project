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