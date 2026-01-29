# SOP: Test Case Generator

## Goal

Generate detailed, structured test cases based on unstructured user input using a local LLM.

## Inputs

- **User Input**: A natural language description of the feature or requirement.
- **Template**: A structured markdown template defining the expected output format.

## Process

1. **Input Validation**: Ensure user input is not empty.
2. **Template Loading**: Read the `testcase_template.md` from `tools/templates/`.
3. **Prompt Construction**:
   - System Prompt: Define role (QA Engineer).
   - User Prompt: Combine Template + User Input.
4. **LLM Inference**:
   - Call `llama3.2` via Ollama API (`/api/generate`).
   - Parameters: `temperature=0.7` (Creative but structured).
5. **Output Processing**:
   - Return the raw markdown response.

## Error Handling

- **Ollama Offline**: specific error message to user.
- **Model Missing**: logic to prompt user to pull model.
- **Empty Response**: Retry mechanism (max 1 retry).
