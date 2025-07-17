from config import NUMBERS_FILE

def get_next_numbers(start, count):
    try:
        with open(NUMBERS_FILE, "r", encoding="utf-8") as f:
            all_numbers = [line.strip() for line in f if line.strip()]
        return all_numbers[start:start+count]
    except FileNotFoundError:
        return []
