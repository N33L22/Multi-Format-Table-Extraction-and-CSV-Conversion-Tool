import streamlit as st
import pandas as pd
import base64
import time
from requests.exceptions import RequestException
from PyPDF2 import PdfReader

# Importing functions from converter files
from pdf_converter import convert_pdf_to_dataframe
from word_converter import convert_word_to_dataframe
from xml_converter import convert_xml_to_dataframe
from html_converter import convert_html_to_dataframe
from web_converter import convert_web_to_dataframe  # Update the import statement

# Function to convert file to DataFrame based on file type
def convert_file_to_dataframe(file, file_type):
    if file_type == "pdf":
        return convert_pdf_to_dataframe(file)
    elif file_type == "docx":
        return convert_word_to_dataframe(file)
    elif file_type == "xml":
        return convert_xml_to_dataframe(file)
    elif file_type == "html":
        return convert_html_to_dataframe(file)
    else:
        st.error("Unsupported file type.")
        return None

# Function to get the number of pages in a PDF file
def get_num_pages(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    return num_pages

# Main function
def main():
    st.title("Table Data Converter")

    # Upload file
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "xml", "html"])
    if uploaded_file:
        progress_bar = st.progress(0)
        progress_status = st.empty()
        
        # Display progress bar while uploading
        for percent_complete in range(100):
            progress_bar.progress(percent_complete + 1)
            progress_status.text(f"Uploading... {percent_complete + 1}%")
            time.sleep(0.1)

        # Convert uploaded file to DataFrame
        file_name = uploaded_file.name.lower()  # Convert file name to lowercase
        file_type = file_name.split(".")[-1]  # Extract file extension
        if file_type == "pdf":
            num_pages = get_num_pages(uploaded_file)  # Get the number of pages for PDF files
            st.info(f"Number of pages in PDF file: {num_pages}")
        dfs = convert_file_to_dataframe(uploaded_file, file_type)

        # Display the DataFrames if not empty
        if dfs is not None:
            selected_tables = st.multiselect("Select tables to download:", range(1, len(dfs) + 1), default=range(1, len(dfs) + 1))

            for i, df in enumerate(dfs):
                # Check if the user selected this table for download
                if i + 1 in selected_tables:
                    if isinstance(df, pd.DataFrame) and not df.empty:
                        # Display the DataFrame content
                        st.write(f"Converted DataFrame from table {i + 1}:")
                        st.write(df)

                        # Download button for the converted Excel file
                        if st.button(f"Download Excel Table {i + 1}"):
                            csv_data = df.to_csv(index=False)
                            b64 = base64.b64encode(csv_data.encode()).decode()
                            href = f'<a href="data:file/csv;base64,{b64}" download="converted_table_{i + 1}.csv">Download Excel Table {i + 1}</a>'
                            st.markdown(href, unsafe_allow_html=True)
                    elif isinstance(df, str):
                        st.warning(f"Table {i + 1} is empty.")
 
    st.title("Web Page to DataFrame")
    web_url = st.text_input("Enter the URL of the web page:")
    if st.button("Convert"):
        if web_url:
            st.write("Converting web page to DataFrame...")
            dfs_with_links = convert_web_to_dataframe(web_url)
            if dfs_with_links:
                for i, (df, download_link) in enumerate(dfs_with_links):
                    st.write(f"Table {i + 1}:")
                    st.write(df)
                    st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()