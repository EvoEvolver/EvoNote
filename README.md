
# EvoNote: Knowledge base-centered AI system

<p align="center">
<b>Generate</b>
<br>
<b>Evolve</b>
<br>
<b>Share</b>
<br>
<i>your knowledge base</i> with AI
</p>

## Quick start

```python
from evonote.ui import *
# Build a knowledge base from a text
root_note.s("Introduction to M. Foucault").be(
    writer.build_from(
        """
        Michel Foucault (1926–1984) was a French historian and philosopher,
        associated with the structuralist and post-structuralist movements.
        """
    )
)
# Generate a text from the knowledge base
root_note.s("Example of philosopher").be(
    writer.auto("Give an example of French philosopher")
).show()
"""""show
Michel Foucault
"""""
```

## Why knowledge base?

Because **non-parametric** knowledge is the **last piece** towards artificial general intelligence (AGI). We believe that large language model (parametric) + knowledge base (non-parametric) will finally make AGI possible. 

Characteristics of parametric knowledge (e.g. LLM):

- Fast and efficient
- Understanding and reasoning
- Hard to train & hard to forget
- Hallucination-prone (Like a **drunk person**)

Characteristics of non-parametric knowledge (e.g. notebook):

- Plug-and-play learning and forgetting
- Explainable and accurate
- Less efficient and dependent on parametric knowledge
- Not really understanding (Like a [**Chinese room**](https://plato.stanford.edu/entries/chinese-room/))

## Core of intelligence-related tasks

Knowledge base (KB) is the core of many intelligence-related tasks.

- **Paper reading**: Based on the text, update the reader's KB by adding/removing/modifying items in it.
- **Academic research**: Actively construct a knowledge base by asking (finding unknown in KB) / reading papers (adding to KB) / meditating (rearranging KB items) / discussing (comparing KBs) / doing experiments (changing confident level of KB items).  
- **Paper writing**: Assuming a KB of the reader, generate a linearized text whose core is the difference between the KB of the reader and the writer.
- **Joke writing**: Assuming a KB of the audience, make 
a text with which the audience can draw an unexpected & reasonable relation among items in the KB. (See [humor and art](docs/philosophy/Humor and art.md))

Typically, these tasks requires 

- Adding / Updating items in the knowledge base by linearized texts
- Comparing two knowledge bases and finding the difference
- Finding new relation among items in the knowledge base and modifying accordingly 

## Why EvoNote

EvoNote is build for holding and operating knowledge bases (notebooks). EvoNote offers

- A graph-based knowledge base framework
- Convenient tools for 
  - constructing knowledge bases from texts
  - generating texts from knowledge bases
- Tools for auto-exploration to find new insights in knowledge bases (*)
- Tools for export and import knowledge bases to facilitate collaboration (*)

(* means under development)

## What EvoNote is note

- EvoNote does not aim to build large knowledge bases swiftly and search from it with low latency. Instead, EvoNote provides a more human-like approach, in which the structure of knowledge items is highly non-trivial. With a structure, one can search the knowledge even more semantically than a naive embedding-based search.
 