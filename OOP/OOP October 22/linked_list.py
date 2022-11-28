from node import Node
from sys import maxsize

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        #if the list is empty, the first inserted value becomes the head
        if self.head is None:
            self.head = new_node

        # 'new_node' becomes the head if its value is less than head's value
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            #'new_node' inserted at the middle or end of the list
            previous = self.head
            runner = previous.next

            while (runner is not None) and (runner.value < value):
                previous = runner
                runner = runner.next
                
            new_node.next = runner
            previous.next = new_node

    def print_list_items(self, count=False):
        # print all elements of the list
        element = self.head
        counter = 0
        if element is None:
            print("The list is empty.")
        else:
            while element is not None:
                counter += 1
                print(element.value, end=" ")        
                element = element.next
            print()
            
        if count:
            return counter

    def return_counter(self):
        return self._return_counter_recursively(self.head)

    def _return_counter_recursively(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._return_counter_recursively(node.next)

    def is_node_in_list(self, node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.value == node_value:
                return True
            else:
                current_node = current_node.next
        
        return False

    def delete_node(self, target_value):
        if self.head is None:
            return False
        elif self.head.value == target_value:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next
            while (runner is not None) and (runner.value < target_value):
                previous = runner
                runner = runner.next
            if runner.value == target_value:
                previous.next = runner.next
                return True
            else:
                return False

    def print_reversed(self):
        current = maxsize
        max_node = None
        while self.head.value < current:
            runner = self.head
            while runner.next is not max_node:
                runner = runner.next

            max_node = runner
            print(runner.value, end=" ")
            current = runner.value
        print()
        
    # Estefania's Solution
    def print_reversed_2(self):
        return self.print_reversed_recursive(self.head)

    def print_reversed_recursive(self, node):
        if node is not None:
            self.print_reversed_recursive(node.next)
            print(node.value, end=" ")
