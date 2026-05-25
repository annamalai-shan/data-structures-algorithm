"""
Monotonic Stack Implementation in Python
This module provides monotonic stack implementations for common problems.
"""


class MonotonicStack:
    """A monotonic stack implementation."""

    def __init__(self, increasing=True):
        """
        Initialize a monotonic stack.
        
        Args:
            increasing: If True, maintains increasing order; otherwise decreasing
        """
        self.stack = []
        self.increasing = increasing

    def push(self, value):
        """
        Push a value while maintaining monotonic property.
        
        Args:
            value: Value to push
        """
        if self.increasing:
            while self.stack and self.stack[-1] > value:
                self.stack.pop()
        else:
            while self.stack and self.stack[-1] < value:
                self.stack.pop()
        self.stack.append(value)

    def __len__(self):
        """Return the size of the stack."""
        return len(self.stack)

    def __str__(self):
        """Return string representation of the stack."""
        return str(self.stack)


def next_greater_element(nums):
    """
    Find the next greater element for each element in the array.
    
    Args:
        nums: List of numbers
        
    Returns:
        List where result[i] is the next greater element of nums[i]
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result


def next_smaller_element(nums):
    """
    Find the next smaller element for each element in the array.
    
    Args:
        nums: List of numbers
        
    Returns:
        List where result[i] is the next smaller element of nums[i]
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result


def previous_greater_element(nums):
    """
    Find the previous greater element for each element in the array.
    
    Args:
        nums: List of numbers
        
    Returns:
        List where result[i] is the previous greater element of nums[i]
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    
    return result


def previous_smaller_element(nums):
    """
    Find the previous smaller element for each element in the array.
    
    Args:
        nums: List of numbers
        
    Returns:
        List where result[i] is the previous smaller element of nums[i]
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    
    return result


def daily_temperatures(temperatures):
    """
    Find how many days you have to wait for a warmer temperature.
    
    Args:
        temperatures: List of daily temperatures
        
    Returns:
        List where result[i] is the number of days to wait for a warmer temperature
    """
    n = len(temperatures)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result


def largest_rectangle_area(heights):
    """
    Find the largest rectangle area in a histogram.
    
    Args:
        heights: List of bar heights
        
    Returns:
        Maximum rectangle area
    """
    stack = []
    max_area = 0
    heights.append(0)  # Add sentinel
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area


# Example usage
if __name__ == "__main__":
    # Next greater element
    nums = [2, 1, 2, 4, 3]
    print(f"Next greater element: {next_greater_element(nums)}")
    
    # Next smaller element
    print(f"Next smaller element: {next_smaller_element(nums)}")
    
    # Previous greater element
    print(f"Previous greater element: {previous_greater_element(nums)}")
    
    # Previous smaller element
    print(f"Previous smaller element: {previous_smaller_element(nums)}")
    
    # Daily temperatures
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Days to wait for warmer temp: {daily_temperatures(temps)}")
    
    # Largest rectangle in histogram
    heights = [2, 1, 5, 6, 2, 3]
    print(f"Largest rectangle area: {largest_rectangle_area(heights)}")
