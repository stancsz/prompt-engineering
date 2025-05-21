import os
import pandas as pd
from jinja2 import Template
from openai import OpenAI
from openai import RateLimitError, APIError
import time

# Initialize OpenAI client
try:
    client = OpenAI()
except Exception as e:
    print(f"Error initializing OpenAI client. Ensure OPENAI_API_KEY is set as an environment variable: {e}")
    exit()

# 1. Define the Prompt Template
summarization_template = Template("""
You are a professional summarizer.
Summarize the following article into 3 concise bullet points.
Focus on the main ideas and key facts.

Article:
\"\"\"
{{ article_text }}
\"\"\"

Summary:
""")

# Function to call LLM with retry logic
def get_llm_summary_with_retry(article_text, model="gpt-3.5-turbo", temperature=0.0, max_tokens=150, retries=3, delay=1):
    prompt_content = summarization_template.render(article_text=article_text)
    for i in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt_content}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except RateLimitError:
            print(f"Rate limit hit. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2 # Exponential backoff
        except APIError as e:
            print(f"API Error: {e}. Retrying...")
            time.sleep(delay)
            delay *= 2
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break # Exit on other errors

    print(f"Failed to get LLM summary after {retries} retries for article: {article_text[:50]}...")
    return "Summary generation failed."

def main():
    # 2. Create Input Data (or read from existing articles.csv)
    # For demonstration, let's create a dummy CSV if it doesn't exist
    articles_csv_path = "articles.csv"
    if not os.path.exists(articles_csv_path):
        print(f"'{articles_csv_path}' not found. Creating a dummy one.")
        dummy_data = {
            'id': [1, 2, 3],
            'text': [
                "The recent discovery of a new exoplanet, Kepler-186f, has excited astronomers. It is the first Earth-size planet found in the habitable zone of another star, suggesting it could potentially harbor liquid water and life. This finding opens new avenues for the search for extraterrestrial life.",
                "Quantum computing is a rapidly emerging technology that harnesses the principles of quantum mechanics to solve problems too complex for classical computers. Unlike classical bits, which are either 0 or 1, quantum bits (qubits) can be both simultaneously, enabling exponential processing power.",
                "Artificial intelligence (AI) is rapidly transforming various industries, from healthcare to finance. Machine learning, a subset of AI, enables systems to learn from data without explicit programming. Deep learning, a further subset, uses neural networks with many layers to achieve state-of-the-art performance in tasks like image recognition and natural language processing."
            ]
        }
        df_input = pd.DataFrame(dummy_data)
        df_input.to_csv(articles_csv_path, index=False)
        print(f"Dummy '{articles_csv_path}' created.")
    else:
        print(f"Reading articles from existing '{articles_csv_path}'.")
        df_input = pd.read_csv(articles_csv_path)

    generated_summaries = []

    print("\n--- Starting Summarization Process ---")
    for index, row in df_input.iterrows():
        article_id = row['id']
        article_text = row['text']
        print(f"Processing article ID: {article_id}")

        summary = get_llm_summary_with_retry(article_text)
        generated_summaries.append({'id': article_id, 'summary': summary})
        time.sleep(0.5) # Small delay to be polite to the API

    df_output = pd.DataFrame(generated_summaries)
    output_csv_path = "summaries.csv"
    df_output.to_csv(output_csv_path, index=False)
    print(f"\n--- Summarization Complete! ---")
    print(f"Generated summaries saved to '{output_csv_path}'.")
    print("\nContents of summaries.csv:")
    print(df_output)

if __name__ == "__main__":
    main()
