import inspect

def _check_type(value, expected_type, name):
    if not isinstance(value, expected_type):
        raise TypeError(f"Аргумент '{name}' должен быть типа {expected_type}, а не {type(value)}")

def strict(func):
    signature = inspect.signature(func)
    parameters = signature.parameters

    def wrapper(*args, **kwargs):
        for i, (name, param) in enumerate(parameters.items()):
            if param.kind == param.POSITIONAL_OR_KEYWORD and param.annotation:
                _check_type(args[i], param.annotation, name)

        for name, value in kwargs.items():
            param = parameters.get(name)
            if param and param.annotation:
                _check_type(value, param.annotation, name)

        return func(*args, **kwargs)

    return wrapper

#@strict
#def sum_two(a: int, b: int) -> int:
#    return a + b

#print(sum_two(1, 2))  # )))
#print(sum_two(1, 2.4))  # TypeError