import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# 1. The Cockpit (Frontend UI)
st.title("🚀 AI Database Query Optimizer")
st.markdown("Analyze slow SQL queries, detect bottlenecks, and generate optimized indexing strategies.")

# Get OpenAI API Key from user
api_key = st.text_input("Enter your OpenAI API Key to power the AI:", type="password")

# Input for the slow SQL query
raw_sql = st.text_area("Paste your slow SQL query here:", height=150)

# 2. The Engine & Orchestrator (Backend Logic)
if st.button("Analyze & Optimize"):
    if not api_key:
        st.error("Please provide an OpenAI API Key.")
    elif not raw_sql:
        st.error("Please provide a SQL query to analyze.")
    else:
        with st.spinner("Analyzing hangar inventory routes (Scanning SQL)..."):
            
            # Connect to the AI Brain
            llm = ChatOpenAI(temperature=0.2, openai_api_key=api_key, model_name="gpt-4o")
            
            # The Prompt (Teaching the AI its job)
            prompt_template = """
            You are a Senior Database Administrator. Analyze the following SQL query for performance bottlenecks.
            
            Slow Query:
            {sql_query}
            
            Provide your response in exactly this format:
            1. Bottleneck Identified: (Explain why it is slow in one sentence)
            2. Recommended Index: (Write the exact SQL command to create the index)
            3. Optimized Query: (Rewrite the query if necessary)
            4. Performance Impact: (Predict the improvement)
            """
            
            prompt = PromptTemplate(input_variables=["sql_query"], template=prompt_template)
            
            # Run the AI
            chain = prompt | llm
            response = chain.invoke({"sql_query": raw_sql})
            
            # 3. The Output (Returning data to the Cockpit)
            st.success("Optimization Complete!")
            st.markdown(response.content)
