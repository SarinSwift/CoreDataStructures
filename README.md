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

## Stacks  
**Last In First Out**
Insertion and deletion happend only from one end of the list 

**Implementations on Arrays**  
Can be problematic because arrays require a set amount of space when initially created.  
Can possibly lead to a stack over flow ( Array won’t have enough space to add on a new item )  

**Implementations on LinkedLists**  
Adding elements to the beginning of the linked list would be O(1) or constant time  
Advantageous because no matter how large your stack is, the runtime will still be O(1)  
Doesn’t go in the problem of ‘stack overflow’ because linkedlists can grow infinitely (dynamicly allocated spaces)  

**Methods:**   
push(): adding elements to the top  
pop(): removing elements from the stack  
top/peek: returns what the first element on top of the stack is  
is_empty(): checks if the stack is empty or not  
size: how big the stack is  

## Queues
**First In First Out**
A linear abstract data type that can contain a long list of elements  

**Implementations on Arrays**  
Can be worse to use arrays with queues depending on the situation and circumstances.  
There can be many cases where we don’t know how big the queue is going to get.  
Enqueue may need copying over old content.  
Resizing also gets more difficult because adding and removing happens from different ends of the array  

**Implementations on LinkedLists**  
Lets the queue resize dynamically using memory.  
Won’t need to know queue size ahead of time because the queue grows dynamically in memory.  
If we use self.head and self.tail pointers in the linked list, we don't need to traverse through all items  
Runtimes for both enqueue and dequeue are O(1)  

**Methods:**  
enqueue(): adding an element to a queue  
dequeue(): removing an element from a queue  
is_empty(): checks if the queue is empty or not  
size: how big the queue is  


## Hash Tables
**Looking upp data quickly without having to search through everything**  
Hash Tables have 2 parts: An array, and a Hash function  
Array: actually holds our data  
Hash function: the way we decide where our data will live. 

Hash tables create a mapping - relationship between 2 sets of data and are O(1) runtime to lookup, add, and delete from the hash table.  
Hash tables are good to use when we quickly want to look up data in our collection.  
They are not good if we want to keep track of ordered data.  

**Good Hash Tables**
1. Should be easy to compute- quick and efficient lookup time  
2. Should avoid collision- The more collisions happen, the harder it is to come up with fast efficient algorithms to resolve them. 
3. Should use all the input data and always return the same key for the same hash bucket per value  

**Hash function**  
Calculated by the hash-value % number of buckets  
This equation will give us the index at which the key should live in.

**Collisions**  
Occurs when a hashing function generates the same index which comes from different keys.  
Collision is almost always expected to happen when mapping out our keys and values.  
Resolutions: Linear probing, and chaining  
***Linear Probing***  
Looking for the next empty bucket in the array. This is a kind of rehashing.  
The function will loop back from the beginning of the table until it finds an available bucket for the element.   
***Chaining***  
Multiple elements can be stored at 1 key.  
The downside is that it takes more time to look up values if there are many in the same bucket.  

It all comes down to creating a good hash function. A 'good' hash function is easy to compute and avoids collision to allow look up times of O(1). But even with these good implementations, we will still run into collisions.
