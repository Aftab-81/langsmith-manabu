from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ No API key found. Check your .env file and variable name (GOOGLE_API_KEY).")
else:
    try:
        embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001"
        )
        embed = embedding_model.embed_query("Hello")
        print("✅ API key is valid and active!")
        print(f"Embedding length: {len(embed)}")
    except Exception as e:
        print("❌ API key failed or model call error.")
        print(f"Error: {e}")