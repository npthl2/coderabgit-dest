"""
simple_utils.py - A tiny utility library

This module provides basic utility functions for common operations:
- String manipulation (reverse_string)
- Text analysis (count_words)
- Unit conversions (celsius_to_fahrenheit)

The functions are designed to be simple, efficient, and easy to use
for everyday programming tasks.

Author: npthl2
Created: 2025-06-24
Version: 1.0.0
"""

from typing import Union


def reverse_string(text: str) -> str:
    """
    Reverse the characters in a string.
    
    Takes a string and returns it with all characters in reverse order.
    This function uses Python's slice notation for efficient string reversal.
    
    Args:
        text (str): The string to reverse.
        
    Returns:
        str: A new string with characters in reverse order.
        
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
        >>> reverse_string("12345")
        '54321'
    
    Note:
        This function works with any string, including empty strings,
        numbers, and special characters.
    """
    return text[::-1]


def count_words(sentence: str) -> int:
    """
    Count the number of words in a sentence.
    
    Words are defined as sequences of characters separated by whitespace.
    Multiple consecutive spaces are treated as a single separator.
    Leading and trailing whitespace is ignored.
    
    Args:
        sentence (str): The sentence to count words in.
        
    Returns:
        int: The number of words in the sentence.
        
    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("  hello   world  ")
        2
        >>> count_words("")
        0
        >>> count_words("   ")
        0
        >>> count_words("Python is awesome!")
        3
        
    Note:
        Punctuation attached to words (like "awesome!") is counted
        as part of the word. Use more sophisticated text processing
        if you need to separate punctuation from words.
    """
    return len(sentence.split())


def celsius_to_fahrenheit(celsius: Union[int, float]) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Uses the standard conversion formula: F = C × 9/5 + 32
    This is the most commonly used temperature conversion between
    the Celsius and Fahrenheit scales.
    
    Args:
        celsius (Union[int, float]): Temperature in Celsius degrees.
        
    Returns:
        float: Temperature in Fahrenheit degrees.
        
    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
        >>> celsius_to_fahrenheit(25)
        77.0
        
    Note:
        - Water freezes at 0°C (32°F)
        - Water boils at 100°C (212°F) at standard atmospheric pressure
        - -40°C equals -40°F (the only point where both scales meet)
        
    Raises:
        No explicit validation is performed. Non-numeric inputs
        will raise a TypeError from the mathematical operations.
    """
    return (celsius * 9/5) + 32


# 모듈의 공개 API 정의
__all__ = ['reverse_string', 'count_words', 'celsius_to_fahrenheit']

# 버전 정보
__version__ = '1.0.0'
__author__ = 'npthl2'

if __name__ == "__main__":
    # 간단한 테스트 실행 (doctest 활용)
    import doctest
    print("Running doctest...")
    doctest.testmod(verbose=True)
    print("Documentation tests completed!")
