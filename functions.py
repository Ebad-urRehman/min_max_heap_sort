import numpy as np

class Node:
    def __init__(self, data):
        self.node_data = data
        self.left = None
        self.right = None
        self.root = None

class binary_tree:
    def __init__(self):
        self.my_list = []
        self.min_heap = []
        self.max_heap = []
        self.root = None

    def print_preorder_traversal(self):
        temp_stack = []
        root = self.root
        while root is not None:
            print(root.node_data)
            if root.right is not None:
                temp_stack.append(root.right)
            if root.left is not None:
                root = root.left
            else:
                back_trav = temp_stack.pop()
                root = back_trav

    def inorder_myalgo(self):
        temp_stack = []
        root = self.root
        while root is not None:
            if root.left is not None:
                temp_stack.append(root)
                root = root.left
            else:
                print(root.node_data, end=", ")
                if root.right is not None:
                    temp_stack.append(root.right)
                poped_ele = temp_stack.pop()
                print(poped_ele.node_data, end=", ")
                if poped_ele.right is not None:
                    root = poped_ele.right
                else:
                    if len(temp_stack) >= 1:
                        poped_ele = temp_stack.pop()
                        root = poped_ele
                    else:
                        root = None

    def print_postorder_alg_rem(self):
        # this list will later converted into a stack
        root = self.root
        keys_stack = []
        dict = {}
        while True:
            while root is not None:
                # storing root value in stack
                # stack to keep track of all values
                keys_stack.insert(0, root.node_data)

                # dictionary to find address of coresponding value
                dict[root.node_data] = root

                if root.right is not None:
                    negative_flag = -root.right.node_data
                    # appending right nodedata to temp_stack with -ive sign
                    keys_stack.insert(0, negative_flag)
                    dict[negative_flag] = root.right
                root = root.left

            for i in range(len(keys_stack)):
                if keys_stack[0] >= 0:
                    print(keys_stack[0])
                    # deleting poped values
                    del dict[keys_stack[0]]
                    keys_stack.pop(0)
                else:
                    right_node = dict[keys_stack[0]]
                    root = right_node
                    # deleting poped values
                    del dict[keys_stack[0]]
                    keys_stack.pop(0)
                    break
    def is_instance_node(self, address):
        return isinstance(address, Node)

    def take_input_lvl_wise(self):
        total_levels = int(input("Enter total levels of complete binary tree"))
        total_nodes = (2 ** total_levels) - 1
        print(f"Total Nodes : {total_nodes}")
        my_queue = []
        root_data = int(input("Enter data for root Node"))
        root = Node(root_data)
        self.root = root
        my_queue.insert(0, root)
        self.my_list.append(root)
        nodes_processed = 1
        while nodes_processed != total_nodes:
            poped_ele = my_queue.pop(0)
            current = poped_ele
            if current:
                if current.left is None:
                    data_left = int(input("Enter data for nodes in level order"))
                    new_node_left = Node(data_left)
                    current.left = new_node_left
                    my_queue.append(new_node_left)
                    self.my_list.append(new_node_left)
                    nodes_processed += 1
                if current.right is None:
                    data_right = int(input("Enter data for nodes in level order"))
                    new_node_right = Node(data_right)
                    my_queue.append(new_node_right)
                    current.right = new_node_right
                    self.my_list.append(new_node_right)
                    nodes_processed += 1


    def arr_rep_print(self):
        for address in self.my_list:
            print(address.node_data)

    def find_parent_node(self):
        child_node_pos = int(input("Enter the position of child node to find its parent"))
        if 0 < child_node_pos <= len(self.my_list):
            parent_node_pos = child_node_pos // 2
            print(parent_node_pos)
            print(f"The value at parent Position {parent_node_pos} is : {self.my_list[parent_node_pos - 1].node_data}")
        elif child_node_pos == 0:
            print("The index you entered is of root node")
        else:
            print("Child does not exists")

    def find_child_nodes(self):
        parent_node_pos = int(input("Enter the position of parent node to find its left and right child"))
        parent_node_index = parent_node_pos - 1
        print(f"The value at parent Position {parent_node_pos} is : {self.my_list[parent_node_index].node_data}")
        left_child_index = (2 * parent_node_index) + 1
        right_child_index = (2 * parent_node_index) + 2
        print(f"Left Child Data at Position {left_child_index + 1} is {self.my_list[left_child_index].node_data}")
        print(f"Right Child Data at Position {right_child_index + 1} is {self.my_list[right_child_index].node_data}")

    def find_depth(self):
        total_levels = np.log2(len(self.my_list) + 1)
        print(int(total_levels))

    def insert_heap_min(self, value):
        new_node = Node(value)
        if len(self.min_heap) == 0:
            self.min_heap.append(new_node)
            return

        # finding total nodes which are in heap now
        # +1 as child is on number n+1
        n = len(self.min_heap) + 1
        # this loop breaks in the case where traversed elements reached first node
        while n > 1:
            parent_index = int((n // 2) - 1)
            parent = self.min_heap[parent_index]
            if new_node.node_data < parent.node_data:
                new_node.node_data, parent.node_data = parent.node_data, new_node.node_data
                n = parent_index + 1
            else:
                break

        self.min_heap.append(new_node)

    def insert_heap_max(self, value):
        new_node = Node(value)
        if len(self.max_heap) == 0:
            self.max_heap.append(new_node)
            return

        # finding total nodes which are in heap now
        # +1 as child is on number n+1
        n = len(self.max_heap) + 1
        # this loop breaks in the case where traversed elements reached first node
        while n > 1:
            parent_index = int((n // 2) - 1)
            parent = self.max_heap[parent_index]
            if new_node.node_data > parent.node_data:
                new_node.node_data, parent.node_data = parent.node_data, new_node.node_data
                n = parent_index + 1
            else:
                break

        self.max_heap.append(new_node)

    def delete_min_heap(self):
        if len(self.min_heap) == 0:
            print("Insert heap first")
        total_nodes = len(self.min_heap)
        for i in range(len(self.min_heap)):
            print(self.min_heap[i].node_data)
        last = self.min_heap[-1]
        # storing last node data for sink traversal
        current = last
        # deleting last node
        self.min_heap.pop(-1)
        current_index = 0
        left = 1
        right = 2
        while right < total_nodes:
            if current.node_data <= self.min_heap[left].node_data and current.node_data <= self.min_heap[right].node_data:
                self.min_heap[current_index] = current.node_data
                return
            if self.min_heap[left].node_data <= self.min_heap[right].node_data:
                self.min_heap[current_index] = self.min_heap[left]
                current_index = left
            else:
                self.min_heap[current_index].node_data = self.min_heap[right].node_data
                current_index = right
            left = 2 * current_index + 1
            right = 2 * current_index + 2

        def delete_max_heap(self):
            if len(my_tree.max_heap) == 0:
                print("Insert heap first")
            first = self.root
            total_nodes = len(self.max_heap)
            last = self.max_heap[-1]
            # storing last node data for sink traversal
            current = last
            # deleting last node
            self.max_heap.pop(-1)
            current_index = 0
            left = 1
            right = 2
            while right <= total_nodes:
                if current.node_data <= self.max_heap[left].node_data and current.node_data <= self.max_heap[
                    right].node_data:
                    self.max_heap[current_index] = current.node_data
                    return
                if self.max_heap[left] <= self.max_heap[right]:
                    self.max_heap[current_index] = self.max_heap[left]
                    current_index = left
                else:
                    self.max_heap[current_index] = self.max_heap[right]
                    current_index = right
                left = 2 * current_index
                right = 2 * current_index + 1


    def delete_min_heap(self):
        if len(self.min_heap) == 0:
            print("Heap is empty. Cannot delete.")
            return None

        # Swap the root (minimum element) with the last element in the heap
        min_value = self.min_heap[0].node_data
        last_node = self.min_heap.pop()
        if len(self.min_heap) > 0:
            self.min_heap[0].node_data = last_node.node_data
            self.min_heapify(0)  # Restore the heap property
        print("Deleted successfully")
        for address in self.min_heap:
            print(address.node_data)
        return min_value

    def min_heapify(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        # Compare with left child
        if left_child_index < len(self.min_heap) and \
                self.min_heap[left_child_index].node_data < self.min_heap[smallest].node_data:
            smallest = left_child_index

        # Compare with right child
        if right_child_index < len(self.min_heap) and \
                self.min_heap[right_child_index].node_data < self.min_heap[smallest].node_data:
            smallest = right_child_index

        # If the smallest is not the current index, swap and recursively heapify
        if smallest != index:
            self.min_heap[index].node_data, self.min_heap[smallest].node_data = \
                self.min_heap[smallest].node_data, self.min_heap[index].node_data
            self.min_heapify(smallest)

    def heap_sort(self, my_list):
        # Build a min heap using insert_heap_min
        for element in my_list:
            self.insert_heap_min(element)
        sorted_list = []
        # Delete elements from the min heap and append to the sorted_list
        while self.min_heap:
            sorted_list.append(self.min_heap[0].node_data)
            self.delete_min_heap()
        return sorted_list


if __name__ == "__main__":
    nodes_no = int(input("Enter total nodes you want to put in min heap"))
    my_tree = binary_tree()
    for i in range(nodes_no):
        my_tree.insert_heap_min(int(input("Enter a node to insert in heap : ")))
    for address in my_tree.min_heap:
        print(address.node_data)

    # my_tree.delete_min_heap()
    # print("Deleted")
    # my_tree.delete_min_heap()
    # print("Deleted")
    # my_tree.delete_min_heap()
    # print("Deleted")
    print("Input an array to sort")
    arr_size = int(input("Enter size of array : "))
    array = []
    for i in range(arr_size):
        array.append(int(input("Enter an element in array : ")))

    my_tree.heap_sort()
    print("array is sorted now")
    for address in my_tree.min_heap:
        print(address.node_data)

