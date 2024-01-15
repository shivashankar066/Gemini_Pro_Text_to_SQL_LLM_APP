import os

from dotenv import load_dotenv

load_dotenv()  # load all environmental varibles
import streamlit as st
import google.generativeai as genai
import sqlite3
import os

# Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load Gemini pro model and provide SQL query as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text


# Function to hit the database based on our query and get response

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# Define your prompt
prompt = ["""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    DIVISION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""
          ]

# Streamlit App

st.set_page_config(page_title="Retrival of SQL from Text")
st.header("Gemini App To Retrieve SQL Data from given Text")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is: ")
    for row in response:
        print(row)
        st.info(row)
    st.info("Author: Shivashankar")
