# Glossary of Terms & Acronyms - Chapter 6

*   **automated metrics**: quantitative ways to measure the performance of LLM outputs, compare different prompt versions, and track improvements over time.
*   **BLEU (Bilingual Evaluation Understudy)**: a precision-focused metric primarily used for evaluating machine translation. It measures the n-gram overlap between the generated text (hypothesis) and one or more human-written reference translations.
*   **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**: a recall-focused metric commonly used for evaluating summarization and machine translation. It measures the overlap of n-grams, word sequences, or word pairs between the generated summary and one or more reference summaries.
*   **Perplexity (PPL)**: a measure of how well a probability distribution or language model predicts a sample. In simpler terms, it quantifies how "surprised" the model is by a given sequence of words.
*   **Embedding Similarity**: Measures the semantic similarity between the embedding vector of the generated text and the embedding vector of a reference text (or query).
*   **human evaluation**: the gold standard for many prompt engineering tasks, especially those involving open-ended generation, complex reasoning, or user-facing applications.
*   **Fluency/Readability**: Is the generated text grammatically correct, natural-sounding, and easy to read?
*   **Relevance**: Does the output directly address the user's query or the prompt's intent? Is it on-topic?
*   **Accuracy/Factuality**: Is the information presented factually correct and free from hallucinations? (Crucial for factual tasks).
*   **Coherence/Consistency**: Does the response flow logically? Is it internally consistent? Does it maintain consistency with previous turns in a conversation?
*   **Completeness**: Does the response provide all necessary information to fulfill the request?
*   **Conciseness**: Is the response brief and to the point, without unnecessary verbosity? (Important for summarization, extraction).
*   **Usefulness/Helpfulness**: Would a human user find this output genuinely helpful or actionable in a real-world scenario?
*   **Safety/Harmlessness**: Is the content free from bias, toxicity, hate speech, or other harmful outputs? (Critical for all applications).
*   **Tone/Style Adherence**: Does the output match the requested tone (e.g., formal, friendly, witty) or style (e.g., journalistic, poetic)?
*   **Creativity/Novelty**: For generative tasks, is the output original, imaginative, and not repetitive?
*   **Likert Scales**: (e.g., 1-5): For subjective criteria like fluency, relevance, usefulness.
*   **Binary Judgments (Yes/No)**: For objective criteria or quick filtering.
*   **A/B testing**: (also known as split testing or controlled experiments) provides a scientific framework, allowing you to compare two or more prompt variants under controlled conditions to identify the best performer with statistical confidence.
*   **Control Group**: The baseline version of the prompt or system that you are currently using or that represents the status quo.
*   **Treatment Group(s)**: The new variant(s) of the prompt or system that you are testing. You can have multiple treatment groups (A/B/n testing).
*   **Metric of Success**: A quantifiable measure that indicates whether a prompt variant is performing better.
*   **Statistical Significance**: The probability that the observed difference between the control and treatment groups is not due to random chance, but rather a true effect of the change.
*   **p-value**: A common measure of statistical significance.
*   **Confidence Interval**: A range of values within which the true difference between the groups is likely to fall.
*   **Null Hypothesis (H0)**: States that there is no significant difference between the control and treatment groups. Any observed difference is due to random chance.
*   **Alternative Hypothesis (H1)**: States that there *is* a significant difference between the groups, and the treatment group is indeed better (or worse) than the control.
