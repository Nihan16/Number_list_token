from config import NUMBERS_FILE, NAMES_FILE

def get_next_numbers(start, count):
    try:
        with open(NUMBERS_FILE, "r", encoding="utf-8") as f:
            all_numbers = [line.strip() for line in f if line.strip()]
        return all_numbers[start:start+count]
    except FileNotFoundError:
        return []

def get_next_names(start, count):
    try:
        with open(NAMES_FILE, "r", encoding="utf-8") as f:
            all_names = [line.strip() for line in f if line.strip()]
        return all_names[start:start+count]
    except FileNotFoundError:
        return []
