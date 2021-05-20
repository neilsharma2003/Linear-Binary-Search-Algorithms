# Linear-Binary-Search-Algorithms
For Linear search:

input n integer array elements with spaces between them. Example input: 5 6 2 1
input target integer in array. Example input: 1
Outputs indexes where element has been found or lack thereof 

For Binary search:
Follow same steps as linear search.

If you have a repeating integer in the array (and that's the target), you must search for it seperately. Remove the instance of the integer in the first search and search again. 

The benefit of binary search is that in each operation, we halve the array elements (O(n) = log2(n)) whereas linear search requires a element-by-element scan of the list and this proves inferior when n is large.
