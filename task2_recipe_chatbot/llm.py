from llama_cpp import Llama
from typing import List

MODEL_PATH = "models/tinyllama.gguf"

_llm = None


def get_llm():
    """
    Lazy and safe LLM loader.
    Import happens ONLY when endpoint is called.
    """
    global _llm

    if _llm is not None:
        return _llm

    try:
        from llama_cpp import Llama
    except ImportError:
        raise RuntimeError(
            "llama-cpp-python is not installed. "
            "Install it or disable LLM fallback."
        )

    _llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=2048,
        n_threads=4
    )
    return _llm


def generate_recipe_llm(ingredients: List[str]) -> str:
    llm = get_llm()

    prompt = f"""
You are a cooking assistant.

Ingredients: {', '.join(ingredients)}

Suggest ONE simple recipe.
Return recipe name and steps.
"""

    output = llm(prompt, max_tokens=256)
    return output["choices"][0]["text"].strip()