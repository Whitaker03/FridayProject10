import openai
key = "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"
client = openai.OpenAI(
api_key=key,
)
prompt ="I’m testing to see if this will work. Please say ‘this test worked’"
chat_completion = client.chat.completions.create(
messages=[
{
"role": "user",
"content": prompt,
}
],
model="gpt-4o-2024-08-06",
)
print(chat_completion.choices[0].message.content)