import streamlit as st
import os
import openai
import shutil

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

from rag.generator import generate_answer
from reports.generator import generate_report
from rag.index_manager import reset_index
from ingestion.processor import ingest_document

# -------------------------------
# App Config
# -------------------------------

st.set_page_config(
    page_title="AI Investment Analyst",
    layout="wide"
)

st.title("📊 AI Investment Analyst Dashboard")


# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.header("Upload Documents")

pdf_file = st.sidebar.file_uploader(
    "Upload Financial PDF",
    type=["pdf"]
)

csv_file = st.sidebar.file_uploader(
    "Upload Financial CSV",
    type=["csv"]
)

company_name = st.sidebar.text_input(
    "Company Name",
    placeholder="e.g. ACME Ltd"
)


# -------------------------------
# Helper Functions
# -------------------------------

DATA_DIR = "data"

def save_file(uploaded_file, folder):

    print("UPLOAD PIPELINE STARTED")

    # 🔥 Reset old vectors
    reset_index()

    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 🔥 Rebuild index
    ingest_document(file_path)

    print("UPLOAD PIPELINE COMPLETED")

    return file_path


def clear_data():

    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)

    os.makedirs(DATA_DIR)

    st.session_state.clear()   # 🔥 reset flags



# -------------------------------
# Upload Section
# -------------------------------

st.header("📂 Document Management")

if st.button("Clear Previous Files"):
    clear_data()
    st.success("Old files removed.")


if pdf_file and "pdf_processed" not in st.session_state:

    with st.spinner("Indexing document..."):

        pdf_path = save_file(pdf_file, f"{DATA_DIR}/pdfs")

    st.session_state["pdf_processed"] = True

    st.success(f"PDF uploaded and indexed: {pdf_file.name}")



if csv_file:
    csv_path = save_file(csv_file, f"{DATA_DIR}/csvs")
    st.success(f"CSV uploaded: {csv_file.name}")


# -------------------------------
# Q&A Section
# -------------------------------

st.header("💬 Ask Financial Questions")

query = st.text_input(
    "Enter your question",
    placeholder="What are the key risks?"
)

if st.button("Ask AI"):

    if not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing..."):
            answer = generate_answer(query)

        st.markdown("### 📌 Answer")
        st.write(answer)


# -------------------------------
# Report Section
# -------------------------------

st.header("📑 Generate Investment Memo")

# if st.button("Generate Report"):

#     if not company_name:
#         st.warning("Enter company name.")
#     else:

#         with st.spinner("Generating report..."):
#             generate_report(company_name)

#         output_file = f"reports/output/{company_name.replace(' ', '_')}_memo.docx"

#         if os.path.exists(output_file):

#             with open(output_file, "rb") as f:

#                 st.download_button(
#                     label="⬇️ Download Report",
#                     data=f,
#                     file_name=os.path.basename(output_file),
#                     mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                 )

#             st.success("Report ready!")

if st.button("Generate Report"):
    if not company_name:
        st.warning("Enter company name.")
    else:
        with st.spinner("Generating report..."):
            output_file = generate_report(company_name)  # Returns temp file path

        with open(output_file, "rb") as f:
            st.download_button(
                label="⬇️ Download Report",
                data=f,
                file_name=f"{company_name.replace(' ','_')}_memo.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        st.success("Report ready!")

# -------------------------------
# Footer
# -------------------------------

st.markdown("---")
st.caption("AI Investment Analyst • RAG Powered by OpenAI • Built with Streamlit")
