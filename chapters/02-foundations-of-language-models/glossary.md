# Glossary of Terms & Acronyms - Chapter 02

**Transformer**: architecture, introduced in 2017, revolutionized NLP by replacing recurrent and convolutional layers with attention mechanisms.
**encoder**: processes input
**decoder**: generates output
**GPT (Generative Pre-trained Transformer) - Decoder-Only Models**: These models consist solely of a Transformer decoder stack. They are *autoregressive*, meaning they generate text one token at a time, predicting the next token based on all previously generated tokens and the input prompt.
**autoregressive**: meaning they generate text one token at a time, predicting the next token based on all previously generated tokens and the input prompt.
**BERT (Bidirectional Encoder Representations from Transformers) - Encoder-Only Models**: These models consist solely of a Transformer encoder stack. They are trained to understand context from both left and right sides of a word in a sentence.
**T5 / Seq2Seq (Encoder-Decoder Models)**: These models utilize both a Transformer encoder and a decoder. They frame all NLP tasks as a "text-to-text" problem, where both input and output are text sequences.
**Pretraining**: To learn general language understanding, generation, and world knowledge from vast amounts of unlabeled text data.
**Fine-Tuning**: To adapt a pretrained model's general knowledge to a specific downstream task or domain.
**Instruction Tuning**: To teach the model to follow human instructions and align its outputs with human preferences, making it more useful and conversational.
**RLHF (Reinforcement Learning from Human Feedback)**: Human evaluators rank model outputs, and this feedback is used to further optimize the model's behavior through reinforcement learning, aligning it with human values and instructions.
**MLM (Masked Language Modeling)**: (for BERT-like models) predicting masked words.
**CLM (Causal Language Modeling)**: (for GPT-like models) predicting the next word.
**Tokenization**: the process of converting raw text into smaller, discrete units called *tokens*.
**tokens**: the fundamental building blocks that LLMs operate on.
**Byte-Pair Encoding (BPE)**: Iteratively merges the most frequent pairs of characters or subwords.
**WordPiece**: Used by BERT, similar to BPE but based on likelihood.
**SentencePiece**: Used by T5, handles multiple languages and allows for training a tokenizer directly from raw text.
**Context Window Limits**: LLMs have a maximum number of tokens they can process in a single input.
**embedding**: After tokenization, each token (or sequence of tokens) is converted into a dense numerical vector called an *embedding*.
**Semantic Similarity**: The cosine similarity between two embedding vectors indicates how semantically similar the corresponding texts are.
**Contextual embeddings**: meaning the embedding for a word like "bank" will differ depending on whether it refers to a financial institution or a river bank.
**RAG (Retrieval Augmented Generation)**: Embeddings are central to RAG systems.
**Vector space**: The collection of all possible embeddings forms a high-dimensional *vector space*.
**Attention mechanisms**: allow an LLM to weigh the importance of different parts of the input sequence when processing each token.
**context window**: (also known as context length or sequence length) refers to the maximum number of tokens an LLM can process and consider at any given time.
**Self-Attention**: The core innovation of the Transformer. Each token in the input sequence computes an "attention score" with every other token.
**Scaled Dot-Product Attention**: A specific, efficient way to compute these attention scores.
**Multi-Head Attention**: Instead of a single attention mechanism, Transformers use multiple "attention heads" in parallel.
