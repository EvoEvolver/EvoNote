import os


def get_stringified_string(s):
    return '"""' + escape_multi_quote(s) + '"""'


def escape_multi_quote(s: str):
    # find the index where 3 or more double quotes appear
    res = []
    search_start = 0
    while True:
        pos = s.find('"""', search_start)
        if pos == -1:
            res.append(s[search_start:])
            break
        else:
            res.append(s[search_start: pos])
            quote_start = pos
            # pos += 3
            while pos < len(s):
                if s[pos] == '"':
                    pos += 1
                else:
                    break
            res.append('\\"' * (pos - quote_start))
            search_start = pos
    return ''.join(res)


def get_stringified_string_with_indent(s: str, indent):
    res = ['"""']
    split = s.splitlines()
    for line in split[:-1]:
        res.append(escape_multi_quote(line))
        res.append("\n")
        res.append(" " * indent)
    res.append(escape_multi_quote(split[-1]))
    res.append('"""')
    return "".join(res)


def get_abs_path(out_path, caller_path):
    if os.path.isabs(out_path):
        abs_path = out_path
    else:
        abs_path = os.path.join(os.path.dirname(caller_path), out_path)
    abs_path = os.path.normpath(abs_path)
    return abs_path
