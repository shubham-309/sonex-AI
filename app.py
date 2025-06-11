import streamlit as st
import os
import tempfile
from utils import process_audio_file  # Ensure this function is correctly defined in utils

# Set up page configuration
st.set_page_config("Advance Services", page_icon="logo/image.png", layout="wide")
col1, col2 = st.columns([1, 8])

with col1:
    st.image("logo/image.png", width=80)

with col2:
    st.title("SonexAI 🚀🔊")
    st.subheader("Harness the Power of AI to Deliver Intelligent, Audio-Based Insights. 💡✨")

# Model selection
model = st.selectbox(
    "Choose AI Model",
    options=["gpt-4o", "gpt-4", "Claude", "Groq"],
    index=0  # Default to GPT-4o
)

transcript_model = st.selectbox(
    "Choose Transcription Model",
    options=["ivrit", "Whisper"],
    index=1  # Default to Whisper
)

supported_formats = ["wav", "mp3", "ogg", "flac", "aac", "aiff", "alac", "dsd", "wma", "m4a", "mp4", "avi", "3gpp"]

# Option to upload a single audio file or specify a directory
option = st.radio("Choose input type", ["Upload Single Audio", "Load Audio Directory"])

if option == "Upload Single Audio":
    audio_file = st.file_uploader("Upload an audio file", type=supported_formats)
elif option == "Load Audio Directory":
    audio_dir = st.text_input("Enter the path to the directory containing audio files")
    audio_file = None

output_dir_path = "transcripts"
output_dir = st.text_input("Enter the output directory path for saving transcriptions", value=output_dir_path)
only_transcripts = st.checkbox("Get only transcription (with Speaker Diarization)", value=False)

# Process the audio file or directory on button click
if st.button("Process"):
    if option == "Upload Single Audio" and audio_file:
        # Save the uploaded file temporarily
        temp_dir = tempfile.gettempdir()
        audio_file_path = os.path.join(temp_dir, audio_file.name)
        with open(audio_file_path, "wb") as f:
            f.write(audio_file.read())
        
        # Show a progress bar and spinner while processing
        with st.spinner("Processing audio..."):
            process_audio_file(transcript_model, audio_file_path, output_dir, model, only_transcripts)

    elif option == "Load Audio Directory" and audio_dir:
        if os.path.isdir(audio_dir):
            audio_files = [f for f in os.listdir(audio_dir) if f.split('.')[-1].lower() in supported_formats]
            total_files = len(audio_files)
            
            if total_files > 0:
                for index, file_name in enumerate(audio_files):
                    audio_file_path = os.path.join(audio_dir, file_name)
                    process_audio_file(transcript_model, audio_file_path, output_dir, model, only_transcripts)
                    
            else:
                st.error("No supported audio files found in the specified directory.")
        else:
            st.error("Directory not found. Please provide a valid directory path.")
    else:
        st.error("Please upload a file or provide a directory.")
