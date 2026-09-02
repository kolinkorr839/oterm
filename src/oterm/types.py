import json
from collections.abc import Callable
from pathlib import Path
from typing import Any, Literal, TypedDict

from pydantic import BaseModel, Field
from pydantic_ai import Tool as PydanticTool
from pydantic_ai.capabilities import AbstractCapability


def _load_custom_defaults() -> dict[str, Any]:
    path = Path(__file__).resolve().parents[2] / "custom_defaults.json"
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


_custom = _load_custom_defaults()

_PROMPTS_DIR = Path(__file__).resolve().parents[2] / "prompts"


def load_prompt_template(name: str | None = None) -> str | None:
    """Load a prompt template by name from the prompts/ directory."""
    template = name or _custom.get("prompt_template")
    if not template:
        return None
    path = _PROMPTS_DIR / f"{template}.md"
    try:
        return path.read_text()
    except FileNotFoundError:
        return None


class ToolDef(TypedDict):
    name: str
    description: str
    tool: PydanticTool


class CapabilityDef(TypedDict):
    name: str
    description: str
    factory: Callable[[], AbstractCapability[None]]


class ChatModel(BaseModel):
    """Chat model for storing chat metadata"""

    id: int | None = None
    name: str = ""
    model: str = _custom.get("model", "")
    system: str | None = _custom.get("system", None)
    provider: str = _custom.get("provider", "ollama")
    parameters: dict[str, Any] = Field(default_factory=lambda: dict(_custom.get("parameters", {})))
    tools: list[str] = Field(default_factory=lambda: list(_custom.get("tools", [])))
    thinking: bool = _custom.get("thinking", False)


class MessageModel(BaseModel):
    """Message model for storing chat messages"""

    id: int | None = None
    chat_id: int
    role: Literal["user", "assistant"]
    text: str
    images: list[str] = Field(default_factory=list)
