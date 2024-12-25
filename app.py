import streamlit as st
import openai
import pandas as pd

# Sidebar for API key
st.sidebar.header("OpenAI API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# Main page
st.title("NLP Application with OpenAI")

# User input
user_input = st.text_area("Enter text for NLP processing")

if st.button("Process"):
    if api_key and user_input:
        # Initialize the OpenAI client with the correct syntax
        client = openai.OpenAI(api_key=api_key)
        
        try:
            # Corrected OpenAI v1.x API Call
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            # Display result
            result = response.choices[0].message.content
            st.write("### Response")
            st.write(result)

            # Optional: Convert to DataFrame
            df = pd.DataFrame({"Input": [user_input], "Output": [result]})
            st.dataframe(df)

            # Download as CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "result.csv", "text/csv")

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.warning("Please enter API key and input text.")
