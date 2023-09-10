
# Class

## Knowledge storage
`Note`: The node of knowledge. It only contains the knowledge itself.

`Notebook`: The collection of the references to `Note` objects. It contains **the relationship among knowledge**. It includes parents, children and path in the tree structure. It also contains the indexings of the notes.

## Indexing
`Indexing`: The class for storing the data of one indexing. It can return related notes when provided with queries. It must be interpreted by the `Indexer` class.

`Indexer`: The factory of `Indexing` objects. Indexers are stateless and their state are stored in the `Indexing` object. A `Indexer` should never be instantiated and all its methods should be static. 

# Important functionalities

`search`: The folder includes the codes for searching in the knowledge base.

`writer`: The folder includes the codes for building the knowledge base.



