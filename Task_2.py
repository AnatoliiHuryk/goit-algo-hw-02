from collections import deque

def is_palindrome(input_string):
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())

    char_deque = deque(normalized_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


test_string = "A man a plan a canal Panama"
print(f"Чи є рядок '{test_string}' паліндромом? {is_palindrome(test_string)}")
