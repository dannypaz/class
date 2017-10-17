### Recursion

In order to implement and understand Decision Trees (our next classification algorithm), we'll need a little bit of a refresher on recursion.

Recursion is a very powerful computer science idea. Recursion is when a function calls itself. The idea is to reduce the problem into a simpler version of the same problem until you reduce it to what we call the *base case*.

Several math functions are naturally recursive. For example, *factorial*. Here's an example of factorial: `6! = 6*5*4*3*2*1 = 120`. You can also write it like this: `6! = 6 * 5!`. In this way, we've reduced it to a simpler version of the same problem.

Here's the code:

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
```

Fibonacci is another commonly seen example. The Fibonacci sequence is constructed by summing the two previous numbers to get the next number. Here's the sequence: 0, 1, 1, 2, 3, 5, 8, 11, 21, 33, ...

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

We can also write a sum function, which sums a list, recursively:

```python
def sum(lst):
    if not lst:
        return 0
    return lst[0] + sum(lst[1:])
```

Note that every recursive problem has two cases (can be more too):

* The *Base Case*: This is the stopping point or minimal example. It's an empty list or when an integer is 0. It's the simplest problem that can't be reduced any more.
* The *Recursive Step*: This is where all the work is done. We reduce the problem into a smaller version of the same problem (in solving factorial of n we reduced the problem to solving factorial of n - 1).


### Trees
The examples above can also be easily written *iteratively* (using loops instead of recursion), but there are instances where recursion is really key.

A *tree* in computer science is a *data structure* (way of storing data) which looks like this:

```
         8
       /   \
      5     7
       \   / \
        3 1   2
             /
            6
```

We'll be using them for *decision trees* (discussed below). You can think of those as a flow chart:

![decision tree](images/decisiontree.jpg)

Right now, we'll be dealing with abstract trees so we can get comfortable with how to code with them.

We call each "box" a *node*. Here's the definition of a *binary tree node* (binary means that each node has at most two *children*).

A *binary tree node* is either:
* NULL, or
* Has a *left child* which is a binary tree node and a *right child* which is a binary tree node

A *binary tree* is a structure with a *root* which is a *binary tree node*.

Note that even our definition is recursive!

Here's the code for a `TreeNode`:

```python
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This code would create the binary tree drawn above:

```python
root = TreeNode(8)
root.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(2)
root.right.right.left = TreeNode(6)
```

In general, when you're working with a binary tree, you need to look at the root value and then call your function on both the left and the right subtrees.

For example, to find the minimum, you need to compare the minimum of the left subtree with the minimum of the right subtree and with the root value. The minimum of those three values will be the minimum.

Here's the code:

```python
def find_minimum(root):
    if not root:
        return -1
    else:
        return min((root.value, find_minimum(root.left), find_minimum(root.right)))
```

### Recursion Examples and exercises

* Examples in [examples.py](examples.py)

### Recursion Practice (optional)
We're going to be implementing an algorithm that relies on recursion. We're going to practice with some problems. Write the functions in `recursion_practice.py`.

We'll be using this implementation of a `TreeNode` (in `node.py`) for all the questions concerning trees (2-4):

```python
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

1. Write a recursive function which takes an integer and computes and sum of the digits:

    ```python
    sum_digits(4502)    # returns 11
    ```

    Here's how to think about it recursively:
    ```
    4502 % 10 gives you 2
    4502 / 10 gives you 450
    So sum_digits(4502) = 4502 % 10 + sum_digits(4502 / 10)
    ```

2. Write a function `sum_tree` which sums all the values in a binary tree. Here's how to think about it recursively:

    ```
    sum_tree(root) = sum_tree(root.left) + sum_tree(root.right) + root.value
    ```

3. Write a function `print_all` which prints all the values in a binary tree. In your recursive call you'll need to print `root.left`, `root.right` and `root.value`. You can do these three things in any order and it will affect the order of the outcome.

    As a sidenote these are called *traversals* and each possible order has a name. **Preorder** is `value, left, right`. **Postorder** is `left, right, value`. **Inorder** is `left, value, right`.

4. Write a function `build_coinflip_tree` which takes an integer *k* and builds the tree containing all the possible results of flipping a coin *k* times. The value at each node should be a string of the flips to get there. For example, if *k* is 3, your tree should look like something similar to this:

    ```
                       ''
                     /    \
                   /        \
                 /            \
               /                \
             H                    T
           /   \                /   \
         /       \            /       \
       HH         HT        TH         TT
      /  \       /  \      /  \       /  \
    HHH  HHT   HTH  HTT  THH  THT   TTH  TTT
    ```

    To verify your result, you'll have to just do things like:
    ```python
    root = build_coinflip_tree(3)
    assert root.value == ""
    assert root.left.value == "H"
    assert root.left.left.value == "HH"
    ```
    or build the tree manually and use the `equals` function written in `recusion_examples.py`.
    
    **Hint:** The `value` parameter you'll see in the docstring is so that you can pass to the tree what path you took to get there. It might make the problem a little easier to build a tree like this instead:
    
    ```
         ''
        /  \
       /    \
      H      T
     / \    / \
    H   T  H   T
    ```


## Extra Credit
1. Go back to the traversal problem from above. If you are given the *output* of that function, can you rebuild the tree? Let's say you have the preorder and inorder. Write a function which builds the tree. You can assume values are unique.

    **Hint:** The first item in the preorder traversal is the root. In the inorder traversal, everything to the left of the root is in the left subtree and everything to the right is in the right subtree.

2. Write a function `print_tree` which takes a tree and prints the output in a human readable format.

3. Write a function `make_word_breaks` which takes a string `phrase` and a set `word_list`. The idea is to determine if you can make word breaks in the string. For example: `"thedogruns"` would become `"the dog runs"`. Of course for many strings of letters, this is not possible. Don't worry about being efficient, just try every possibility.