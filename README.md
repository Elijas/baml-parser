# Overview

This project demonstrates how to use the [BAML](https://www.boundaryml.com/) parser by itself, without requiring the full BAML ecosystem. This approach is ideal if you want to experiment with BAML's parsing capabilities while maintaining your current infrastructure.

### How It Works

We start a local server to use as OpenAI API compatible mock API server. The local server receives requests and simply returns the same input it receives. This creates a "pass-through" mechanism that lets you:

1. Continue using your current systems
1. Add BAML's parsing capabilities
1. Avoid a complete migration to the full BAML framework

It serves as a temporary workaround for [BAML Issue #1403](https://github.com/BoundaryML/baml/issues/1403), which addresses the need for using BAML's parser independently from its other components.



# Setup

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/), the python package manager
2. Start the OpenAI API compatible "echo" server:

```uv run litellm --config echo_server/config.yaml --host 127.0.0.1 --port 8200```

3. Run this notebook:

```uv run python -m notebook README.ipynb```

# Examples


```python
import os
os.environ["BAML_LOG"] = "warn"
from baml_client import b
from baml_client.type_builder import TypeBuilder
```

### Example: Static output model


```python
# We have the class defined in the food.baml file:
#
#    class Food {
#        count int
#        items string[]
#    }

llm_response = """
    Of course, I can help you with that. Here is a list of fruits:
    { count: 2.0,, "items": [banana, 'cherry'] }
    Let me know if you need anything else!
"""

b.ParseFood(llm_response)
```




    Food(count=2, items=['banana', 'cherry'])



### Example: Dynamic output model


```python
tb = TypeBuilder()
tb.add_baml("""
   dynamic class Result {
       price float
       tags string[]
   }
""")

llm_response = """
    Here is your answer:
    { price: 42,, "tags": new! }
    Let me know if you need anything else!
"""

b.ParseCompletion(llm_response, {"tb": tb})
```




    Result(price=42.0, tags=['new!'])



### Export README.ipynb to README.md


```python
!uv run jupyter nbconvert --to markdown README.ipynb
```

    [NbConvertApp] Converting notebook README.ipynb to markdown
    [NbConvertApp] Writing 2333 bytes to README.md

