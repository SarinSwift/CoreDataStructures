# CoreDataStructures

## Linked Lists

**Linear data structures**  
Are structured so that items are in order and we have to traverse it sequentially  
Examples are: Arrays, LinkedLists  

**Non-linear data structures**  
Items don't have to be arranged in order  
Examples are: Hashes(Dictionaries), Trees, and Graphs  

   
**Differences of arrays and linked lists:**  
Memory management  
***Arrays:*** Static data structures -- all resources need to be allocated once they are created.
So if more elements needed to be added, you’ll have to copy the whole data in that array and recreate it with
more memory so we can add more data to it   
***LinkedLists:*** Dynamic data structures -- can shrink and grow in memory. Does not need a set amount of data in memory
to be allocated in order to exist  
When an array is created, it needs a certain amount of memory. On the other hand LinkedLists do not need memory all
in one place.  
The nodes can live in different places in memory.  

**Parts of a linked list:**  
Contains self.head, and some cases self.tail  
***Nodes:*** contains data(information that a node contains) and next(a reference to the next node)  
Nodes only know about the data it contains and who it’s next node is.  
Adding and removing nodes is as simple as rearranging the pointers  

**Types of linked lists:**  
 - Singly: Goes in one direction. Has one tracker that can traverse the list  
 - Doubly: 2 references contained within each node  
 - Circular: Does not end with nil. Has a node that acts as the tail(not head)  
 
 **Linked Lists are good to use when:**  
   - You want to add or remove things quickly  
   - Not sure of size of the list  
   - Not worried about finding elements later on  
   - Sure that you wouldn’t need to traverse through the entirety of the list  
