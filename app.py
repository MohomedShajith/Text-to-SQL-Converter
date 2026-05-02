import streamlit as st
from llm import generate_sql
from database import run_query

title = st.title("Text To SQL Converter")

user_question = st.text_input("Enter The Text Quary")

if st.button("Search"):
    sql  = generate_sql(user_question)
    if sql.strip() == "INVALID_QUERY":
        st.warning("Please enter a valid question about the data.")
    else:
        st.code(sql, language="sql")

        try:
            results = run_query(sql)
            st.dataframe(results)
        except:
            st.error("Could not run the query. The generated SQL may have an error.")