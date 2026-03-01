# Project 09 — AI Chat CLI

**Difficulty:** Advanced
**Topics:** Anthropic API, streaming, conversation history, `argparse`, `.env`

---

## What you're building

Your own terminal chatbot powered by Claude! You'll call the Anthropic API, maintain a conversation history so the AI remembers context, and stream the response word-by-word for a satisfying live feel.

---

## Setup

1. Get your API key at [https://console.anthropic.com](https://console.anthropic.com).
2. Store it safely:
   ```
   # .env
   ANTHROPIC_API_KEY=sk-ant-...
   ```
3. Install dependencies:
   ```
   pip install anthropic python-dotenv
   ```

---

## Requirements

1. Start a chat loop — the user types a message, Claude responds, repeat.
2. Maintain **conversation history** (a list of `{"role": ..., "content": ...}` dicts) and pass it with every request so the model remembers the whole conversation.
3. **Stream** the response using the streaming API so text appears as it's generated.
4. Support a `/quit` command to exit.
5. Support a `/clear` command to reset conversation history.
6. Support a `/system <prompt>` command to set a custom system prompt mid-session.

---

## Example Output

```
You: Hey, what's the capital of Denmark?
Claude: The capital of Denmark is Copenhagen. It's also the largest city
in the country, situated on the eastern coast of the island of Zealand...

You: What's a fun fact about it?
Claude: One fun fact: Copenhagen is consistently ranked as one of the
most bike-friendly cities in the world — over 60% of residents commute
by bicycle daily...

You: /clear
Conversation cleared.
```

---

## Stretch Goals

- [ ] Add a `--persona` flag to start with a preset system prompt (e.g., `--persona chef`, `--persona tutor`).
- [ ] Save conversations to a timestamped log file.
- [ ] Add token usage tracking — show how many tokens were used per reply.
- [ ] Build a `--one-shot` mode for piping: `echo "Summarize this: ..." | python chat.py --one-shot`.
- [ ] Use `rich` or `prompt_toolkit` for colored, nicely formatted terminal output.

---

## Hints

- The Anthropic Python SDK docs: `pip show anthropic` or check the [GitHub repo](https://github.com/anthropics/anthropic-sdk-python).
- Streaming with the SDK looks like:
  ```python
  with client.messages.stream(...) as stream:
      for text in stream.text_stream:
          print(text, end="", flush=True)
  ```
- Always append both the user message AND the assistant's full response to `history` so the context grows correctly.
