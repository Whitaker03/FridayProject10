import openai
import pandas as pd

# Set your OpenAI API key
key = "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"  # Replace with your actual OpenAI API key
client = openai.OpenAI(api_key=key)

# Test OpenAI API Connection
try:
    prompt = "I’m testing to see if this will work. Please say ‘this test worked’"
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o-2024-08-06",
    )
    print(chat_completion.choices[0].message.content)  # Test response
except Exception as e:
    print(f"API Connection Test Failed: {e}")

# Define the aspect extraction function
def extract_aspects(comment):
    """
    Extract aspects mentioned in a review using OpenAI API.
    """
    if not comment or not isinstance(comment, str) or comment.strip() == "":
        return "No aspects"  # Handle empty comments
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that extracts aspects or features mentioned in customer reviews."
                },
                {
                    "role": "user",
                    "content": f"Extract the key aspects or features mentioned in this review: {comment}"
                }
            ],
            model="gpt-4o-2024-08-06",
        )
        aspects = response.choices[0].message.content.strip()
        return aspects
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Error"

# Load your dataset
try:
    # Example dataset; replace with actual file or database query
    reviews_df = pd.read_csv('feedback_with_sentiment.csv')  # Replace with your source file
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Dataset file not found.")
    reviews_df = pd.DataFrame()  # Create an empty DataFrame if the file is missing

# Apply aspect extraction if data is available
if not reviews_df.empty:
    print("Extracting aspects from reviews...")
    reviews_df['aspects'] = reviews_df['comment'].apply(extract_aspects)

    # Save the updated dataset
    output_file = 'feedback_with_aspects.csv'
    reviews_df.to_csv(output_file, index=False)
    print(f"Aspect extraction completed and saved to '{output_file}'")
else:
    print("No data available for aspect extraction.")
