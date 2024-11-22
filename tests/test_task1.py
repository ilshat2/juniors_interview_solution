import unittest
from task1.solution import strict

class TestStrictDecorator(unittest.TestCase):

    def test_correct_arguments(self):
        @strict
        def add(a: int, b: int):
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(a=4, b=6), 10)

    def test_incorrect_positional_argument(self):
        @strict
        def multiply(a: int, b: int):
            return a * b

        with self.assertRaises(TypeError) as context:
            multiply("2", 3)
        self.assertEqual(
            str(context.exception),
            "Аргумент 'a' должен быть типа <class 'int'>, а не <class 'str'>"
        )

    def test_incorrect_keyword_argument(self):
        @strict
        def divide(a: int, b: int):
            return a / b

        with self.assertRaises(TypeError) as context:
            divide(a=5, b="2")
        self.assertEqual(
            str(context.exception),
            "Аргумент 'b' должен быть типа <class 'int'>, а не <class 'str'>"
        )

    def test_mixed_arguments(self):
        @strict
        def greet(name: str, age: int):
            return f"Имя {name}, возраст {age}"

        self.assertEqual(greet("Иван", 42))
        self.assertEqual(greet(name="Василий", age=33))

    def test_missing_annotations(self):
        @strict
        def no_annotations(a, b):
            return a + b

        self.assertEqual(no_annotations(2, "3"), "23")

    def test_extra_kwargs(self):
        @strict
        def test_func(a: int, b: int = 0):
            return a + b

        self.assertEqual(test_func(2), 2)
        with self.assertRaises(TypeError) as context:
            test_func(2, b="3")
        self.assertEqual(
            str(context.exception),
            "Аргумент 'b' должен быть типа <class 'int'>, а не <class 'str'>"
        )

if __name__ == "__main__":
    unittest.main()
