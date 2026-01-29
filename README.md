# ⚡ B.L.A.S.T. Local LLM Test Case Generator

A deterministic, local LLM-powered test case generator built using the **B.L.A.S.T.** (Blueprint, Link, Architect, Stylize, Trigger) protocol. This system leverages **Ollama (Llama 3.2)** to transform unstructured feature descriptions into structured QA test plans.

## 🏗️ Architecture (A.N.T. 3-Layer)

This project follows the **A.N.T.** (Architecture, Navigation, Tools) 3-layer modular design:

1. **Layer 1: Architecture (`architecture/`)**
    * Contains Technical SOPs (`testcase_generator.md`).
    * Defines the logic, prompt strategy, and validation rules before code is written.

2. **Layer 2: Navigation (Decision Logic)**
    * The `tools/generator.py` script acts as the brains, orchestrating the interaction between the user input, the formal template, and the local LLM.

3. **Layer 3: Tools (`tools/`)**
    * **Engines**: `server.py` (Flask) and `generator.py` (Ollama API wrapper).
    * **Templates**: `tools/templates/testcase_template.md` ensures consistent, high-quality QA output.

## 🚀 Workflow (The B.L.A.S.T. Protocol)

1. **Blueprint**: Define the data schema and North Star in `gemini.md`.
2. **Link**: Verify connection to local Ollama instance via `handshake_ollama.py`.
3. **Architect**: Build the 3-layer system (SOP -> Server -> UI).
4. **Stylize**: Refine the output and provide a modern Dark Mode Chat UI.
5. **Trigger**: Deploy locally and push to GitHub.

## 🛠️ Setup & Usage

### Prerequisites

- [Ollama](https://ollama.com/) installed and running.
* Llama 3.2 model pulled: `ollama pull llama3.2`.
* Python 3.8+.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dasakash10101/blast-framework-llama3.2.git
   cd blast-framework-llama3.2
   ```

2. Install dependencies:

   ```bash
   pip install flask requests
   ```

### Running the Generator

1. Start the Flask server:

   ```bash
   python tools/server.py
   ```

2. Open your browser to `http://localhost:5000`.
3. Enter your feature description and click **Generate**.

## 📄 Project Governance

- **Constitution**: `gemini.md` (Self-healing rules & schemas).
* **Project Memory**: `task_plan.md`, `findings.md`, `progress.md`.
