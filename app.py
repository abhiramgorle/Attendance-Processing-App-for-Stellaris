import streamlit as st
import csv
from io import StringIO

def process_csv(input_content, output_filename):
    fields = ["Attendance Date", "Name", "Email", "Mobile", "Session-1", "Session-2"]
    rows = []
    rowss = []

    # Use StringIO to create a file-like object from the uploaded content
    with StringIO(input_content.decode('utf-8')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

    i = 0
    k = []
    for row in rows:
        if i % 2 != 0:
            for j in range(len(row)):
                if j == 1:
                    continue
                else:
                    k.append(row[j])
        else:
            k.append(row[-1])
            rowss.append(k)
            k = []
        i += 1

    rowss.pop(0)

    with open(output_filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rowss)

    return rowss

# Streamlit UI
st.title("Attendance Processing App for Suryam Sir")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    st.text("File Uploaded Successfully!")

    # Processing the file and getting the result
    result_rows = process_csv(uploaded_file.read(), "result.csv")

    # Display the result
    st.write("Processed Data:")
    st.write(result_rows)

    # Download button for the result CSV
    csv_string = StringIO()
    csv_writer = csv.writer(csv_string)
    csv_writer.writerows(result_rows)
    
    st.download_button(
        label="Download Processed CSV",
        data=csv_string.getvalue(),
        file_name="result.csv",
        key="download_button"
    )
