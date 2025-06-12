import streamlit as st
import os
import tempfile
from utils import process_audio_file  # Ensure this function is correctly defined in utils
from fpdf import FPDF
import arabic_reshaper
from bidi.algorithm import get_display
import io

class HebrewPDF(FPDF):
    def __init__(self):
        super().__init__()
        # Try different font paths that might be available
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
            '/usr/share/fonts/TTF/DejaVuSans.ttf',  # Alternative Linux path
            'DejaVuSans.ttf'  # Local directory
        ]
        
        font_found = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    self.add_font('DejaVu', '', font_path, uni=True)
                    font_found = True
                    break
                except:
                    continue
        
        if not font_found:
            try:
                # If DejaVu is not found, download it to the local directory
                import urllib.request
                font_url = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf"
                if not os.path.exists('DejaVuSans.ttf'):
                    urllib.request.urlretrieve(font_url, 'DejaVuSans.ttf')
                self.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
            except:
                # Last resort: use a built-in font
                st.warning("Could not load DejaVu font. PDF might not display Hebrew text correctly.")
                self.add_font('Arial', '', 'Arial', uni=True)
    
    def hebrew_cell(self, w, h, txt, border=0, align='R'):
        try:
            # Reshape and convert to bidi
            reshaped_text = arabic_reshaper.reshape(txt)
            bidi_text = get_display(reshaped_text)
            self.cell(w, h, bidi_text, border, align=align)
        except:
            # Fallback if reshaping fails
            self.cell(w, h, txt, border, align=align)
    
    def hebrew_multi_cell(self, w, h, txt, border=0, align='R'):
        try:
            # Process text line by line
            lines = txt.split('\n')
            for line in lines:
                if line.strip():  # Only process non-empty lines
                    reshaped_text = arabic_reshaper.reshape(line)
                    bidi_text = get_display(reshaped_text)
                    self.multi_cell(w, h, bidi_text, border, align=align)
                else:
                    self.ln()  # Add empty line
        except:
            # Fallback if reshaping fails
            self.multi_cell(w, h, txt, border, align=align)

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
            results = process_audio_file(transcript_model, audio_file_path, output_dir, model, only_transcripts)
            
            if results:
                st.write("### Generated Results")
                st.write(results)
                
                # Create PDF with Hebrew support
                pdf = HebrewPDF()
                pdf.add_page()
                pdf.set_font('DejaVu', '', 14)
                pdf.set_right_margin(10)
                pdf.set_left_margin(10)
                
                # Write content to PDF
                pdf.hebrew_multi_cell(0, 10, results)
                
                # Save PDF to a temporary file first
                temp_pdf_path = os.path.join(temp_dir, "temp.pdf")
                pdf.output(temp_pdf_path, 'F')
                
                # Read the temporary PDF file into memory
                with open(temp_pdf_path, 'rb') as pdf_file:
                    pdf_data = pdf_file.read()
                
                # Clean up the temporary file
                os.remove(temp_pdf_path)
                
                # Add download button
                base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
                st.download_button(
                    label="Download Results as PDF",
                    data=pdf_data,
                    file_name=f"{base_name}_results.pdf",
                    mime="application/pdf"
                )

    elif option == "Load Audio Directory" and audio_dir:
        if os.path.isdir(audio_dir):
            audio_files = [f for f in os.listdir(audio_dir) if f.split('.')[-1].lower() in supported_formats]
            total_files = len(audio_files)
            
            if total_files > 0:
                for index, file_name in enumerate(audio_files):
                    audio_file_path = os.path.join(audio_dir, file_name)
                    results = process_audio_file(transcript_model, audio_file_path, output_dir, model, only_transcripts)
                    
                    if results:
                        st.write(f"### Results for {file_name}")
                        st.write(results)
                        
                        # Create PDF with Hebrew support
                        pdf = HebrewPDF()
                        pdf.add_page()
                        pdf.set_font('DejaVu', '', 14)
                        pdf.set_right_margin(10)
                        pdf.set_left_margin(10)
                        
                        # Write content to PDF
                        pdf.hebrew_multi_cell(0, 10, results)
                        
                        # Save PDF to a temporary file first
                        temp_dir = tempfile.gettempdir()
                        temp_pdf_path = os.path.join(temp_dir, f"temp_{index}.pdf")
                        pdf.output(temp_pdf_path, 'F')
                        
                        # Read the temporary PDF file into memory
                        with open(temp_pdf_path, 'rb') as pdf_file:
                            pdf_data = pdf_file.read()
                        
                        # Clean up the temporary file
                        os.remove(temp_pdf_path)
                        
                        # Add download button
                        base_name = os.path.splitext(file_name)[0]
                        st.download_button(
                            label=f"Download Results for {file_name} as PDF",
                            data=pdf_data,
                            file_name=f"{base_name}_results.pdf",
                            mime="application/pdf"
                        )
                    
            else:
                st.error("No supported audio files found in the specified directory.")
        else:
            st.error("Directory not found. Please provide a valid directory path.")
    else:
        st.error("Please upload a file or provide a directory.")
