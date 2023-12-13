import functions
main_menu = """
1. Insertion in Heap
2. Deletion in Heap
3. Heap Sort
"""
my_tree = functions.binary_tree()
while True:
        choice_main = input(main_menu)
        match choice_main:
            case '1':
                nodes_no = int(input("Enter total nodes you want to put in min heap"))
                for i in range(nodes_no):
                    my_tree.insert_heap_min(int(input("Enter a node to insert in heap : ")))
                for address in my_tree.min_heap:
                    print(address.node_data)
            case '2':
                my_tree.delete_min_heap()

            case '3':
                print("Input an array to sort")
                arr_size = int(input("Enter size of array : "))
                array = []
                for i in range(arr_size):
                    array.append(int(input("Enter an element in array : ")))
                sorted_array = my_tree.heap_sort(array)
                print("Sorted array is : ")
                print(sorted_array)
