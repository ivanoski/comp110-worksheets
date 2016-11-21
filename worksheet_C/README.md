
##A

Checks if there are duplicates within the list

##B

The maximum number of checks is the length of the list squared minus the length of the list.
O(n*n - n)
 This is because of the nested for loop and the fact it doesnt check a place in the list against itslef

##C

This method still checks every combination of positions in the list but eliminates pairs that would be checked twice in the first algorithm

##D

It cuts out duplicates in the list therefore halving the number of checks

##E

The complexity is still quadratic
O(0.5 * (n * n - n))
even if it runs twice as fast there is still an n ** 2 in the equation

##F

O(nlogn)
wiki.python.org/main/TimeComplexity

##G

O(nlogn + n)
It does the sort function, then the algorithm

##H

The second one as n ** 2 will get much larger much quicker than nlogn

##I

More readable

