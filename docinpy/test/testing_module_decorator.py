from docinpy.decorator import todo, example

"""
# Todo for the function
"""


@todo
def summation(a, b):
    """
    Returns the sum of two numbers
    """
    pass


"""
# Todo for the class
"""


@todo("finish this class")
class A:
    """
    A class
    """
    pass


"""
# Example
"""


@example
def how_to_print():
    """
    This is an example
    """
    print("Hello World")
