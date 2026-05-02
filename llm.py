import os
from groq import Groq
from schema import SCHEMA
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


def generate_sql(user_question):
    prompt = f"""You are a Text-to-SQL translator. Convert natural language questions into valid PostgreSQL queries.

Database schema:
{SCHEMA}

Rules:
1. Return ONLY the SQL query — no explanation, no markdown, no backticks
2. ALWAYS wrap every column name in double quotes e.g. "PhoneService", "Churn", "Contract"
3. String values are case-sensitive — use exact values as listed in the schema
4. The table name is: customers
5. Do not wrap the table name in double quotes
6. If the input is not a valid database question or is random/meaningless text, return exactly: INVALID_QUERY

Question: {user_question}"""
    
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content
  
if __name__ == "__main__":
    sql = generate_sql("show me all customers who are males")
    print(sql)

    from database import run_query
    result = run_query(sql)
    print(result)