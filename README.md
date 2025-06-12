# SonexAI Tool 🚀🔊

SonexAI is an advanced audio processing and analysis tool that leverages AI to deliver intelligent, audio-based insights. The tool transcribes audio files and provides comprehensive analysis including speaker differentiation, sentiment analysis, and actionable insights.

## Features ✨

- **Multiple AI Model Support**
  - GPT-4
  - Claude
  - Groq
  - Custom model selection

- **Transcription Options**
  - Whisper ASR
  - Ivrit (for Hebrew content)
  - Speaker diarization

- **Comprehensive Analysis**
  - 📝 Detailed transcription
  - 👥 Speaker differentiation
  - 📊 Sentiment analysis
  - 🔑 Keyword and topic extraction
  - 💡 Actionable insights
  - ⚖️ Compliance monitoring
  - 📈 Custom analytics

- **File Handling**
  - Single audio file processing
  - Batch directory processing
  - Multiple audio format support (wav, mp3, ogg, flac, aac, aiff, alac, dsd, wma, m4a, mp4, avi, 3gpp)

- **Output Options**
  - Direct display in web interface
  - Downloadable PDF reports
  - Text file exports
  - JSON analytics output

## Installation 🛠️

1. Clone the repository:
```bash
git clone <repository-url>
cd SonexAI-Tool
```

2. Install system dependencies:
```bash
# For Ubuntu/Debian
sudo apt-get install fonts-dejavu-core
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Environment Setup 🌍

1. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GROQ_API_KEY=your_groq_api_key
```

2. Create necessary directories:
```bash
mkdir -p transcripts analytics logs
```

## Usage 🎯

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Access the web interface at `http://localhost:8501`

3. Choose your options:
   - Select AI model (GPT-4, Claude, or Groq)
   - Select transcription model (Whisper or Ivrit)
   - Choose input type (single file or directory)
   - Upload audio file(s) or specify directory path
   - Set output directory for transcripts
   - Toggle transcription-only mode if needed

4. Click "Process" to start analysis

5. View results and download PDF reports

## Directory Structure 📁

```
SonexAI-Tool/
├── app.py              # Main Streamlit application
├── utils.py            # Utility functions for audio processing
├── requirements.txt    # Python dependencies
├── packages.txt        # System dependencies
├── transcripts/        # Output directory for transcriptions
├── analytics/          # JSON analytics output
├── logs/              # Processing logs
└── .env               # Environment variables
```

## Deployment on Render 🚀

1. Create a new Web Service on Render
2. Connect your repository
3. Set environment variables in Render dashboard
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run app.py`

The `packages.txt` file will automatically install system dependencies on Render.

## Features in Detail 🔍

### Transcription
- Accurate speech-to-text conversion
- Support for multiple languages
- Speaker diarization for multi-speaker audio

### Analysis
1. **Speaker Differentiation**
   - Identifies different speakers
   - Labels speakers consistently
   - Maintains conversation flow

2. **Sentiment Analysis**
   - Detects emotional tone
   - Identifies positive/negative sentiments
   - Tracks sentiment changes

3. **Topic Extraction**
   - Identifies main discussion points
   - Extracts key phrases
   - Categorizes topics

4. **Actionable Insights**
   - Identifies next steps
   - Highlights decisions made
   - Suggests follow-up actions

5. **Compliance Monitoring**
   - Checks for regulatory adherence
   - Flags potential issues
   - Ensures protocol compliance

## Output Formats 📄

1. **PDF Reports**
   - Professional formatting
   - Right-to-left support for Hebrew
   - Complete analysis summary

2. **JSON Analytics**
   - Structured data format
   - Easy integration with other tools
   - Detailed analysis metrics

3. **Text Transcripts**
   - Clean, formatted text
   - Speaker labels
   - Time-stamped content

## Error Handling 🛡️

- Graceful handling of unsupported audio formats
- Duplicate file processing prevention
- Font fallback mechanisms for PDF generation
- Comprehensive error logging

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

[Add your license information here]

## Support 💬

For support, please [create an issue](repository-issues-url) or contact [your-contact-info].

---

Built with ❤️ using OpenAI, Anthropic, and Groq APIs 
