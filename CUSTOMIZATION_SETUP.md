# Custom oterm setup

## Install (editable)

```
~/git/newer_botocore/venv/bin/pip install -e \
  ~/git/oterm
```

## Run

```
~/git/newer_botocore/venv/bin/oterm
```

## Configuration

All custom defaults live in `custom_defaults.json`:

- `model` - default model (qwen3:8b)
- `models` - allowlist for the model dropdown (qwen3:8b, gemma3:latest)
- `prompt_template` - active prompt from `prompts/` (spanish, chinese)
- `thinking` - disable qwen3 thinking via API-level think:false

## Prompt templates

Language-specific system prompts live in `prompts/*.md`. Switch languages
by changing `prompt_template` in `custom_defaults.json`. Add new languages
by creating a new markdown file in `prompts/`.

## Customizations

- Up/Down/PageUp/PageDown scroll chat history from the prompt
- Escape toggles focus between prompt and message area
- Escape dismisses modal screens (prompt history, chat edit)
- Markdown paragraph spacing added
- Teal green header bar
- Splash screen disabled
- Version update notification disabled
- Blank line collapsing in responses
- Auto-create default chat on startup
- Default model: qwen3:8b
