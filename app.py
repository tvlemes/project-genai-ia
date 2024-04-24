'''
Gerador de código SQL com Genai da Google

Autor: `Thiago Vilarinho Lemes`
Data: `23/04/2024`
'''
# importing the necessary libraries
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ['API_KEY']
# setting web app page name and selecting wide layout(optional)
st.set_page_config(page_title='Geração de SQL', layout='wide', page_icon='./docs/icon.png')#,layout="wide") # option-1 without wide layout
# st.set_page_config(page_title='Text-To-SQL APP',page_icon=None,layout="wide") # option-2 with wide layout

# setting column size 
# col1, col2 = st.columns((0.3,1.7))    # without wide layout ( option-1)
# col1, col2 = st.columns((0.15,1.7)) # with wide layout

# col1.image('text_to_sql_logo.jpeg')
# col2.markdown("# :rainbow[ SQL QUERY AI ASSISTANT APP]")
st.write( "#### :blue[ Este é o aplicativo da Web SQL Query Generator usando o Google Gemini! ]")

query_input =st.text_area('Por favor, insira seu prompt usando inglês simples')
submit=st.button("Gerar SQL")

# defining the api key and loading the gemini pro 
genai.configure(api_key=API_KEY)  # put your secret api key here
model=genai.GenerativeModel('gemini-pro')

########################################################################################################

# this information helps the LLM model output to be more accurate when generating the sql query
# it is advised to put relevant supportive information, to make the sql query generated be precise,
# supportive_info1 = ["""Based on the  prompt text, create a SQL query, and make sure to exclude ''' in the beginning and end."""]

# if submit is clicked
# if submit:
#     #creating the columns side by side 
#     # col1, col2, col3 = st.columns((0.7,1.0,1.0)) # with wide layout ,
#     with st.spinner("Generating.."):
#         st.write("##### 1. The Generated SQL Query Code :")
#         response=model.generate_content([supportive_info1[0], query_input])
#         st.code(response.text)

# # defining the api key and loading the gemini pro
# genai.configure(api_key="API_KEY")  # 
# model=genai.GenerativeModel('gemini-pro')

# # defining supportive information for the gemini llm model
# # this information helps the LLM model output to be more accurate when generating the sql query
# supportive_info1 = ["""Based on the  prompt text, create a SQL query, and make sure to exclude ''' in the beginning and end."""]
# supportive_info2 = ["""Based on the SQL query code, create an example input dataframe before the SQL query code is applied and the output dataframe after the SQL query is applied. """]
# supportive_info3 = [""" Explain the SQL query in detail without any example output."""]

# # Use the model to generate content based on the supportive information and query input provided
# response=model.generate_content([supportive_info1[0], query_input])
# response2=model.generate_content([supportive_info2[0], response.text])
# response3=model.generate_content([supportive_info3[0], response.text])

########################################################################################################

# defining the api key and loading the gemini pro
genai.configure(api_key=API_KEY)  # 
model=genai.GenerativeModel('gemini-pro')

# defining supportive information for the gemini llm model
# this information helps the LLM model output to be more accurate when generating the sql query
supportive_info1 = ["""Based on the  prompt text, create a SQL query, and make sure to exclude ''' in the beginning and end."""]
supportive_info2 = ["""Based on the SQL query code, create an example input dataframe before the SQL query code is applied and the output dataframe after the SQL query is applied. """]
supportive_info3 = [""" Explain the SQL query in detail without any example output."""]

# Use the model to generate content based on the supportive information and query input provided
response=model.generate_content([supportive_info1[0], query_input])
response2=model.generate_content([supportive_info2[0], response.text])
response3=model.generate_content([supportive_info3[0], response.text])

# if submit is clicked
if submit:
    #creating the columns side by side 
    # col1, col2, col3 = st.columns((0.7,1.0,1.0)) # with wide layout ,
    with st.spinner("Gerando Query.."):

        st.write("##### 1. O código de consulta SQL gerado:")
        response=model.generate_content([supportive_info1[0], query_input])
        st.code(response.text)

        st.write("##### 2. Uma amostra da saída esperada:")
        response2=model.generate_content([supportive_info2[0], response.text])
        st.write(response2.text)

        st.write("##### 3. Explicação do código de consulta SQL gerado:")
        response3=model.generate_content([supportive_info3[0], response.text])
        st.write(response3.text)