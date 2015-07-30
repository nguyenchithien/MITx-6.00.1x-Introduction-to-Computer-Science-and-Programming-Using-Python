L9 PROBLEM 4  (4/4 points)
Note: Before you begin the next set of exercises, you may wish to review these notes on Big O notation.

Determine the complexity of the following tasks.

6.00.1x staff decide to hold an online chess tournament,
and n 6.00.1x students respond to participate in it.




 O(1)
 
 
 O(logn)
 
 
EXPLANATION:

To win, a student will have to play every other student and keep winning,
eliminating students one at a time, a total of n students.
You are asked to write an n page research paper.





 O(1)
 
 O(n2)
 
 
EXPLANATION:

Each page takes 30 mins to write and there are n pages.

You are asked to write an n page personal essay.
You've written plenty of personal essays in your time,






 O(1) <span> <text>O(1) </text> </span> - correct
 O(n)
 
 
 
EXPLANATION:

The number of pages you write does not influence how long it takes you to write.

You just dropped a box of glass toys and n toys in the box broke in half.






 O(1)
 
 
 
EXPLANATION:

You have to compare every piece with every other piece. If you have 1 toy and it breaks in half,
you have 1 comparison to make. If you have 2 toys and they both break in half there are 4 pieces and you have to do 6 comparisons.
If you have 3 toys, there are 6 pieces and you have to do 15 comparisons. If you have N/2 toys, you have N pieces and
