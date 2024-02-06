def count_chars(data):
    rus_letters = sum(1 for ch in data if ch >= "А" and ch <= "я")
    return rus_letters

if __name__ == '__main__':
