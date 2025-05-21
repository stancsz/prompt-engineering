# Glossary of Terms & Acronyms - Chapter 03

**Zero-Shot Learning**: The model performs a task solely based on the natural language instruction provided in the prompt, without any explicit examples of input-output pairs for that specific task.
**One-Shot Learning**: The prompt includes a single example of an input-output pair that demonstrates the desired task or format, followed by the actual query.
**Few-Shot Learning**: The prompt includes multiple (typically 2-5, but can be more) examples of input-output pairs that illustrate the task, followed by the actual query.
**in-context learning**: The model leverages its vast pre-trained knowledge to infer the task from the provided context.
**instruction-based prompts**: provides explicit, natural language commands or directives that describe the task the LLM should perform.
**example-based prompt**: (also known as few-shot prompting) provides one or more input-output examples *before* the actual query.
**frame**: your request
**phrasing**: you choose
**clarity**: of your instructions
**Negative Constraints**: Telling the Model What *Not* to Do
**decoding controls**: These parameters govern how the Large Language Model (LLM) selects the next token during the text generation process, allowing you to fine-tune the output's creativity, diversity, coherence, and determinism.
**Temperature**: a parameter that controls the randomness or "creativity" of the model's output.
**Top-k sampling**: restricts the model's choice for the next token to only the `k` most probable tokens in the vocabulary.
**Top-p sampling (also known as nucleus sampling)**: selects the smallest set of tokens whose cumulative probability exceeds a threshold `p`.
**Beam search**: a greedy decoding algorithm that explores multiple possible sequences (called "beams") simultaneously to find the most probable output.
**Greedy Decoding**: The simplest decoding strategy, where the model always selects the token with the highest probability at each step.
