# Custom oterm setup

## Install (editable)

```
/Users/jcua/git/newer_botocore/venv/bin/pip install -e \
  /Users/jcua/git/oterm
```

## Create custom Ollama models

```
ollama create spanish-teacher \
  -f /Users/jcua/git/oterm/Modelfile.spanish-teacher
```

## Run

```
/Users/jcua/git/newer_botocore/venv/bin/oterm
```

## Customizations

- Up/Down/PageUp/PageDown scroll chat history from the prompt
- Escape toggles focus between prompt and message area
- Markdown paragraph spacing added
- Teal green header bar
- Splash screen disabled
- Default model: gemma3:latest
