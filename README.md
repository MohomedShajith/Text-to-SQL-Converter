# 🔍 AI-Powered Text-to-SQL Converter
 
> Query your database in plain English — no SQL knowledge required.
 
---
 
## 📖 About
 
This is an AI-powered Text-to-SQL converter that allows you to filter and query a database using plain natural language. It was built on top of a PostgreSQL database containing customer churn prediction data.
 
**How it works:** Your natural language input is sent to the Groq AI API, which translates it into a valid SQL statement. That query is then executed against the PostgreSQL database, and the results are displayed in a clean Streamlit frontend — alongside the generated SQL query itself. This makes it a great learning tool for anyone looking to understand SQL by comparing their plain-English input with the equivalent query.
 
**Key features:**
 
- Natural language filtering on a real PostgreSQL customer churn dataset
- Groq AI API handles the natural language → SQL translation
- Streamlit frontend displays both the results dataframe and the generated SQL query
- Side-by-side view of input vs. SQL — ideal for learning query syntax
---
 
## 🛠️ Tech Stack
 
| Layer        | Technology                        |
|--------------|-----------------------------------|
| Frontend     | [Streamlit](https://streamlit.io) |
| AI / LLM     | [Groq AI API](https://groq.com)   |
| Database     | PostgreSQL                        |
| Language     | Python 3.10+                      |
| ORM / Driver | `psycopg2`                        |
| Config       | `python-dotenv`                   |
 
---
 
## 🚀 How to Run Locally
 
Follow these steps to get the project running on your machine.
 
### 1. Clone the repository
 
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
 
### 2. Create and activate a virtual environment
 
```bash
python -m venv venv
 
# On macOS/Linux
source venv/bin/activate
 
# On Windows
venv\Scripts\activate
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Set up your environment variables
 
Create a `.env` file in the root of the project (see the [Environment Variables](#-environment-variables) section below) and fill in your credentials.
 
### 5. Set up the PostgreSQL database
 
Make sure PostgreSQL is running locally and that your churn dataset is loaded into the database. Update the connection details in your `.env` file accordingly.
 
### 6. Run the app
 
```bash
streamlit run app.py
```
 
The app will open in your browser at `http://localhost:8501`.
 
---
 
## 🔐 Environment Variables
 
Create a `.env` file in the root directory with the following variables:
 
```env
# Groq AI
GROQ_API_KEY=your_groq_api_key_here
 
# PostgreSQL Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```
 
> ⚠️ Never commit your `.env` file to version control. Make sure it is listed in your `.gitignore`.
 
---
 