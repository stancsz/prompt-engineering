# Glossary of Terms & Acronyms - Chapter 04

**static templates and dynamic variables**: provides a fixed prompt structure with placeholders that are populated at runtime.
**Static Text**: The unchanging core instructions, context, or formatting guidelines that define the general task.
**Dynamic Variables (Placeholders)**: Specific sections within the static text that are designed to be replaced with user-provided input, retrieved data, or other context-specific information at the time the prompt is sent to the LLM.
**Chain-of-Thought (CoT) prompting**: encourages the model to "think aloud" by generating intermediate reasoning steps before providing a final answer.
**Zero-Shot CoT**: where you merely append a phrase like "Let's think step by step" or "Think step by step and then provide the answer" to your original prompt.
**Few-Shot CoT**: involves providing a few examples of input-output pairs where the output explicitly includes the step-by-step reasoning, followed by the new query.
**Self-Consistency**: Generate multiple CoT paths and then aggregate the final answers (e.g., by majority vote) to improve robustness.
**Tree of Thought (ToT)**: A more advanced technique where the model explores multiple reasoning paths in a tree-like structure, allowing for backtracking and more systematic exploration of solutions.
**Least-to-Most Prompting**: Break down a complex problem into a series of simpler sub-problems, solve each sub-problem, and then use the solutions as context for the next sub-problem.
**ensemble methods**: These techniques involve generating multiple outputs and then aggregating them to arrive at a more robust and often more accurate final answer.
**Voting**: a simpler ensemble technique primarily used for classification, categorization, or selection tasks.
**Ensemble prompts**: involve using *different* prompt formulations, strategies, or even different LLM models to generate outputs for the same task, and then combining or selecting the best result.
**context window**: limits the amount of text they can process at once.
**Chunking**: Breaking down large bodies of text (documents, conversations) into smaller, manageable segments or "chunks" that fit within the LLM's context window.
**Fixed-Size Chunking**: Splitting text into chunks of a predetermined token count.
**Sentence/Paragraph Chunking**: Splitting text based on natural linguistic boundaries (sentences, paragraphs).
**Recursive Chunking**: A more advanced method that attempts to split text by larger units (e.g., sections, paragraphs) first, then recursively splits smaller units if they still exceed the limit.
**Overlap Chunking**: Adding a small overlap (e.g., 10-20% of tokens) between consecutive chunks to preserve context across boundaries.
**Summarization**: Condensing previous interactions or long documents into a shorter, more concise summary that can be fed back into the context window.
**Extractive Summarization**: Identifying and extracting key sentences or phrases directly from the original text.
**Abstractive Summarization**: Generating new sentences and phrases that capture the main ideas, potentially rephrasing content.
**Iterative Summarization**: For very long conversations, periodically summarizing the conversation history and replacing the raw history with its summary.
**RAG (Retrieval-Augmented Generation)**: A powerful pattern that combines the generative capabilities of LLMs with the ability to retrieve relevant information from an external knowledge base.
**vector database (or vector store)**: Your external knowledge base (documents, databases) is processed and converted into numerical embeddings (vector representations) and stored in a **vector database** (or vector store).
**meta-prompting**: involves using an LLM to generate, refine, or evaluate other prompts, enabling more dynamic, scalable, and autonomous workflows.
**higher-order prompts**: refer to a sequence or chain of prompts where the output of one prompt serves as the input or a refinement for a subsequent prompt.
**Meta-Prompt**: A prompt whose primary purpose is to instruct an LLM to generate or modify another prompt.
