import json
import random
import os

# Topics and templates for intermediate/advanced Python questions
TEMPLATES = [
    ("What is the output of the following code?\n{code}", "{answer}"),
    ("What does the following decorator do?\n{code}", "{answer}"),
    ("How would you implement a context manager for {topic}?", "{answer}"),
    ("Explain the difference between {concept1} and {concept2} in Python.", "{answer}"),
    ("How do you use a generator to {task}?", "{answer}"),
    ("What is the purpose of the __{dunder}__ method?", "{answer}"),
    ("How can you optimize the following code?\n{code}", "{answer}"),
    ("What is the result of this list comprehension?\n{code}", "{answer}"),
    ("How do you use the {module} module to {task}?", "{answer}"),
    ("What exception is raised by the following code?\n{code}", "{answer}"),
]

# Example data for randomization
CONCEPTS = [
    ("list comprehension", "generator expression"),
    ("deep copy", "shallow copy"),
    ("@staticmethod", "@classmethod"),
    ("tuple", "list"),
    ("set", "frozenset"),
    ("__init__", "__new__"),
    ("property", "attribute"),
]
MODULES = [
    ("itertools", "create combinations of a list"),
    ("collections", "use a Counter to count elements"),
    ("functools", "cache function results"),
    ("os", "list files in a directory"),
    ("re", "find all words in a string"),
    ("json", "serialize a dictionary"),
    ("datetime", "get the current date"),
]
DUNDERS = [
    "__str__", "__repr__", "__call__", "__enter__", "__exit__", "__getitem__", "__setitem__", "__iter__", "__next__"
]
TASKS = [
    "yield Fibonacci numbers", "read a large file line by line", "produce an infinite sequence", "filter even numbers from a list"
]
TOPICS = [
    "file handling", "database connections", "thread synchronization", "resource cleanup", "temporary files"
]

# Example code snippets and answers
CODE_SNIPPETS = [
    ("a = [i**2 for i in range(3)]\nprint(a)", "[0, 1, 4]"),
    ("def f():\n    yield from range(2)\nprint(list(f()))", "[0, 1]"),
    ("d = {'a': 1, 'b': 2}\nprint(list(d.keys()))", "['a', 'b']"),
    ("print(type(lambda x: x))", "<class 'function'>"),
    ("print([x for x in range(5) if x % 2 == 0])", "[0, 2, 4]"),
    ("try:\n    1/0\nexcept Exception as e:\n    print(type(e))", "<class 'ZeroDivisionError'>"),
]

ANSWERS = [
    "A decorator modifies the behavior of a function or method.",
    "A context manager handles setup and cleanup actions using __enter__ and __exit__.",
    "A generator yields values one at a time and maintains state between yields.",
    "A deep copy copies nested objects, a shallow copy only top-level references.",
    "@staticmethod does not access class or instance, @classmethod gets the class as first argument.",
    "The __str__ method returns a user-friendly string representation.",
    "The __call__ method makes an instance callable like a function.",
    "The collections.Counter counts hashable objects in an iterable.",
    "The re.findall function returns all non-overlapping matches of a pattern.",
    "ZeroDivisionError is raised when dividing by zero.",
]

def generate_flashcards(n=500):
    flashcards = []
    for _ in range(n):
        template = random.choice(TEMPLATES)
        # Fill in template with random data
        code, code_answer = random.choice(CODE_SNIPPETS)
        concept1, concept2 = random.choice(CONCEPTS)
        module, task = random.choice(MODULES)
        dunder = random.choice(DUNDERS)
        topic = random.choice(TOPICS)
        answer = random.choice(ANSWERS)
        # Prepare question and answer
        question = template[0].format(
            code=code,
            concept1=concept1,
            concept2=concept2,
            module=module,
            task=task,
            dunder=dunder,
            topic=topic
        )
        # For code output, use code_answer, else use answer
        if '{answer}' in template[1]:
            if 'output' in template[0] or 'result' in template[0] or 'exception' in template[0]:
                ans = code_answer
            else:
                ans = answer
            answer_text = template[1].format(answer=ans)
        else:
            answer_text = template[1]
        flashcards.append({
            'question': question,
            'answer': answer_text
        })
    return flashcards

def append_flashcards_to_json(new_flashcards, json_path):
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.extend(new_flashcards)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Appended {len(new_flashcards)} flashcards. Total now: {len(data)}")

if __name__ == "__main__":
    json_path = os.path.join(os.path.dirname(__file__), 'flashcards.json')
    new_flashcards = generate_flashcards(500)
    append_flashcards_to_json(new_flashcards, json_path)
    print("Done.")
