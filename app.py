import streamlit as st
import csv
from io import StringIO

def process_csv(input_content, output_filename,session_number):
    
    rows = []
    rowss = []

    # Use StringIO to create a file-like object from the uploaded content
    with StringIO(input_content.decode('utf-8')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    x = session_number
    i = 0
    k = []
    l = []
    for row in rows:
        if i % x != 0:
            k.append(row[-1])
        else:
            k.append(row[-1])
            l = row
            l.pop(1)
            l.pop(-1)
            l[-1:-1] = k
            j = l[-1]
            l.pop(-1)
            l.insert(3,j)
            rowss.append(l)
            k = []
        i += 1

    rowss.pop(0)

    with open(output_filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(fields)
        csvwriter.writerows(rowss)

    return rowss

# Streamlit UI
st.title("Attendance Processing App for Suryam Sir")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Dropdown for number selection
session_number = st.number_input("Enter number of sessions", min_value=1, max_value=10)



if st.button("Process"):
    st.text("File Uploaded Successfully!")

    # Processing the file and getting the result
    result_rows = process_csv(uploaded_file.read(), "result.csv", session_number)
    fields = ["Attendance Date", "Name", "Email", "Mobile"]
    # sessions = []
    for i in range(1, session_number+1):
        session_name = f"Session-{i}"
        fields.append(session_name)
    # Display the result
    # st.write("Processed Data:")
    # st.write(result_rows)

    # Download button for the result CSV
    csv_string = StringIO()
    csv_writer = csv.writer(csv_string)
    csv_writer.writerow(fields)
    csv_writer.writerows(result_rows)

    st.download_button(
        label="Download Processed CSV",
        data=csv_string.getvalue(),
        file_name="result.csv",
        key="download_button"
    )

