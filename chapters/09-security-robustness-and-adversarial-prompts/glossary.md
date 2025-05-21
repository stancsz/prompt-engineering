# Glossary of Terms & Acronyms - Chapter 9

*   **Prompt Injection:** A type of adversarial attack where a malicious user crafts an input (a "payload") that tricks the LLM into ignoring its original system instructions or performing unintended actions.
*   **Jailbreaks:** A specific subset of prompt injection attacks designed to bypass the safety guardrails, content moderation filters, or ethical guidelines built into an LLM.
*   **Direct Injection (Inline Injection):** The malicious payload is directly inserted into the user's input field.
*   **Indirect Injection:** The malicious payload is embedded in data that the LLM later processes.
*   **Prompt Sandboxing:** Clearly separate system instructions from user-provided content.
*   **Red Teaming:** Proactively test your LLM application for vulnerabilities by simulating prompt injection and jailbreak attempts.
*   **Sanitization:** The process of cleaning or modifying user-supplied input to remove or neutralize potentially harmful or unintended characters, sequences, or patterns that could alter the prompt's structure or the LLM's instructions.
*   **Validation:** The process of checking whether user-supplied input conforms to a set of predefined rules, constraints, or a specific schema.
*   **Blacklisting:** Attempting to identify and block all known "bad" inputs or patterns.
*   **Whitelisting:** Defining and allowing only "known good" inputs or patterns, rejecting everything else by default.
*   **Token-Level Sanitization:** Malicious inputs can sometimes exploit how LLMs tokenize text.
*   **Guardrails:** Mechanisms designed to ensure that LLM outputs align with ethical guidelines, safety policies, legal requirements, and application-specific rules.
*   **Policy Rules:** Explicit, high-level guidelines that define what content or behavior is permissible or impermissible for the LLM.
*   **Hard Filters (Blocking/Redaction):** Strictly block, truncate, or replace disallowed content.
*   **Soft Filters (Warning/Flagging):** Detects potential policy violations but doesn't immediately block the content; instead, it flags the output for human review or logging.
*   **Pre-processing Guardrails (Input Filtering):** Analyze user input *before* it is sent to the LLM.
*   **In-Prompt Guardrails (Policy Prompting):** Embed policy rules directly into the LLM's system prompt or initial instructions.
*   **Post-processing Guardrails (Output Filtering):** Analyze the LLM's generated output *before* it is displayed to the user.
*   **LLM-based Guardrails (Self-Correction/Moderation):** Using an LLM itself to act as a guardrail by evaluating inputs or outputs against a set of policies.
