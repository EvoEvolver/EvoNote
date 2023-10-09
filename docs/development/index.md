# Overall

IDE recommendation: PyCharm

Docstring style: rst

## DocInPy

Please use the [DocInPy](https://github.com/EvoEvolver/EvoNote/tree/main/doc_in_py) style for adding sections in the codes. 

## Installation

```bash
git clone git@github.com:EvoEvolver/EvoNote.git
pip install -e .
```

# Classes

## Knowledge storage
`Note`: The node of knowledge. It only contains the knowledge itself.

`Tree`: The collection of the references to `Note` objects. It contains **the relationship among knowledge**. It includes parents, children and path in the tree structure. It also contains the indexings of the notes.

## Indexing
`Indexing`: The class for storing the data of one indexing. It can return related notes when provided with queries. It must be interpreted by the `Indexer` class.

`Indexer`: The factory of `Indexing` objects. Indexers are stateless and their state are stored in the `Indexing` object. A `Indexer` should never be instantiated and all its methods should be static. 

## Cache

`CacheManager`: The class for managing the cache of expensive tasks.

`cache_manager`: The instance of `CacheManager` for the whole program. You should import it whenever you want to read and write the caches.

`cache_manager.read_cache(self, input: any, type: str) -> Cache`: `input` should be a hashable. Cache storage and retrieval is realized by matching both `input` and `type`. See https://github.com/EvoEvolver/EvoNote/blob/main/evonote/search/fine_searcher.py for an example of usage.

When you want to discard a certain type of cache. You can use `with cache_manager.refresh_cache(cache_type: str):` to wrap the code that generates the cache. This will disable the cache of the type `cache_type`.

## Debug

In the `debug` file, many useful function for revealing the intermediate results are provided. You can use them to debug the program. For example:
```python
from evonote.debug import display_chats
with display_chats():
    some_code()
```
All the calling of chat completion will be displayed.

See https://github.com/EvoEvolver/EvoNote/blob/main/playground/debug.py for examples of usage.

# Important functionalities

`search`: The folder includes the codes for searching in the knowledge base.

`builder`: The folder includes the codes for building the knowledge base.

