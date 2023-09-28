from doc_in_py.core import get_module_members
from utils import to_dict


def test_section():
    import testing_module_section
    struct = get_module_members(testing_module_section)
    actual = to_dict(struct)
    expected = {'struct_type': 'module', 'name': 'testing_module_section', 'children': [
        {'struct_type': 'section', 'name': 'Section 1',
         'children': [{'struct_type': 'comment', 'obj': 'Some content xyz'},
                      {'struct_type': 'section', 'name': 'Section 2',
                       'children': [{'struct_type': 'comment', 'obj': 'Some content abc'},
                                    {'struct_type': 'function', 'name': 'foo'}]},
                      {'struct_type': 'section', 'name': 'Section 3', 'children': [
                          {'struct_type': 'comment', 'obj': 'Some content in section 3'},
                          {'struct_type': 'function', 'name': 'bar'},
                          {'struct_type': 'class', 'name': 'baz',
                           'children': [{'struct_type': 'function', 'name': '__init__'},
                                        {'struct_type': 'section', 'name': 'Section 4',
                                         'children': [{'struct_type': 'comment',
                                                       'obj': 'A little bit content'}]}]}]},
                      {'struct_type': 'section', 'name': 'Section 5',
                       'children': [{'struct_type': 'comment', 'obj': 'Good bye'}]}]}]}

    assert actual == expected
