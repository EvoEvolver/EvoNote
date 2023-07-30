from typing import Callable

from evonote.file_helper.core import Cache
from evonote.file_helper.utils import get_stringified_string


class ValueByInput:
    """
    Class for variables whose value is meaningful only with a certain key
    """

    def __init__(self, value, hash: str, input: any, type: str, meta: any = None,
                 func: Callable = None):
        self.input_hash: str = hash
        self.value = (value, hash)
        self.input = input
        self.type = type
        self.meta = meta
        # Should ensure that self.func(self.input) = self.value
        self.func = func
        self.comment = {}

    def feedback(self):
        pass

    def retake(self):
        assert self.func is not None
        res = ValueByInput(self.func(self.input), self.input_hash, self.input, self.type,
                           self.meta, self.func)
        return res

    @classmethod
    def from_cache(cls, cache: Cache, func: Callable):
        res = ValueByInput(cache._value, cache._hash, cache._input, cache._type)
        res.meta = cache._meta
        res.func = func
        return res

    def set(self, value, input_hash):
        if input_hash == self.input_hash:
            self.value = value

    override_assign = True

    def __setattr__(self, key, incoming_value):
        value = incoming_value
        if key == "value":
            if len(incoming_value) != 2:
                raise ValueError(
                    "ValueByInputHash's assigner must be a tuple of length 2")
            value_carried, hash_to_be_matched = incoming_value
            if hash_to_be_matched == self.input_hash:
                value = value_carried
            else:
                # Do nothing if the key does not match
                return
        super().__setattr__(key, value)

    def __iter__(self):
        return iter(self.value)

    def __str__(self):
        return str(self.value)

    def self_value_in_code(self):
        res = []
        if isinstance(self.value, str):
            res.append(f'{get_stringified_string(self.value)}')
        else:
            res.append(f'{self.value}')
        return "".join(res)
