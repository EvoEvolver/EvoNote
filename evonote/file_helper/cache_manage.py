from __future__ import annotations

import hashlib
import json
import os
from typing import Dict, Optional, List

from evonote.utils import get_main_path


def get_hash(input: any, type: str) -> str:
    return hashlib.sha1(json.dumps([input, type]).encode("utf-8")).hexdigest()


class Cache:
    def __init__(self, value, hash: str, input: any, type: str,
                 meta: Optional[Dict] = None):
        self.value = value
        self.hash: str = hash
        self.input: any = input
        self.type: str = type
        self.meta = meta

    def get_self_dict(self):
        return {
            "value": self.value,
            "hash": self.hash,
            "input": self.input,
            "type": self.type,
            "meta": self.meta
        }

    def set_cache(self, value: any, meta: Optional[Dict] = None):
        self.value = value
        self.meta = meta

    def is_valid(self):
        return self.value is not None


CacheTable = Dict[str, Cache]


def serialize_cache_table(cache_table: Dict[str, Cache]):
    res = []
    for key, cache in cache_table.items():
        res.append(cache.get_self_dict())
    return json.dumps(res, indent=1)


def get_cache_file_path(filepath: str):
    return filepath + ".ec.json"


class CacheManager:
    def __init__(self, cache_path: str = None):
        if cache_path is None:
            cache_path = get_cache_file_path(get_main_path())
        self.cache_path = cache_path
        # Map from the file path to the cache table
        self.cache_table: Dict[str, Cache] = self.load_cache_table()
        # List of pending cache
        self.pending_cache: List[Cache] = []

    def save_all_cache_to_file(self):
        self.apply_cache_update()
        with open(self.cache_path, "w") as f:
            f.write(serialize_cache_table(self.cache_table))

    def read_cache(self, input: any, type: str, create_cache=True) -> Cache | None:
        hash = get_hash(input, type)
        cache_table = self.cache_table
        if hash not in cache_table:
            if create_cache:
                new_cache = Cache(None, hash, input, type)
                self.add_cache(new_cache)
                return new_cache
            else:
                return None
        return cache_table[hash]

    def add_cache(self, cache: Cache):
        self.pending_cache.append(cache)

    def apply_cache_update(self):
        remaining_cache = []
        for cache in self.pending_cache:
            if cache.is_valid():
                self.cache_table[cache.hash] = cache
            else:
                remaining_cache.append(cache)
        self.pending_cache = remaining_cache

    def discard_cache_update(self):
        self.pending_cache = []

    def load_cache_table(self) -> CacheTable:
        if not os.path.exists(self.cache_path):
            # Create file if not exists
            with open(self.cache_path, "w") as f:
                f.write("[]")
            return {}
        with open(self.cache_path, "r") as f:
            cache_list = json.load(f)
        cache_table = {}
        for cache_dict in cache_list:
            cache = Cache(cache_dict["value"], cache_dict["hash"], cache_dict["input"],
                          cache_dict["type"], cache_dict["meta"])
            cache_table[cache.hash] = cache
        return cache_table


def save_cache():
    cache_manager.save_all_cache_to_file()


def discard_cache():
    cache_manager.discard_cache_update()


cache_manager = CacheManager()
