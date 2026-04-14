#Split Evens-Odds Test Program

from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

print("---- Split Evens and Odds Test ----")

#Build the original list
my_list = SplitEvensOdds()
my_list.build_forward_list([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

#Display original list
print("Head ->", " -> ".join(str(x) for x in my_list), "-> None")

#Split the list
evens, odds = my_list.split_even_odd()

#Display evens list
print("Head ->", " -> ".join(str(x) for x in evens), "-> None")

#Display odds list
print("Head ->", " -> ".join(str(x) for x in odds), "-> None")

#Display original list (should now be empty)
print("Head ->", " -> ".join(str(x) for x in my_list), "-> None")
