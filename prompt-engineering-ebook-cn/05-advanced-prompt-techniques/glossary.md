# Glossary of Terms & Acronyms - Chapter 5

*   **Prompt Chain:** A sequence of individual prompts where the output of one prompt serves as the input or additional context for the next prompt in the series. This allows for multi-step reasoning, data transformation, and iterative refinement.
*   **Orchestration:** The overarching logic and control flow that manages the execution of a prompt chain. This includes: Sequential Execution, Conditional Logic, Loops, Parallel Execution, Error Handling.
*   **Pipeline:** A structured, end-to-end workflow that defines the sequence of prompts, the data flow between them, and the orchestration logic. Pipelines have clear inputs, intermediate steps, and a final output.
*   **LangChain:** A popular framework for developing applications powered by LLMs. It provides abstractions for chains, agents, prompt templates, and integrations with various LLMs and external tools.
*   **LlamaIndex:** Focuses on data ingestion and retrieval for LLM applications, often used in conjunction with RAG pipelines.
*   **Semantic Kernel:** Microsoft's SDK for integrating LLMs with conventional programming languages, enabling "AI plugins" and chaining.
*   **Retrieval-Augmented Generation (RAG):** An architectural pattern that enhances the LLM's ability to generate responses by first retrieving relevant information from an external knowledge base and then using that information to inform the generation.
*   **Vector Database:** A specialized database for storing high-dimensional numerical vectors (embeddings) and performing similarity searches. Also known as a vector store or vector index.
*   **Memory:** Refers to the LLM's ability to retain and recall information from past interactions within a conversational session or across multiple sessions.
*   **Short-Term Memory (In-Context Memory):** Refers to the information that fits directly within the LLM's current context window.
*   **Long-Term Memory:** Refers to the ability to store and retrieve information from past interactions that extends beyond the current context window, potentially across multiple sessions or even different users.
*   **Programmatic Prompt Generation:** Writing code to dynamically construct prompts, send them to LLM APIs, and process their responses.
*   **API Integration:** The process of connecting and interacting with LLM APIs using code.
*   **Prompt Templating Engines:** Tools that allow you to define prompt structures with placeholders (variables) that are filled with dynamic content at runtime.
*   **LLM SDKs and Libraries:** Software Development Kits (SDKs) provided by LLM providers or higher-level frameworks that abstract away the complexities of direct API calls.
*   **Direct API Integration:** Directly making HTTP requests to LLM endpoints.
*   **Parameter-Efficient Fine-Tuning (PEFT):** Methods that allow you to adapt LLMs to specific tasks or domains by training only a small fraction of the model's parameters.
*   **Prefix Tuning:** Involves learning a small, continuous sequence of task-specific vectors (the "prefix") that are prepended to the input embeddings at each layer of the Transformer model.
*   **Adapters:** Small, lightweight neural network modules inserted *within* each layer of a pre-trained Transformer model.
*   **Soft Prompts (Prompt Tuning / Prompt Learning):** A category of PEFT methods where continuous, trainable vectors are learned and prepended to the input sequence, similar to prefix tuning, but these "prompts" are not human-readable tokens but rather optimized numerical embeddings.
*   **Hallucinations:** The model generates factually incorrect, nonsensical, or fabricated information with high confidence.
*   **Truncation:** The model's output is cut off prematurely, or it fails to consider all provided input context.
*   **Ambiguity/Misinterpretation:** The model misunderstands the intent of the prompt, leading to irrelevant, off-topic, or inconsistent responses.
*   **Overfitting to Examples (in Few-Shot):** The model mimics the provided few-shot examples too literally, failing to generalize to new inputs or adopting an undesired style from the examples.
*   **Irrelevant Output:** The model generates text that is coherent but does not directly address the user's query or the prompt's objective.
*   **Repetition:** The model generates repetitive phrases, sentences, or patterns.
*   **Format Mismatch:** The model fails to adhere to specified output formats (e.g., JSON, bullet points, tables).
*   **Safety/Bias Issues:** The model generates harmful, biased, or inappropriate content.
