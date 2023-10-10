from docinpy.core import get_module_members
from utils import to_dict


def test_decorator():
    import testing_module_decorator
    struct = get_module_members(testing_module_decorator)
    actual = to_dict(struct)
    expected = {'children': [{'children': [{'children': [{'name': 'summation',
                                                          'struct_type': 'function'}],
                                            'name': 'function: summation',
                                            'obj': 'This part is unfinished',
                                            'struct_type': 'todo'}],
                              'name': 'Todo for the function',
                              'struct_type': 'section'},
                             {'children': [{'children': [{'name': 'A',
                                                          'struct_type': 'class'}],
                                            'name': 'class: A',
                                            'obj': 'finish this class',
                                            'struct_type': 'todo'}],
                              'name': 'Todo for the class',
                              'struct_type': 'section'},
                             {'children': [{'children': [{'name': 'how_to_print',
                                                          'struct_type': 'function'}],
                                            'name': 'how_to_print',
                                            'struct_type': 'example'}],
                              'name': 'Example',
                              'struct_type': 'section'}],
                'name': 'testing_module_decorator',
                'struct_type': 'module'}
    assert actual == expected
