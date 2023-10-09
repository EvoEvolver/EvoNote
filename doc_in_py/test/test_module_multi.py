from doc_in_py.core import get_module_members
from utils import to_dict


def test_section():
    import testing_module_multi
    struct = get_module_members(testing_module_multi)
    actual = to_dict(struct)
    expected = {'struct_type': 'module', 'name': 'testing_module_multi', 'children': [
        {'struct_type': 'section', 'name': 'first section', 'children': [
            {'struct_type': 'comment',
             'obj': 'This is some annotation to the first section'},
            {'struct_type': 'module', 'name': 'testing_module_multi.a',
             'children': [{'struct_type': 'class', 'name': 'A'}]},
            {'struct_type': 'module', 'name': 'testing_module_multi.b'}]},
        {'struct_type': 'section', 'name': 'second section',
         'children': [{'struct_type': 'module', 'name': 'testing_module_multi.c'},
                      {'struct_type': 'section', 'name': 'another section', 'children': [
                          {'struct_type': 'comment', 'obj': 'This is another section'},
                          {'struct_type': 'module', 'name': 'testing_module_multi.d'},
                          {'struct_type': 'module', 'name': 'testing_module_multi.e'}]}]},
        {'struct_type': 'section', 'name': 'other section', 'children': [
            {'struct_type': 'module', 'name': 'testing_module_multi.another'}]}]}

    assert actual == expected
