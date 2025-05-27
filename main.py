from linkedlist import Linkedlist
def main():
    linkedlist=Linkedlist()
    linkedlist.insert_at_front(9)
    linkedlist.insert_at_end(3)
    linkedlist.insert_at_end(2)
    linkedlist.insert_at_front(7)
    node=linkedlist.get_node(3)
    if node is not None:
        print('Found node with data 3')
    else:
        print('Node with data 3 not found')
        
    linkedlist.insert_after(node,5)
    linkedlist.print_list()
    first_node=linkedlist.get_first_node()
    if first_node is not None:
        print(f"First Node {first_node.data}")
    last_node=linkedlist.get_last_node()
    if last_node is not None:
        print(f"Last Node {last_node.data}")  
    linkedlist.delete_node(9)    
    linkedlist.print_list()              
if __name__=="__main__":
    main()        