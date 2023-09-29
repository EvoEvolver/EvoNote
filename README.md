
# EvoNote: Knowledge base-centered AI system

![Evomark](./docs/evonote.svg)

## Why knowledge base?

Because **non-parametric** knowledge is an **essential piece** towards artificial general intelligence (AGI). We believe that large language model (parametric) + knowledge base (non-parametric) will finally make AGI possible. 

Characteristics of parametric (dense) knowledge (e.g. LLM):

- Good at understanding and reasoning with common knowledge
- Hard to learn & hard to forget due to its **dense nature**.
- Hallucination-prone (Like a **drunk person**)

Characteristics of non-parametric (discrete) knowledge (e.g. knowledge graph):

- Plug-and-play learning and forgetting
- Explainable and accurate
- Not really understanding subtle contexts of objects due to its **discrete nature** (Like a [**Chinese room**](https://plato.stanford.edu/entries/chinese-room/)).

## Core of intelligence-related tasks

Knowledge base (KB) is the core of many intelligence-related tasks.

- **Paper reading**: Based on the text, update the reader's KB by adding / removing / modifying items in it.
- **Academic research**: Actively construct a knowledge base by asking (finding unknown in KB) / reading papers (adding to KB) / meditating (rearranging KB items) / discussing (comparing KBs) / doing experiments (changing confident level of KB items).  
- **Paper writing**: Assuming a KB of the reader, generate a linearized text whose core is the difference between the KB of the reader and the writer.
- **Joke writing**: Assuming a KB of the audience, make 
a text with which the audience can draw an unexpected & reasonable relation among items in the KB.

Typically, these tasks requires 

- Adding / Updating items in the knowledge base by linearized texts
- Comparing two knowledge bases and finding the difference
- Finding new relation among items in the knowledge base and modifying accordingly 

## Why EvoNote

EvoNote is build for holding and operating knowledge bases (notebooks). EvoNote offers

- A tree-based knowledge base framework
- Convenient tools for 
  - constructing knowledge bases from texts and Python modules
  - generating texts or Python codes from knowledge bases
- Tools for exploration to find new insights in knowledge bases (*)
- Tools for export and import knowledge bases to facilitate collaboration (*)

(* means under development)

## What EvoNote is not

- EvoNote does not aim to build large multimodal knowledge bases swiftly and search from it with low latency (e.g. [LlamaIndex](https://github.com/jerryjliu/llama_index), [embedchain](https://github.com/embedchain/embedchain)). Instead, EvoNote provides a more human-like approach, in which the structure of knowledge items is highly non-trivial. With a structure, one can search the knowledge even more semantically than a naive embedding-based search.

- The knowledge base in EvoNote is not a *knowledge graph*. We believe that knowledge graph is too rigid to hold human knowledge. Similar to what is happening in human-brain, the knowledge base in EvoNote is softer and vaguer, whose interpretation is dependent on the language model. 
  - Knowledge graph also allows to many edges to a node, which make the connection of knowledge dense and hard to process.

## Installation

Currently, EvoNote is not ready for production usage. Please refer to the Development section for development usage.

## Development

- In order to use OpenAI API, the environment variables `OPENAI_API_KEY` should be set to your API key.
- PyCharm is recommended.

Idea needed:
- How to efficiently use the structure of the knowledge base to search for useful items?
- How to construct knowledge base items from a paper-long text with high quality?
- How to rearrange the knowledge base items to find new insights?