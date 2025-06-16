#Regular expressions
import re
result = re.search(r'\d+', 'Order 12345')
print('1.',result.group())

#Finding 4 letter words
result = re.findall(r'\b\w{4}\b', 'This is a test line with four word terms')
print('2.',result)

result = re.sub(r'\s+', '-', 'hello   world python')  # Output: 'hello-world-python'
print('3.',result)

pattern = re.compile(r'\d{3}-\d{2}-\d{4}')
result = pattern.match('123-45-6789')  # Valid SSN format
print('4.',result)

#Raw strings treat backslashes literally, avoiding double escaping.
#Example: r"\d+" is better than "\\d+"

#Using re.IGNORECASE to ignore case sensitivity
result = re.search(r'hello', 'Hello World', re.IGNORECASE)
print('5.', result.group())  # Output: 'Hello'

#Using re.MULTILINE to match start and end of each line
text = """First line
Second line
Third line"""
result = re.findall(r'^Second', text, re.MULTILINE)
print('6.', result)  # Output: ['Second']

#Using re.DOTALL to match across multiple lines
text = """First line
Second line
Third line"""
result = re.findall(r'.*Second.*', text, re.DOTALL)
print('7.', result)  # Output: ['First line\nSecond line\nThird line']

#Some common regex patterns
common_patterns = {
    'Email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'URL': r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',
    'IP Address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    'Date (YYYY-MM-DD)': r'\d{4}-\d{2}-\d{2}',
}
# Example usage of common patterns
text = "Contact us at support@example.com or visit https://example.com. Server IP: 192.168.1.1. Date: 2024-06-01"

for name, pattern in common_patterns.items():
    match = re.findall(pattern, text)
    print(f"{name}: {match}")

# Examples from realtime applications
# Validating a phone number (format: (123) 456-7890)
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
phone_number = "(123) 456-7890"
if re.match(phone_pattern, phone_number):
    print("Valid phone number format")

# Validating a postal code (format: 12345 or 12345-6789)
postal_code_pattern = r'^\d{5}(-\d{4})?$'
postal_code = "12345-6789"
if re.match(postal_code_pattern, postal_code):
    print("Valid postal code format")