def get_next_numbers(start: int, count: int):
    try:
        with open("numbers.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            return lines[start:start + count]
    except FileNotFoundError:
        return []
