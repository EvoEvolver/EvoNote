# Testing modules

This package holds the testing modules for agents to use. We want to test the coding ability of agents. Especially, we think the following abilities are important:

- Learn how to use a library by reading its documentation
- Combine domain knowledge in coding
- Write correct code and testing

## Ideas for designing testing modules

Importantly, we do not want the agent to use its knowledge from pretrained models. If the testing modules are about ordinary programming tasks, the agents might have already met them in the corpus. Therefore, we need to make the testing modules looks alien to the agents. To do this, we use the following strategies:

- Write a testing module about a topic rarely appeared in codes (e.g. operating a chemistry lab)
- Rewrite existing topic in a different way. For example, we can rephrase everything about machine learning by magic and put the usage of the magic in the documentation. 

## An example of testing module

```python
"""
## Magic available
"""
def use_fire_ball(target_name: str):
    """Use fire ball to attack the target. Deal 10 damage.

    Args:
        target_name: The name of the target.
    """
    pass

def use_ice_ball(target_name: str):
    """Use ice ball to attack the target. Deal 5 damage.

    Args:
        target_name: The name of the target.
    """
    pass
"""
## Magic usage
Using a fire ball after a ice ball will cause a explosion and deal 5 additional damage.
"""
```

We can ask the agent to write a function to attack a target with a series of magic. The agent should be able to learn the usage of magic from the documentation.

## Format of documentation

We want to mix the documentation with the code by the DocInPy format.
