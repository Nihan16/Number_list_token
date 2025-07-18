def get_next_numbers(start_index: int = 0, count: int = 10) -> list[str]:
    """
    Reads a specified number of lines (numbers) from 'numbers.txt' starting from start_index.
    """
    try:
        with open("numbers.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            return [line.strip() for line in lines[start_index : start_index + count]]
    except FileNotFoundError:
        print("Error: numbers.txt not found. Please create the file.")
        return []
    except Exception as e:
        print(f"An error occurred while reading numbers.txt: {e}")
        return []

def get_next_names(start_index: int = 0, count: int = 10) -> list[str]:
    """
    Reads a specified number of lines (names) from 'names.txt' starting from start_index.
    """
    try:
        with open("names.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            return [line.strip() for line in lines[start_index : start_index + count]]
    except FileNotFoundError:
        print("Error: names.txt not found. Please create the file.")
        return []
    except Exception as e:
        print(f"An error occurred while reading names.txt: {e}")
        return []

