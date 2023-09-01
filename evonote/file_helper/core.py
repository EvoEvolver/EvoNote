from __future__ import annotations

import hashlib
import inspect
import json
import os
from typing import Dict, Optional, Tuple, List

from evonote.utils import get_main_path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from evonote.file_helper.var_types import ValueByInput


def get_hash(input: any, type: str) -> str:
    return hashlib.sha1(json.dumps([input, type]).encode("utf-8")).hexdigest()


class Cache:
    def __init__(self, value, hash: str, input: any, type: str,
                 meta: Optional[Dict] = None):
        self._value = value
        self._hash: str = hash
        self._input: any = input
        self._type: str = type
        self._meta = meta

    def get_self_dict(self):
        return {
            "value": self._value,
            "hash": self._hash,
            "input": self._input,
            "type": self._type,
            "meta": self._meta
        }

    def set_cache(self, value: any, meta: Optional[Dict] = None):
        self._value = value
        self._meta = meta

    def is_valid(self):
        return self._value is not None


class CacheTable:
    def __init__(self):
        self.map: Dict[str, Cache] = {}

    def __setitem__(self, key, value):
        self.map[key] = value


def serialize_cache_table(cache_table: Dict[str, Cache]):
    res = []
    for key, cache in cache_table.items():
        res.append(cache.get_self_dict())
    return json.dumps(res, indent=1)


class EvoCore:
    def __init__(self):
        # Map from the file path to the cache table
        self.cache_table_map: Dict[str, CacheTable] = {}
        # List of pending cache
        self.pending_cache: List[Tuple[Cache, str]] = []

    def save_all_cache_to_file(self):
        self.apply_cache_update()
        for filepath, cache_table in self.cache_table_map.items():
            with open(filepath + ".ec.json", "w") as f:
                f.write(serialize_cache_table(cache_table.map))

    def read_cache(self, input: any, type: str, create_cache=True) -> Cache | None:
        filepath = get_main_path()
        hash = get_hash(input, type)
        if filepath not in self.cache_table_map:
            self.cache_table_map[filepath] = load_cache_table(filepath)
        cache_table = self.cache_table_map[filepath]
        if hash not in cache_table.map:
            if create_cache:
                new_cache = Cache(None, hash, input, type)
                self.add_cache(new_cache, filepath)
                return new_cache
            else:
                return None
        return cache_table.map[hash]

    def add_value_to_cache(self, var: ValueByInput, filepath: str):
        cache = Cache(var.value, var.input_hash, var.input, var.type)
        self.pending_cache.append((cache, filepath))

    def add_cache(self, cache: Cache, filepath: str):
        self.pending_cache.append((cache, filepath))

    def apply_cache_update(self):
        remaining_cache = []
        for cache, filepath in self.pending_cache:
            if cache.is_valid():
                self.cache_table_map[filepath].map[cache._hash] = cache
            else:
                remaining_cache.append((cache, filepath))
        self.pending_cache = remaining_cache

    def discard_cache_update(self):
        self.pending_cache = []


def load_cache_table(filepath: str) -> CacheTable:
    cache_path = filepath + ".ec.json"
    if not os.path.exists(cache_path):
        # Create file if not exists
        with open(cache_path, "w") as f:
            f.write("[]")
        return CacheTable()
    with open(filepath + ".ec.json", "r") as f:
        cache_list = json.load(f)
    cache_table = CacheTable()
    for cache_dict in cache_list:
        cache = Cache(cache_dict["value"], cache_dict["hash"], cache_dict["input"],
                      cache_dict["type"], cache_dict["meta"])
        cache_table.map[cache._hash] = cache
    return cache_table
