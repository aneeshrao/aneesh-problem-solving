# 🧮 Basics of Problem Solving

**Topics Learnt:**  
1. Count the Factors  
2. Check if a Number is Prime  
3. Sum of N Natural Numbers
4. Some Basic Mathematical Notations
5. Formula for [a, b]
6. Formula for (a, b)
7. Geometric Progression (GP)
8. Which Algorithm to use or better at Problem Solving?

## 1. What is a Factor?

A factor of a number is an integer that divides the number evenly, leaving no remainder. 
For example, 

a. The factors of 6 are 1, 2, 3, and 6 because:
- 6 ÷ 1 = 6 (remainder 0)
- 6 ÷ 2 = 3 (remainder 0)
- 6 ÷ 3 = 2 (remainder 0)
- 6 ÷ 6 = 1 (remainder 0)

b. The factors of 100 are 1, 2, 4, 5, 10, 20, 25, 50, and 100 because:
- 100 ÷ 1 = 100 (remainder 0)
- 100 ÷ 2 = 50 (remainder 0)
- 100 ÷ 4 = 25 (remainder 0)
- 100 ÷ 5 = 20 (remainder 0)
- 100 ÷ 10 = 10 (remainder 0)
- 100 ÷ 20 = 5 (remainder 0)
- 100 ÷ 25 = 4 (remainder 0)
- 100 ÷ 50 = 2 (remainder 0)
- 100 ÷ 100 = 1 (remainder 0)


## 2. What is a Prime Number?

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
In other words, a prime number is the number which will have count of factors exactly equal to 2.

For example, 

a. the first few prime numbers are:
- 2 - count of factors = 2 (divisible by 1 and 2)
- 3 - count of factors = 2 (divisible by 1 and 3)
- 5 - count of factors = 2 (divisible by 1 and 5)
- 7 - count of factors = 2 (divisible by 1 and 7)
- 11 - count of factors = 2 (divisible by 1 and 11)
- 13 - count of factors = 2 (divisible by 1 and 13)
- 17 - count of factors = 2 (divisible by 1 and 17)
- 19 - count of factors = 2 (divisible by 1 and 19)
- 23 - count of factors = 2 (divisible by 1 and 23)
- 29 - count of factors = 2 (divisible by 1 and 29)


### 3. Sum of N Natural Numbers

The sum of the first N natural numbers can be calculated using the formula:

`
S = N * (N + 1) / 2
`

Where:
- S is the sum of the first N natural numbers.
- N is the number of natural numbers to be summed.

For example, if N = 5, the sum of the first 5 natural numbers is:

`S = 5 * (5 + 1) / 2 = 5 * 6 / 2 = 30 / 2 = 15`

**Note:** The formula works for any positive integer N. This also called as Arithmetic Progression (AP) where the first term (a) is 1, the last term (l) is N, and the number of terms (n) is N.

### 4. Some Basic Mathematical Notations

1. [a, b] = Both a and b are included in the range.
2. (a, b) = Both a and b are excluded in the range.
3. [a, b) = a is included and b is excluded in the range.
4. (a, b] = a is excluded and b is included in the range.


### 5. Formula for [a, b]:

The count of numbers in the range [a, b] can be calculated using the formula:

`Count = b - a + 1
`

### 6. Formula for (a, b):
The count of numbers in the range (a, b) can be calculated using the formula:

`Count = b - a - 1
`

### 7. Geometric Progression (GP)

A Geometric Progression (GP) is a sequence of numbers where each term after the first is found by multiplying the previous term by a fixed, non-zero number called the common ratio.

The n-th term of a GP can be calculated using the formula:

`Tn = a * r^(n-1)
`

Where:
- Tn is the n-th term of the GP.
- a is the first term of the GP.
- r is the common ratio.
- n is the term number.

For example, in the GP 2, 6, 18, 54, ...:
- a = 2
- r = 3
- The 4th term (T4) is: `T4 = 2 * 3^(4-1) = 2 * 27 = 54`


### 8. Which Algorithm to use or better at Problem Solving?

We as a developers cannot evaluate the execution of the code based on the algorithm we use. Because lot of other factors also play a major role in the execution of the code. Some of them are:
1. Programming Language: Different programming languages have different execution speeds. For example, C++ is generally faster than Python for computational tasks.
2. Compiler/Interpreter: The efficiency of the compiler or interpreter can affect execution time. Some compilers optimize code better than others.
3. Hardware: The performance of the machine (CPU speed, RAM, etc.) can significantly impact execution time.
4. Input Size and Nature: The size and nature of the input data can affect how quickly an algorithm runs. Some algorithms perform better with certain types of data.
5. Implementation: The way an algorithm is implemented can also affect its performance.

The only way to evaluate the execution of the code is by checking the no of iterations the code runs. And based on that we can decide which algorithm to use or better at problem solving.
For example, if an algorithm runs in O(N) time complexity, it means that the number of iterations it runs is directly proportional to the size of the input (N). If N is large, the algorithm will take longer to execute.
