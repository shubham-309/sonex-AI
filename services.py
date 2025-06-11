from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from time import sleep
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

log_file_path = "./logs/processed_files.log"

# Check if the log file exists, if not create it
if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as log_file:
        pass  # Just create an empty log file

def process_audio_file(audio_file_path, output_dir, gpt_model, only_transcripts=False):
    # Read the log file to check if the audio file has been processed
    with open(log_file_path, "r") as log_file:
        processed_files = log_file.readlines()

    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]

    if base_name in [line.split('|')[0].strip() for line in processed_files]:
        print(f"The file '{base_name}' has already been processed.")
    else:
        audio_file= open(audio_file_path, "rb")

        transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )

        print("Transcriptions generated successfully")
        # print(transcription.text)

        text_transcribe = transcription.text

        if only_transcripts:
            output_file_path = os.path.join(output_dir, f"{base_name}_transcription.txt")
            with open(output_file_path, "w") as f:
                f.write(f"{base_name}\n\n{text_transcribe}")
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            with open(log_file_path, "a") as log_file:
                log_file.write(f"{base_name} | {timestamp}\n")
        
        else:
            prompt = """You are analyzing a transcript of a multi-party conversation. Your task is to perform the following actions based on the transcripts provided :

                        1. Speaker Differentiation: Retrieve the full step by step conversation between them, Identify and differentiate between multiple speakers. Label each participant clearly (e.g., name mentioned in the transcript or you can use Speaker A, Speaker B).

                        2. Contextual Understanding: Understand and provide full detailed summary of the flow of dialogue, identifying key topics, intentions, and the emotional tone throughout the transcripts. Identify the primary purpose of the conversation and any significant shifts in context.

                        3. Summarization: Generate a detailed summary of the transcripts. Also highlight the most important points, decisions, or actions agreed upon by the speakers.

                        4. Sentiment Analysis: Analyze the sentiment of the transcripts in detail. Identify when positive, negative, or neutral tones are expressed, and specify which parts or statements reflect these sentiments.

                        5. Keyword and Topic Extraction: Extract the important keywords or phrases that represent the main topics discussed in the transcripts. Categorize them according to their relevance or frequency.

                        6. Actionable Insights: Based on the transcripts content, identify potential next steps, actions, or recommendations. Focus on actionable items that would help achieve the goals mentioned in the discussion.

                        7. Compliance Monitoring: Review the transcripts to check if there are any regulatory or protocol breaches, especially regarding language used or obligations mentioned.

                        8. Customizable Analytics: Tailor your analysis to focus on specific aspects of the call like customer complaints, technical issues, or business opportunities. Provide a deep dive into areas that align with the business needs.

                        Output your findings in an structured (i.e numbered list) and detailed manner with clear headings for each task.

                        Transcripts :- {transcribed_text}

                        Note :
                        1. Identify the language of the transcripts, Ensure the results i.e headings and its corrosponsing text should always be in the same language as of the transcripts.
                        2. Provide a very detailed summary.
                        3. The response should be in text form without any commentary.
                        4. Keep an eye on the details like any number like, car number, insurance number etc provided in the transcripts.
                        5. If someone's name is mentioned in the provided transcript, then denote them by their name.
                    """

            template = PromptTemplate(template=prompt, input_variables=["transcribed_text"])

            model = ChatOpenAI(temperature=0.3, model=gpt_model)

            chain = template | model

            results = chain.invoke(input={"transcribed_text": text_transcribe})

            sleep(0.6)

            base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
            output_file_path = os.path.join(output_dir, f"{base_name}.txt")
            final_results = results.content

            final_output = f"{base_name}\n\n{text_transcribe}\n\n{final_results}"

            sleep(0.6)

            # Write the results to a txt file
            with open(output_file_path, "w") as f:
                f.write(final_output)

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            with open(log_file_path, "a") as log_file:
                log_file.write(f"{base_name} | {timestamp}\n")


def process_all_audio_files(directory, output_dir, gpt_model, only_transcripts=False):
    for file_name in os.listdir(directory):
        if file_name.endswith(".mp3") or file_name.endswith(".wav") or file_name.endswith(".m4a"):  # Modify for your file formats
            audio_file_path = os.path.join(directory, file_name)
            process_audio_file(audio_file_path, output_dir, gpt_model, only_transcripts)

# Directory containing audio files
audio_directory = "./audio"  # Replace with your directory path

# Directory where output will be stored
output_directory = "./transcripts"  # Replace with your desired output directory

# GPT model to use
gpt_model = "gpt-4o"

# Call the function to process all audio files in the directory
process_all_audio_files(audio_directory, output_directory, gpt_model, only_transcripts=False)
