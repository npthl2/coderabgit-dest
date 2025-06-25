# Simple Utils 📚

A tiny utility library with essential functions for everyday programming tasks.

## Features

- **String manipulation**: Reverse strings efficiently
- **Text analysis**: Count words in sentences
- **Unit conversion**: Convert Celsius to Fahrenheit

## Installation

Simply download the `simple_utils.py` file and import it into your project:

```python
from simple_utils import reverse_string, count_words, celsius_to_fahrenheit
```

## Quick Start

```python
import simple_utils

# Reverse a string
result = simple_utils.reverse_string("Hello World")
print(result)  # Output: "dlroW olleH"

# Count words in a sentence
word_count = simple_utils.count_words("Python is awesome!")
print(word_count)  # Output: 3

# Convert temperature
fahrenheit = simple_utils.celsius_to_fahrenheit(25)
print(fahrenheit)  # Output: 77.0
```

## API Reference

### `reverse_string(text: str) -> str`

Reverse the characters in a string.

**Parameters:**
- `text` (str): The string to reverse

**Returns:**
- str: A new string with characters in reverse order

**Example:**
```python
>>> reverse_string("hello")
'olleh'
```

### `count_words(sentence: str) -> int`

Count the number of words in a sentence.

**Parameters:**
- `sentence` (str): The sentence to count words in

**Returns:**
- int: The number of words in the sentence

**Example:**
```python
>>> count_words("hello world")
2
```

### `celsius_to_fahrenheit(celsius: Union[int, float]) -> float`

Convert temperature from Celsius to Fahrenheit.

**Parameters:**
- `celsius` (Union[int, float]): Temperature in Celsius degrees

**Returns:**
- float: Temperature in Fahrenheit degrees

**Example:**
```python
>>> celsius_to_fahrenheit(0)
32.0
```

## Testing

The module includes doctest support. Run tests by executing the module directly:

```bash
python simple_utils.py
```

This will run all the examples in the docstrings and verify they produce the expected outputs.

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT License - feel free to use this code in your projects!

## Contributing

Found a bug or want to add a feature? Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Version History

- **1.0.0** (2025-06-24): Initial release with basic utility functions

---

**Author:** npthl2  
**Created:** 2025-06-24  
**Documentation enhanced by:** Claude (Anthropic)
