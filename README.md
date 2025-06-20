# fast-offline-inference
Run large language models directly in Python without relying on external APIs.

## Inner workings
- [LLM class](https://docs.modular.com/max/api/python/entrypoints#max.entrypoints.llm.LLM)  provides a Python interface to load and run language models.

>[!Tip]
> You can specify the model from a Hugging Face repository or a local path, MAX handles the process of downloading the model. 

- The PipelineConfig class allows you to specify parameters related to the inference pipeline, e.g., max_length and max_num_steps
- The generate() function is used to generate text from the model


# Installation

Run the following command to create a virtual environment and install the required packages:

## Setup Virtual Environment

```bash
python -m venv .venv/fast-offline-inference \ && source .venv/fast-offline-inference/bin/activate
```

## Install Mojo

```bash
pip install modular \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  --extra-index-url https://modular.gateway.scarf.sh/simple/
  
```

## Run the program

```bash
python main.py
```