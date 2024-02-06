def count_chars(data):
    rus_letters = sum(1 for ch in data if ch >= "А" and ch <= "я")
    return rus_letters

def is_palindrome(data):
    latin_letters = "abcdefghijklmnopqrstuvwxyz"
    filtered_text = ""

    for char in data:
        if char in latin_letters:
            filtered_text += char

    filtered_text = filtered_text.lower()

    return filtered_text == filtered_text[::-1]

if __name__ == '__main__':
