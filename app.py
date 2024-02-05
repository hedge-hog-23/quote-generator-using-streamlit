import streamlit as st
import requests

def get_random_quote():
    api_url = "https://api.quotable.io/random"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data["content"]     #content 
        author = quote_data["author"]       #author
        return f'*"{content}"*\n\n ~{author}'
    else:
        return "Unable to fetch a quote at the moment."

def main():
    st.title("Random Quote Generator")
    
    # Button to fetch and display a new random quote
    if st.button("Generate Random Quote"):
        quote = get_random_quote()
        st.write(quote)

if __name__ == "__main__":
    main()
