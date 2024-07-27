import inspect
import requests


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    if hasattr(inspect.getmodule(obj), "__name__"):
        info['module'] = inspect.getmodule(obj).__name__
    if info['type'] == 'function':
        info['function_signature'] = inspect.signature(obj)
        info['function_docstring'] = inspect.getdoc(obj)
    elif info['type'] == 'class':
        info['base_classes'] = [base.__name__ for base in obj.__bases__]
        info['class_methods'] = [method for method in info['methods'] if
                                 method in [m[0] for m in inspect.getmembers(obj, predicate=inspect.isfunction)]]
        info['static_methods'] = [method for method in info['methods'] if method in [m[0]
                    for m in inspect.getmembers(obj, predicate=lambda x: inspect.isfunction(x) and getattr(x,'__self__', None) is obj)]]

    return info


if __name__ == "__main__":
    number_info = introspection_info(42)
    print(number_info)
