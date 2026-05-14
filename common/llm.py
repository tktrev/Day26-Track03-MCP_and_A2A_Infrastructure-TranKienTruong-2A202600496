"""Shared LLM factory for all agents.

Uses OpenAI-compatible API, so any provider's model
can be selected via the OPENAI_MODEL env var.
"""

import os

from langchain_openai import ChatOpenAI


def get_llm() -> ChatOpenAI:
    """Return a ChatOpenAI client."""
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base="https://api.openai.com/v1",
        temperature=0.3,
    )