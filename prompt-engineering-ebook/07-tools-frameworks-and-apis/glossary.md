# Glossary of Terms & Acronyms - Chapter 7: Tools, Frameworks, and APIs

**Prompting SDKs (Software Development Kits)**: Provide the necessary tools and abstractions to simplify building scalable, maintainable, and intelligent LLM-powered systems.
**Frameworks**: Higher-level tools that provide abstractions and built-in implementations for common LLM patterns.
**LLM (Large Language Model)**: A type of artificial intelligence model trained on vast amounts of text data to understand and generate human-like language.
**RAG (Retrieval-Augmented Generation)**: A technique that combines information retrieval with text generation to improve the factual accuracy and relevance of LLM outputs.
**Chains (LangChain)**: Sequences of LLM calls or other utilities within the LangChain framework.
**Agents (LangChain)**: LLMs within LangChain that can use tools (e.g., search engines, calculators, custom APIs) to achieve a goal.
**Prompt Templates (LangChain)**: Components in LangChain used to manage dynamic prompt construction.
**Document Loaders (LangChain)**: Tools in LangChain to load data from various sources (PDFs, websites, databases).
**Text Splitters (LangChain)**: Utilities in LangChain to chunk documents for context management.
**Embeddings & Vectorstores (LangChain)**: Integrations in LangChain for Retrieval-Augmented Generation (RAG).
**Memory (LangChain)**: Component in LangChain to manage conversational history.
**Callbacks (LangChain)**: Hooks in LangChain for logging, streaming, and monitoring LLM interactions.
**Data Connectors (LlamaIndex)**: Tools in LlamaIndex to load data from various sources.
**Indexes (LlamaIndex)**: Structures in LlamaIndex to organize data for efficient retrieval (e.g., vector indexes, tree indexes).
**Query Engines (LlamaIndex)**: Components in LlamaIndex that combine retrieval and LLM generation for Q&A over data.
**Skills/Plugins (Semantic Kernel)**: Collections of functions (native code or prompts) that the LLM can call within Semantic Kernel.
**Planner (Semantic Kernel)**: An LLM-powered component in Semantic Kernel that orchestrates calls to skills to achieve a user's goal.
**Context (Semantic Kernel)**: Manages the state and memory for the LLM within Semantic Kernel.
**PEFT (Parameter-Efficient Fine-Tuning)**: Techniques that allow for fine-tuning large models with fewer trainable parameters, reducing computational cost.
**Jupyter Notebooks**: Interactive computing environments (including JupyterLab, Google Colab, and VS Code Notebooks) used for rapid experimentation, iterative refinement, visualization, and collaborative development of prompts and LLM workflows.
**Google Colab**: A cloud-based Jupyter notebook environment provided by Google.
**VS Code Notebooks**: Jupyter notebook integration within Visual Studio Code.
**.ipynb**: The standard file extension for Jupyter Notebooks.
**MLOps (Machine Learning Operations)**: A set of practices for deploying and maintaining machine learning models in production.
**Widgets (ipywidgets)**: Interactive elements in Jupyter Notebooks used to create interactive controls like sliders or dropdowns for prompt parameters.
**Weights & Biases Prompts**: An MLOps platform specifically designed for logging, tracing, and monitoring prompt inputs, outputs, and metrics.
**MLflow**: An open-source platform for managing the end-to-end machine learning lifecycle, including experiment tracking, reproducibility, and deployment.
**Git**: A distributed version control system for tracking changes in source code during software development.
**Observability**: The ability to understand the internal state of your system from its external outputs, including comprehensive logging, real-time monitoring, and effective debugging tools.
**Logging**: The practice of recording events, data, and messages generated by your application during its execution, capturing the full lifecycle of a prompt interaction.
**Monitoring**: The continuous collection and aggregation of metrics over time to track the health, performance, and usage patterns of your LLM application.
**Alerting**: Automatically notifying relevant teams or individuals when monitored metrics cross predefined thresholds or when critical events occurs.
**Debugging**: The process of identifying, isolating, and resolving issues within your LLM application, often leveraging logs and monitoring data.
**Structured Logging**: Logging data in a consistent, machine-readable format (e.g., JSON) for easier parsing and analysis by log management systems.
**ELK Stack**: A collection of open-source products—Elasticsearch, Logstash, and Kibana—used for centralized logging, searching, analyzing, and visualizing log data.
**Splunk**: A software platform used to search, analyze, and visualize machine-generated data.
**Datadog**: A monitoring and security platform for cloud applications, offering APM, logging, and metrics.
**Prometheus**: An open-source monitoring system that collects metrics from configured targets.
**Grafana**: An open-source visualization and dashboarding tool, often used with Prometheus for creating dashboards.
**OpenTelemetry**: A set of APIs, SDKs, and tools to instrument, generate, collect, and export telemetry data (metrics, logs, traces).
**Sentry**: A real-time error monitoring tool that provides detailed stack traces and context for exceptions.
**New Relic**: An Application Performance Monitoring (APM) tool that combines metrics, logs, and traces for comprehensive application observability.
**APM (Application Performance Monitoring)**: Tools that combine metrics, logs, and traces to monitor the performance and health of applications.
**LangSmith**: A platform developed by LangChain, specifically providing tracing, evaluation, and monitoring capabilities for LangChain applications.
**Helicone**: An open-source platform for LLM observability, which proxies API calls to track usage, latency, and costs.
**Arize AI**: An MLOps platform that extends to LLM observability, offering experiment tracking, prompt versioning, and performance monitoring.
**Tracing**: The process of following the execution path of a single request across multiple services and LLM calls to understand its flow and identify bottlenecks.
**PII (Personally Identifiable Information)**: Information that can be used to identify, contact, or locate a single person, or can be directly linked to a person.
**Deployment Platforms**: Services and infrastructure used to host and run LLM applications.
**Managed LLM APIs**: Utilizing LLMs as a service directly from cloud providers (e.g., OpenAI API, Anthropic API, Google Cloud Vertex AI, Azure OpenAI Service), where the provider handles model inference, infrastructure, and scaling.
**Self-Hosted Models**: Deploying open-source LLMs on your own infrastructure, either on dedicated servers (on-premises) or on cloud Virtual Machines (VMs) with GPUs.
**Hybrid Architecture**: A deployment strategy combining managed APIs and self-hosted models to leverage the strengths of both.
**Batching**: Grouping multiple independent prompts into a single API request to reduce overhead and improve throughput.
**Asynchronous Calls**: Using non-blocking API calls to send multiple requests concurrently, improving overall responsiveness.
**Caching**: Storing responses to common or identical prompts in a fast-access cache to reduce API calls, lower latency, and decrease load on the LLM.
**Rate Limit Management**: Strategies to handle limits on the number of requests or tokens per minute/second imposed by LLM APIs, often involving retry logic with exponential backoff.
**Exponential Backoff**: A retry strategy that waits progressively longer between retries to gracefully handle rate limit errors and transient network issues.
**Load Balancing**: Distributing incoming requests across multiple instances of an application or multiple LLM endpoints to prevent single points of failure or overload.
**Auto-Scaling**: Automatically adjusting the number of running instances based on demand to ensure optimal resource utilization and performance.
**Model Optimization**: Techniques like using smaller models, quantization, or distillation to reduce model size and inference cost.
**Quantization**: A technique for self-hosted models that reduces model size and inference cost by reducing the precision of model parameters.
**Distillation**: A technique for self-hosted models that involves training a smaller model to mimic a larger one, reducing model size and inference cost.
**Prompt Versioning**: Treating prompts as code, storing them in version control, and using a dedicated prompt registry to track and deploy prompts.
**Prompt Registry**: A dedicated platform or database used to version, track, and deploy prompts.
**Environment Separation**: Maintaining distinct development, staging (or UAT), and production environments with separate API keys and endpoints.
**UAT (User Acceptance Testing)**: A phase of software testing in which the software is tested by the intended audience or users to ensure it meets their needs.
**Shadow Mode**: A deployment strategy where a new version of a service runs alongside the old version, processing live traffic but not affecting the live responses, used for testing.
**Canary Deployments**: A deployment strategy where a new version of a service is rolled out to a small subset of users before being deployed to the entire infrastructure.
**Cost Optimization**: Strategies to reduce the expenses associated with LLM usage, including monitoring token usage, optimizing prompt length, choosing appropriate model sizes, and implementing caching.
**Input/Output Sanitization**: Cleaning and validating user inputs before sending them to LLMs and validating LLM outputs to prevent attacks like prompt injection.
**Prompt Injection**: A type of attack where malicious input is crafted to manipulate an LLM's behavior or extract sensitive information.
**CI/CD (Continuous Integration/Continuous Delivery)**: A set of practices that automate the integration and delivery of code changes, including prompt changes, into production.
**Graceful Degradation**: Designing an application to handle failures or unavailability of LLMs gracefully, such as by falling back to simpler responses or informing the user.
