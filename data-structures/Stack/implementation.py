"""
Stack Implementation in Python
This module provides a stack implementation with common operations.
"""


class Stack:
    """A stack implementation using a list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """
        Push an item onto the stack.
        
        Args:
            item: Item to push
        """
        self.items.append(item)

    def pop(self):
        """
        Pop an item from the stack.
        
        Returns:
            The popped item
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        """
        Peek at the top item without removing it.
        
        Returns:
            The top item
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        """
        Return the size of the stack.
        
        Returns:
            Number of elements in the stack
        """
        return len(self.items)

    def __str__(self):
        """Return string representation of the stack."""
        return str(self.items)


def is_balanced_parentheses(s):
    """
    Check if a string has balanced parentheses using a stack.
    
    Args:
        s: String to check
        
    Returns:
        True if balanced, False otherwise
    """
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()


def evaluate_expression(expression):
    """
    Evaluate a postfix expression using a stack.
    
    Args:
        expression: Postfix expression string
        
    Returns:
        Result of the evaluation
    """
    stack = Stack()
    
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    
    return stack.pop()


def reverse_string(s):
    """
    Reverse a string using a stack.
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    """
    stack = Stack()
    
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack after pushes: {stack}")
    
    # Peek
    print(f"Top element: {stack.peek()}")
    
    # Pop elements
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    
    # Size
    print(f"Stack size: {stack.size()}")
    
    # Balanced parentheses
    print(f"Is '(())' balanced? {is_balanced_parentheses('(())')}")
    print(f"Is '(()' balanced? {is_balanced_parentheses('(()')}")
    
    # Postfix evaluation
    expr = "5 3 + 2 *"
    print(f"Evaluate '{expr}': {evaluate_expression(expr)}")
    
    # Reverse string
    s = "hello"
    print(f"Reverse '{s}': {reverse_string(s)}")
