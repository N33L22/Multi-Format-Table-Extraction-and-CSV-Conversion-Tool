# Multi-Format-Table-Extraction-and-CSV-Conversion-Tool

# Abstract
This project delivers a comprehensive solution for extracting and processing data from a wide range of sources, including PDFs, web links, and files like Word and XML. This system ensures that the gathered data is accurate, well-structured, and ethically sourced by organizing it into Excel or CSV formats. The project emphasizes the importance of proper attribution to avoid plagiarism and maintains data integrity throughout the extraction process.

Following extraction, the data undergoes rigorous preprocessing steps designed to clean, transform, and optimize it for further analysis. This preprocessing enhances the data's quality, making it more suitable for advanced tasks such as visualization and predictive modeling. By improving the data's usability, the project enables more accurate and meaningful insights to be drawn, supporting informed decision-making. Additionally, the project provides a framework that adheres to ethical data practices, ensuring that all data used in visualization and prediction is both reliable and responsibly managed.

# System Flow and Architechture(Working)
![image](https://github.com/user-attachments/assets/10f8631f-d91a-45ee-ad0b-6465db12e009)

Step 1: Define Functions for Extraction and Conversion
1. Extract File Content Function: 
   - Create a function to extract content from different file types (PDF, DOCX, XML, HTML).
   - Use appropriate libraries such as PyPDF2 for PDF, python-docx for DOCX, BeautifulSoup for HTML, lxml for XML parsing.
   - For web pages, utilize requests to fetch the content.
2. Convert to DataFrame Function: 
   - Develop a function to convert the extracted content into a DataFrame.
   - Implement converters for each file type to transform the content into tabular data.


 Step 2: Implement Functions
1. Extract File Content Function: 
   - Write code to handle each file type separately.
   - Extract text content from PDF, DOCX, XML, HTML files.
   - Fetch and extract text content from web pages.
2. Convert to DataFrame Function: 
   - Based on the extracted content, convert it into a DataFrame format.
   - Use pandas DataFrame constructor or other suitable methods to create DataFrames.

![image](https://github.com/user-attachments/assets/d7085d3f-9a3d-4b80-9600-fe0a1c9ecfcf)

# Output 
## Homepage
<img width="1278" alt="Screenshot 2024-09-03 235257" src="https://github.com/user-attachments/assets/89b09939-e8d8-4ed0-8199-3471d6ceee4e">

## Converting table from a webpage to Excel
<img width="1113" alt="Screenshot 2024-09-04 000001" src="https://github.com/user-attachments/assets/6aa004bf-4eb9-4f0a-ba7b-b206dd5bb65f">
