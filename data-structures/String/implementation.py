"""
String Implementation in Python
This module provides common string operations and algorithms.
"""


class StringOperations:
    """A collection of common string operations."""

    @staticmethod
    def reverse(s):
        """
        Reverse a string.
        
        Args:
            s: Input string
            
        Returns:
            Reversed string
        """
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        """
        Check if a string is a palindrome.
        
        Args:
            s: Input string
            
        Returns:
            True if palindrome, False otherwise
        """
        s = s.lower().replace(" ", "")
        return s == s[::-1]

    @staticmethod
    def is_anagram(s1, s2):
        """
        Check if two strings are anagrams.
        
        Args:
            s1: First string
            s2: Second string
            
        Returns:
            True if anagrams, False otherwise
        """
        s1 = s1.lower().replace(" ", "")
        s2 = s2.lower().replace(" ", "")
        return sorted(s1) == sorted(s2)

    @staticmethod
    def count_characters(s):
        """
        Count frequency of each character in a string.
        
        Args:
            s: Input string
            
        Returns:
            Dictionary with character counts
        """
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    @staticmethod
    def find_substring(text, pattern):
        """
        Find the first occurrence of a pattern in text.
        
        Args:
            text: Text to search in
            pattern: Pattern to search for
            
        Returns:
            Index of first occurrence, -1 if not found
        """
        n = len(text)
        m = len(pattern)
        
        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                return i
        return -1

    @staticmethod
    def remove_duplicates(s):
        """
        Remove duplicate characters from a string.
        
        Args:
            s: Input string
            
        Returns:
            String with duplicates removed
        """
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

    @staticmethod
    def is_rotation(s1, s2):
        """
        Check if s2 is a rotation of s1.
        
        Args:
            s1: First string
            s2: Second string
            
        Returns:
            True if s2 is a rotation of s1, False otherwise
        """
        if len(s1) != len(s2):
            return False
        return s2 in (s1 + s1)

    @staticmethod
    def longest_common_prefix(strs):
        """
        Find the longest common prefix among a list of strings.
        
        Args:
            strs: List of strings
            
        Returns:
            Longest common prefix
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    @staticmethod
    def compress_string(s):
        """
        Compress a string using character counts.
        
        Args:
            s: Input string
            
        Returns:
            Compressed string
        """
        if not s:
            return ""
        
        compressed = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                compressed.append(s[i - 1] + str(count))
                count = 1
        
        compressed.append(s[-1] + str(count))
        return ''.join(compressed)


# Example usage
if __name__ == "__main__":
    s = "hello world"
    
    # Reverse string
    print(f"Reverse of '{s}': {StringOperations.reverse(s)}")
    
    # Palindrome check
    print(f"Is 'racecar' a palindrome? {StringOperations.is_palindrome('racecar')}")
    
    # Anagram check
    print(f"Are 'listen' and 'silent' anagrams? {StringOperations.is_anagram('listen', 'silent')}")
    
    # Character count
    print(f"Character count: {StringOperations.count_characters(s)}")
    
    # Find substring
    print(f"Index of 'world' in '{s}': {StringOperations.find_substring(s, 'world')}")
    
    # Remove duplicates
    print(f"Remove duplicates from 'aabbcc': {StringOperations.remove_duplicates('aabbcc')}")
    
    # Rotation check
    print(f"Is 'waterbottle' a rotation of 'erbottlewat'? {StringOperations.is_rotation('waterbottle', 'erbottlewat')}")
    
    # Longest common prefix
    strs = ["flower", "flow", "flight"]
    print(f"Longest common prefix: {StringOperations.longest_common_prefix(strs)}")
    
    # Compress string
    print(f"Compressed 'aaabbc': {StringOperations.compress_string('aaabbc')}")
