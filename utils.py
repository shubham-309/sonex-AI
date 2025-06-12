from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
import os
import json
from time import sleep
import faster_whisper
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

client = OpenAI()
json_output_dir = "./analytics"
log_file_path = "./logs/processed_files.log"

# Check if the log file exists, if not create it
if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as log_file:
        pass  # Just create an empty log file

def transcribe_with_faster_whisper(audio_file, model_path="ivrit-ai/whisper-large-v3"):
    """
    Transcribe an audio file using the transformers pipeline with ivrit-ai/whisper-large-v3.
    
    Args:
        audio_file: File object or path to the audio file.
        model_path: Model identifier (default: "ivrit-ai/whisper-large-v3").
    
    Returns:
        str: The transcribed text.
    """
    try:
        # Initialize the ASR pipeline
        pipe = pipeline("automatic-speech-recognition", model=model_path)
        
        # Transcribe the audio (assuming audio_file is a file object from open())
        transcription = pipe(audio_file.name, generate_kwargs={"language": "he"}, return_timestamps=True)  # Use .name for file object
        
        st.toast("Transcription generated successfully with Transformers!")
        print("Transcription generated successfully with Transformers!", transcription)
        return transcription["text"]
    except Exception as e:
        st.error(f"Error in transcription: {e}")
        return ""

def transcribe_with_whisper(audio_file):
    
    # Load the original Whisper model
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        language='he'
        )
    
    # Transcribe the audio file
    result = transcription.text
    
    return result

def speaker_differentiation(transcription, llm_model):
    prompt = f"""משימה: זיהוי דוברים ופירוק שיחה

                הינך מקבל תמלול של שיחה קולית. מטרתך היא לזהות ולהבדיל בין כל הדוברים בטקסט, ולתייג בבירור כל משתתף.

                תמלול: {transcription}

                דרישות:

                זיהוי דוברים:

                חפש רמזים כמו שמות המוזכרים בתמלול, אינדיקטורים לדיבור ישיר, או תבניות דיבור ייחודיות. הענק לכל דובר תווית ייחודית (למשל, דובר 1, דובר 2, או שמות ספציפיים אם מוזכרים). מבנה הדיאלוג:

                ארגן את השיחה על ידי פירוקה לחלקים בהתאם לתורו של כל דובר. ציין בבירור כאשר יש שינוי דובר. תיוג:

                אם שם של דובר מוזכר, השתמש בשם זה כדי לתייג את הדיאלוג שלו. אם לא מוזכרים שמות, תייג אותם כדובר 1, דובר 2 וכו', באופן עקבי לאורך כל השיחה. הערות חשובות: עקביות: ודא כי אותו דובר מסומן באותו מזהה באופן עקבי לאורך כל התמלול. ייצוג מדויק: שיקף כל שינוי בטון, הפסקות או רגשות אם מצוינים בטקסט (למשל, צחוק, היסוס, הפרעות). תגובתך צריכה להיות בשפת התמלול, ללא הערות נוספות.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    st.toast("Speaker Differentiation Done")

    return results.content

def summary(transcription, llm_model):
    prompt = f"""משימה: סיכום מפורט של תמלול

                אתה מקבל תמלול של שיחת אודיו. מטרתך היא ליצור סיכום מפורט של התוכן, תוך הדגשת הנקודות העיקריות.

                תמלול: {transcription}

                דרישות:

                סיכום התוכן:

                ספק סיכום תמציתי אך מקיף של השיחה כולה. תפוס את הרעיונות והנושאים המרכזיים שנידונו, וסכם את תרומתו של כל דובר.

                הדגשת נקודות מפתח:

                ציין את הנקודות החשובות ביותר שהועלו במהלך השיחה. התמקד בהחלטות, הסכמות או מסקנות שאליהן הגיעו הדוברים.

                פעולות והחלטות:

                ציין את כל הפעולות או הצעדים שהמשתתפים הסכימו עליהם. ציין החלטות חשובות שהתקבלו, כולל ההקשר בו התקבלו.

                הערה מיוחדת:

                תגובתך צריכה להיות באותה השפה של התמלול.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    st.toast("Successfully created summary from the transcripts")

    return results.content

def sentiment_analysis(transcription, llm_model):
    prompt = f"""משימה: ניתוח מעמיק של רגשות בתמלול

                אתה מקבל תמלול של שיחת אודיו. עליך לנתח את הרגשות שמביע כל דובר לאורך הדיאלוג.

                תמלול: {transcription}

                דרישות:

                זיהוי רגשות:

                נתח את הטון והאווירה המובעים על ידי כל דובר בחלקים שונים של השיחה (לדוגמה, חיובי, שלילי או ניטרלי).

                הדגשת שינויים ברגש:

                ציין היכן מתרחשים שינויים משמעותיים בטון. ספק הסברים לשינויים ברגש (כגון תסכול, אופטימיות, התלהבות).

                מיפוי רגשות:

                ציין אילו אמירות או קטעים משקפים את הרגש המסוים. אם אפשר, סווג את הרגש כקל, חזק או ניטרלי בהתאם לעוצמה.

                הערה מיוחדת:

                תגובתך צריכה להיות באותה השפה של התמלול.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    st.toast("Sentiment Analysis Done")

    return results.content

def keyword_topic(transcription, llm_model):
    prompt = f"""משימה: חילוץ מילות מפתח, נושאים עיקריים ופרטים מספריים מהתמלול

                אתה מקבל תמלול של שיחת אודיו. מטרתך היא לחלץ מילות מפתח, ביטויים ופרטים מספריים חשובים המייצגים את הנושאים המרכזיים שנידונו.

                תמלול: {transcription}

                דרישות:

                זיהוי מילות מפתח וביטויים:

                חלץ מילות מפתח או מונחים שמוזכרים לעיתים קרובות או רלוונטיים לנושא השיחה.

                חילוץ פרטים מספריים:

                שימו לב במיוחד לכל מספר שמוזכר בתמלול, כגון:

                מספרי רכב
                מספרי ביטוח
                מספרי טלפון
                מספרי זיהוי סמן את הפרטים המספריים הללו כמילות מפתח חשובות וקטלג אותם בנפרד לצורך בהירות.
                קטלוג נושאים:

                קבץ את מילות המפתח והפרטים המספריים שהוצאו לפי קטגוריות רלוונטיות (לדוגמה, מידע אישי, מועדי פרויקטים, מידע על ביטוח). ציין את תדירות או חשיבות מילות המפתח.

                רלוונטיות והקשר:

                הדגש את הנושאים הקריטיים או החוזרים על עצמם שנידונו. וודא שכל מידע אישי או רגיש (כמו מספרי רכב או ביטוח) מסומן בבירור.

                הערה מיוחדת:

                תגובתך צריכה להיות באותה השפה של התמלול.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    st.toast("Keyword and Topic extraction Done")

    return results.content

def actionable_insights(transcription, llm_model):
    prompt = f"""משימה: תובנות ניתנות לפעולה מתוך תמלול

                אתה מקבל תמלול של שיחת אודיו. מטרתך היא לזהות פריטים ניתנים לפעולה ולספק המלצות על סמך התוכן.

                תמלול: {transcription}

                דרישות:

                זיהוי פריטים ניתנים לפעולה:

                הדגש פעולות מפתח שנדונו או הוסכמו על ידי המשתתפים. זהה כל צעדים הבאים או משימות ספציפיות שהוזכרו במהלך השיחה.

                ספק המלצות:

                הצע פעולות נוספות על סמך הדיון. הצע תובנות או המלצות שעשויות לסייע בהשגת המטרות שנזכרו בשיחה.

                הערה מיוחדת:

                תגובתך צריכה להיות באותה השפה של התמלול.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    return results.content

def compliance_monitoring(transcription, llm_model):
    prompt = f"""משימה: ניטור עמידה בתקנות מתוך תמלול

                אתה מקבל תמלול של שיחת אודיו. מטרתך היא לבחון את השיחה לאיתור הפרות של תקנות או נהלים.

                תמלול: {transcription}

                דרישות:

                בדיקה להפרות רגולטוריות:

                סקור את השפה שבה נעשה שימוש לאיתור הצהרות בלתי הולמות או שאינן עומדות בתקנות.

                עמידה בנהלים:

                וודא שהשיחה מתנהלת בהתאם לנהלים או להנחיות שנקבעו (לדוגמה, שמירה על סודיות, שפה מכבדת).

                הדגשת חששות:

                זהה ודווח על כל הפרה או הצהרה מעוררת שאלות הדורשת פעולה נוספת.

                הערה מיוחדת:

                תגובתך צריכה להיות באותה השפה של התמלול.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    return results.content

def custom_analytics(transcription, llm_model):
    prompt = f"""משימה: ניתוח מותאם אישית להיבטים ספציפיים בשיחה

                אתה מקבל תמלול של שיחת אודיו. התאם את הניתוח שלך כדי להתמקד בהיבטים ספציפיים של השיחה, כגון תלונות לקוחות, בעיות טכניות או הזדמנויות עסקיות.

                תמלול: {transcription}

                דרישות:

                תחום ההתמקדות:

                התאם את הניתוח להדגשת תחומי עניין עסקיים מסוימים (לדוגמה, תלונות לקוחות, בעיות טכניות, הזדמנויות מכירה).

                ניתוח מעמיק:

                ספק ניתוח מעמיק של התחומים שצוינו, תוך חילוץ פרטים או חששות רלוונטיים.

                תובנות ניתנות לפעולה:

                בהתאם לניתוח, הצע פעולות או אסטרטגיות שיסייעו לטפל בבעיות או לנצל הזדמנויות.

                הערה מיוחדת:

                תגובתך צריכה להיות באותה השפה של התמלול.
            """

    template = PromptTemplate(template=prompt, input_variables=["transcription"])

    if llm_model == "gpt-4" or llm_model == "gpt-4o":
                model = ChatOpenAI(temperature=0.3, model=llm_model)
    elif llm_model == "Claude":
        model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0.3)
    elif llm_model == "Groq":
        model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.3)
    else:
        st.error("Invalid model specified. Please choose a valid model.")
        return

    chain = template | model

    results = chain.invoke(input={"transcription": transcription})

    return results.content


def process_audio_file(transcript_model, audio_file_path, output_dir, llm_model, only_transcripts=False):
    # Read the log file to check if the audio file has been processed
    with open(log_file_path, "r") as log_file:
        processed_files = log_file.readlines()
    st.toast("Succesfully loaded audio")

    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]

    if base_name in [line.split('|')[0].strip() for line in processed_files]:
        st.error(f"The file '{base_name}' has already been processed.")
        return None
    else:
        audio_file= open(audio_file_path, "rb")

        if transcript_model == 'Whisper':
            transcription = transcribe_with_whisper(audio_file=audio_file)
            st.toast("Transcriptions generated succesfully")
            text_transcribe = transcription
        else:
            transcription= transcribe_with_faster_whisper(audio_file=audio_file)
            st.toast("Transcriptions generated succesfully")
            text_transcribe = transcription

        if only_transcripts:
            output_file_path = os.path.join(output_dir, f"{base_name}_transcription.txt")
            speakers = speaker_differentiation(text_transcribe, llm_model)
            # Ensure the output file is opened with UTF-8 encoding
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(f"{base_name}\n\n{text_transcribe}\n\n{speakers}")

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            with open(log_file_path, "a") as log_file:
                    log_file.write(f"{base_name} | {timestamp}\n")

            st.success('Transcription saved successfully!', icon="✅")
            return f"{base_name}\n\n{text_transcribe}\n\n{speakers}"
        
        else:
            st.toast("Please wait analysing transcription")
            sleep(0.6)

            speakers = speaker_differentiation(text_transcribe, llm_model)
            detailed_summary = summary(text_transcribe, llm_model)
            sentiment = sentiment_analysis(text_transcribe, llm_model)
            keyword = keyword_topic(text_transcribe, llm_model)
            insights = actionable_insights(text_transcribe, llm_model)
            compliance = compliance_monitoring(text_transcribe, llm_model)
            analytics = custom_analytics(text_transcribe, llm_model)

            # Prepare the JSON output
            output_data = {
                "Transcripts": transcription,
                "Speakers": speakers,
                "Detailed_Summary": detailed_summary,
                "Sentiment": sentiment,
                "Keyword": keyword,
                "Insights": insights,
                "Compliance": compliance,
                "Analytics": analytics
            }

            json_file_path = os.path.join(json_output_dir, f"{base_name}.json")

            # Write the JSON data to a file
            with open(json_file_path, "w", encoding="utf-8") as json_file:
                json.dump(output_data, json_file, indent=4, ensure_ascii=False)

            base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
            output_file_path = os.path.join(output_dir, f"{base_name}.txt")

            final_output = f"{base_name}\n\n{text_transcribe}\n\n{speakers}\n\n{detailed_summary}\n\n{sentiment}\n\n{keyword}\n\n{insights}\n\n{compliance}\n\n{analytics}\n\n"

            st.toast("Hooray! Here is your results")
            sleep(0.6)

            # Write the results to a text file
            with open(output_file_path, "w") as f:
                f.write(final_output)

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            with open(log_file_path, "a") as log_file:
                    log_file.write(f"{base_name} | {timestamp}\n")

            st.success('Successfully saved your Audio data!', icon="✅")
            return final_output
