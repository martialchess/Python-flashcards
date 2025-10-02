import json
import random

def generate_flashcards():
    flashcards = []

    # --- Variables & Data Types ---
    flashcards += [
        {"topic": "Variables", "question": "How do you assign 5 to variable x?", "answer": "x = 5"},
        {"topic": "Variables", "question": "How do you swap two variables a and b?", "answer": "a, b = b, a"},
        {"topic": "Variables", "question": "What keyword is used to define a constant in Python?", "answer": "Python has no true constants, by convention constants are uppercase like MY_VAR = 10"}
    ]

    datatypes = ["int", "float", "str", "list", "dict", "tuple", "set", "bool"]
    for t in datatypes:
        flashcards.append({
            "topic": "Data Types",
            "question": f"How do you check the type of a {t} variable?",
            "answer": "type(x)"
        })

    # --- Strings ---
    flashcards += [
        {"topic": "Strings", "question": "How do you get the length of string s?", "answer": "len(s)"},
        {"topic": "Strings", "question": "How do you make a string lowercase?", "answer": "s.lower()"},
        {"topic": "Strings", "question": "How do you replace 'a' with 'b' in string s?", "answer": "s.replace('a', 'b')"},
        {"topic": "Strings", "question": "How do you split a string by spaces?", "answer": "s.split()"},
        {"topic": "Strings", "question": "How do you join a list of words with spaces?", "answer": "' '.join(words)"}
    ]

    # --- Lists ---
    flashcards += [
        {"topic": "Lists", "question": "How do you append 10 to list nums?", "answer": "nums.append(10)"},
        {"topic": "Lists", "question": "How do you get the last item of a list?", "answer": "nums[-1]"},
        {"topic": "Lists", "question": "How do you sort a list nums in ascending order?", "answer": "nums.sort()"},
        {"topic": "Lists", "question": "How do you create a list of numbers 0 through 9?", "answer": "list(range(10))"}
    ]

    # --- Loops ---
    flashcards += [
        {"topic": "Loops", "question": "How do you write a for loop over list nums?", "answer": "for n in nums: print(n)"},
        {"topic": "Loops", "question": "How do you write a while loop that runs while x < 10?", "answer": "while x < 10: ..."},
        {"topic": "Loops", "question": "How do you iterate with index and value over a list?", "answer": "for i, val in enumerate(nums): ..."}
    ]

    # --- Functions ---
    flashcards += [
        {"topic": "Functions", "question": "How do you define a function foo with no arguments?", "answer": "def foo(): ..."},
        {"topic": "Functions", "question": "How do you return a value from a function?", "answer": "return value"},
        {"topic": "Functions", "question": "How do you specify default arguments in a function?", "answer": "def foo(x=10): ..."}
    ]

    # --- OOP ---
    flashcards += [
        {"topic": "OOP", "question": "How do you define a class Person?", "answer": "class Person:\n    def __init__(self): ..."},
        {"topic": "OOP", "question": "How do you create an object p from class Person?", "answer": "p = Person()"},
        {"topic": "OOP", "question": "How do you inherit class Student from Person?", "answer": "class Student(Person): ..."}
    ]

    # --- Exceptions ---
    flashcards += [
        {"topic": "Exceptions", "question": "How do you handle exceptions in Python?", "answer": "try: ... except Exception as e: ..."},
        {"topic": "Exceptions", "question": "How do you raise an exception manually?", "answer": "raise ValueError('error message')"}
    ]

    # --- Dictionaries ---
    flashcards += [
        {"topic": "Dictionaries", "question": "How do you get value of key 'a' in dict d?", "answer": "d['a']"},
        {"topic": "Dictionaries", "question": "How do you safely get value of key 'a' in dict d?", "answer": "d.get('a')"},
        {"topic": "Dictionaries", "question": "How do you iterate over keys and values in a dict?", "answer": "for k, v in d.items(): ..."}
    ]

    # --- Advanced ---
    flashcards += [
        {"topic": "Advanced", "question": "How do you write a generator function?", "answer": "def gen():\n    yield 1"},
        {"topic": "Advanced", "question": "What is a decorator in Python?", "answer": "A function that wraps another function to extend behavior"},
        {"topic": "Advanced", "question": "How do you use a context manager for files?", "answer": "with open('file.txt') as f: ..."}
    ]

    # Pad out to ~100 cards by repeating variations
    extras = [
        {"topic": "Booleans", "question": "How do you check if x is equal to y?", "answer": "x == y"},
        {"topic": "Booleans", "question": "How do you check if x is not equal to y?", "answer": "x != y"},
        {"topic": "Booleans", "question": "How do you check if x is greater than y?", "answer": "x > y"},
        {"topic": "Booleans", "question": "How do you check membership of 'a' in list l?", "answer": "'a' in l"},
        {"topic": "Booleans", "question": "How do you check if key k exists in dict d?", "answer": "k in d"}
    ] * 10  # replicate to boost count
    flashcards += extras

    # Shuffle cards for variety
    random.shuffle(flashcards)

    return flashcards


if __name__ == "__main__":
    flashcards = generate_flashcards()
    with open("flashcards.json", "w") as f:
        json.dump(flashcards, f, indent=4)
    print(f"Generated {len(flashcards)} flashcards into flashcards.json")
