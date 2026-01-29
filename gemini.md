# Project Constitution (Gemini)

## Data Schemas

### Input Payload

```json
{
  "user_input": "string",
  "template_id": "default" // Future proofing
}
```

### Output Payload

```json
{
  "response": "string (markdown)",
  "model_used": "llama3.2"
}
```

## Behavioral Rules

- **Model**: strictly use `llama3.2`.
- **Interaction**: Input -> Template wrapper -> Ollama API -> Output.
- **Tone**: Professional, technical, QA-focused.
- **Template Source**: Stored within the codebase.

## Architectural Invariants

- **3-Layer Architecture**:
  - Layer 1: Architecture (SOPs in `architecture/`)
  - Layer 2: Navigation (Reasoning)
  - Layer 3: Tools (Scripts in `tools/`)
- **Data-First Rule**: Coding only begins once the "Payload" shape is confirmed.
- **Self-Healing**: Analyze -> Patch -> Test -> Update Architecture.
- **Deliverables**:
  - Local: `.tmp/` (Ephemeral)
  - Global: Payload (Final cloud destination)
