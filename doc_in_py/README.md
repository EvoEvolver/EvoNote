
# DocInPy - Documentation just in your Python code

`DocInPy` is a standard for putting documentation just in your Python code. It is proposed to provide another option other than the current standard of putting documentation in a separate file. Though it is not new to mix documentation with code, in `DocInPy`, you can also do

- Adding sections to your functions and classes
- Adding examples to your functions and classes

We believe in this way we can provide much more context information to new contributors who are not familiar with the codebase. It is also important for AI-based agents to understand the codebase and develop it.

## EvoNote

EvoNote is using `DocInPy` to document its codebase. You can have a good visualization of EvoNote's codebase by running [EvoNote visualization](https://github.com/EvoEvolver/EvoNote/blob/main/playground/visualize_paper.py).

## How to use

### Sections
Putting sections in `DocInPy` is as easy as putting sections in Markdown. You just need to put a `#` before your section title in a comment environment starting with `"""`. For example,
```python
"""
# Section 1
The following is a function.
"""
def foo():
    pass
"""
# Section 2
The following is another function.
"""
def bar():
    pass
```
In this way, `foo()` and `bar()` will have sections `Section 1` and `Section 2` respectively. The sections will also contain the comments under them.

Your section can also contain classes add levels. For example,
```python
"""
# Top Section
## Section 1
"""
class Foo:
    """
    # Section 1
    The following is a function.
    """
    def foo(self):
        pass
    """
    # Section 2
    The following is another function.
    """
    def bar(self):
        pass
"""
## Section 2
"""
def baz():
    pass
```

### Examples

You can also add examples to your functions and classes. Just define your function with a name starting with `__example`. For example,
```python
def __example_usage_of_foo():
    """
    # Example
    The following is an example of using `foo()`.
    """
    foo()
```

## Project todos

- Extract variables from module and classes
- Extract comments for class variables (What should be the format of the comments?)
- Process code of function and extract comments
- TODO decorator for functions

- Serialization from structs to Python code

## Philosophy behind DocInPy

All the programming languages encourage the programmers to put their code in the tree structure. For example, you can put your functions in difference classes, in different files and put the files in different folders. However, it is still very common to put a lot of functions in a single file, in which the codes are arranged in an almost flat structure.

`DocInPy` helps this by adding a zero-cost way to add sections to your functions and classes. It makes another step towards a more tree-like structure of the codebase. We believe this will help the programmers to understand the codebase better. See [Method of Loci](docs/introduction/2.1 Method of Loci.md) for more details.