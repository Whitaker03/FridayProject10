import openai
import pandas as pd
import sqlite3

# Set your OpenAI API key
key = "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"  # Replace with your actual API key
client = openai.OpenAI(api_key=key)

# Test OpenAI API Connection
prompt = "I’m testing to see if this will work. Please say ‘this test worked’"
try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-2024-08-06",
    )
    print(chat_completion.choices[0].message.content)  # Correct parsing
except Exception as e:
    print(f"API Connection Test Failed: {e}")

# Function to classify sentiment
def analyze_sentiment(comment):
    """
    Classify sentiment of a review using OpenAI API.
    """
    if not comment or not isinstance(comment, str) or comment.strip() == "":
        return "Neutral"  # Handle empty or invalid comments
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that classifies sentiment.",
                },
                {
                    "role": "user",
                    "content": f"Classify the sentiment of this review as Positive, Negative, or Neutral: {comment}",
                },
            ],
            model="gpt-4o-2024-08-06",  # Ensure model matches the one that works for you
        )
        sentiment = response.choices[0].message.content.strip()  # Correct parsing
        return sentiment
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Error"

# Connect to the SQLite database
try:
    conn = sqlite3.connect('feedback.db')
    reviews_df = pd.read_sql_query("SELECT id, comment FROM feedback", conn)
    conn.close()
except sqlite3.Error as e:
    print(f"Database Error: {e}")
    reviews_df = pd.DataFrame()  # Create an empty DataFrame if the query fails

# Check if data was loaded successfully
if not reviews_df.empty:
    print("Data loaded successfully:")
    print(reviews_df.head())

    print("Analyzing sentiments...")
    reviews_df['sentiment'] = reviews_df['comment'].apply(analyze_sentiment)

    # Save the results to a new CSV file
    output_file = 'feedback_with_sentiment.csv'
    reviews_df.to_csv(output_file, index=False)
    print(f"Sentiment analysis completed and saved to '{output_file}'")
else:
    print("No data found or failed to load from the database.")
