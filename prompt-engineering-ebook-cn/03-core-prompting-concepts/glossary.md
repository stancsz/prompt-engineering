# Glossary of Terms & Acronyms - Chapter 03

**Zero-Shot Learning**: A paradigm in LLM prompting where the model performs a task solely based on a natural language instruction, without any explicit input-output examples for that specific task provided in the prompt.
**One-Shot Learning**: A paradigm in LLM prompting where the prompt includes a single example of an input-output pair that demonstrates the desired task or format, followed by the actual query.
**Few-Shot Learning**: A paradigm in LLM prompting where the prompt includes multiple (typically 2-5 or more) diverse examples of input-output pairs that illustrate the task, followed by the actual query, enabling the model to infer patterns.
**In-Context Learning**: The phenomenon where Large Language Models leverage their vast pre-trained knowledge and instruction-following capabilities to infer a task, pattern, or style from examples provided within the prompt itself, without updating the model's internal weights.
**Instruction-Based Prompt**: A prompting style that provides explicit, natural language commands or directives describing the task the LLM should perform, relying on the model's inherent instruction-following abilities.
**Example-Based Prompt**: A prompting style that provides one or more input-output examples within the prompt to demonstrate the desired task, format, style, or reasoning process, allowing the LLM to infer the pattern (also known as few-shot prompting).
**Prompt Framing**: The strategic design and structuring of a prompt to effectively communicate the user's intent and guide the LLM towards the desired output.
**Prompt Phrasing**: The specific choice of words, sentence structures, and linguistic cues used within a prompt to maximize clarity and minimize ambiguity for the LLM.
**Prompt Clarity**: The quality of a prompt being unambiguous, precise, and easy for the LLM to interpret, leading to more accurate and relevant responses.
**Negative Constraints**: Instructions within a prompt that explicitly tell the LLM what *not* to include or do in its output, helping to prevent undesirable generations.
**Decoding Controls**: Parameters that govern how a Large Language Model selects the next token during the text generation process, allowing fine-tuning of the output's creativity, diversity, coherence, and determinism.
**Temperature**: A decoding parameter that controls the randomness or "creativity" of an LLM's output by influencing the sharpness of the probability distribution over the next token. Higher values increase randomness, lower values increase determinism.
**Top-k Sampling**: A decoding method that restricts the LLM's choice for the next token to only the `k` most probable tokens in the vocabulary, balancing quality with a degree of diversity.
**Top-p Sampling (Nucleus Sampling)**: A decoding method that dynamically selects the smallest set of tokens whose cumulative probability exceeds a predefined threshold `p`, often producing more natural and diverse text than top-k.
**Beam Search**: A greedy decoding algorithm that explores multiple possible sequences (beams) simultaneously to find the most probable overall output, typically resulting in more coherent and grammatically correct but less diverse text.
**Greedy Decoding**: The simplest decoding strategy where the LLM always selects the token with the highest probability at each step, leading to the most deterministic and often repetitive output.
