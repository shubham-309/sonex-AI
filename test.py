from googletrans import Translator

def translate_text_google_free(text: str, src: str = "he", dest: str = "en") -> str:
    """
    Translate text from Hebrew to English using the free googletrans library.

    :param text: The text to translate.
    :param src: Source language code (default is Hebrew "he").
    :param dest: Target language code (default is English "en").
    :return: The translated text.
    """
    try:
        # Initialize the translator
        translator = Translator()
        
        # Perform translation
        translation = translator.translate(text, src=src, dest=dest)
        
        # Return the translated text
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return ""

# Example usage
hebrew_text = """
Sip22_Outgoing_202306250911_39154339 4339_0543116183_GSM

מה נשמע שבתאי? בוקר טוב. בוקר רוב. התחברת ליתורן של חולחת האישור? לא, אני לא מבין איך את רוצה שאני אתן. זה אין לי שום קרצים של הרכב. אה, תגיד לי, אין בעיה. אני מצטער לך, מה את צריכה חוץ ממספר רכב? אני לא יודע, אני לא יודע מה אני צריכה צריך לתת להם, לתת להם את המספר רכב? כן. אוקיי, ואז מה להגיד? שאתה צריך להתחבל על מנוע ישראל, כן. שנתקעו את המערכת, אבל צריך להגיע להם בשביל זה, לא על מנת לעשות את זה? לא, לא, פתאום, זה טלפון, הנה, סיימפ, שולחים לך אישור במייל שהתחברת, עם המערכות שהתקינו לך ברכב, ואת המספר הזה אתה מרוויר אליי, זה הכל. תשכחי לי, תשכחי לי רק את המספר רכב. שלחתי לך בוואטסאפ, ותעביר אליי, בסדר? אני חייג אליהם עכשיו. יופי, תודה שבתאי. תודה רבה.

דובר 1: מה נשמע שבתאי?  
דובר 2 (שבתאי): בוקר טוב.  
דובר 1: בוקר רוב. התחברת ליתורן של חולחת האישור?  
דובר 2 (שבתאי): לא, אני לא מבין איך את רוצה שאני אתן. זה אין לי שום קרצים של הרכב.  
דובר 1: אה, תגיד לי, אין בעיה. אני מצטער לך, מה את צריכה חוץ ממספר רכב?  
דובר 2 (שבתאי): אני לא יודע, אני לא יודע מה אני צריכה צריך לתת להם, לתת להם את המספר רכב?  
דובר 1: כן.  
דובר 2 (שבתאי): אוקיי, ואז מה להגיד?  
דובר 1: שאתה צריך להתחבל על מנוע ישראל, כן. שנתקעו את המערכת, אבל צריך להגיע להם בשביל זה, לא על מנת לעשות את זה?  
דובר 2 (שבתאי): לא, לא, פתאום, זה טלפון, הנה, סיימפ, שולחים לך אישור במייל שהתחברת, עם המערכות שהתקינו לך ברכב, ואת המספר הזה אתה מרוויר אליי, זה הכל.  
דובר 1: תשכחי לי, תשכחי לי רק את המספר רכב.  
דובר 2 (שבתאי): שלחתי לך בוואטסאפ, ותעביר אליי, בסדר?  
דובר 1: אני חייג אליהם עכשיו.  
דובר 2 (שבתאי): יופי, תודה שבתאי.  
דובר 1: תודה רבה.

סיכום מפורט של תמלול השיחה:

**סיכום התוכן:**
השיחה מתנהלת בין שבתאי ורוב, כאשר רוב מנסה להבין את התהליך הנדרש להתחברות למערכת כלשהי ברכב. השיחה מתמקדת בהבהרת הצעדים שיש לנקוט כדי להשלים את התהליך.

**הדגשת נקודות מפתח:**
1. רוב לא מבין את התהליך הנדרש להתחברות למערכת ברכב.
2. שבתאי מסביר לרוב שעליו לספק את מספר הרכב.
3. יש צורך להתחבר למנוע ישראל כדי להפעיל את המערכת.
4. שבתאי מציין כי ישלחו אישור במייל על ההתחברות, ורוב צריך להעביר את המספר לשבתאי.

**פעולות והחלטות:**
- רוב צריך לספק את מספר הרכב לשבתאי.
- שבתאי יספק לרוב אישור במייל על ההתחברות למערכת.
- רוב צריך להעביר את המספר לשבתאי לאחר קבלת האישור.

**הערה מיוחדת:**
השיחה מתמקדת בעיקר בהבהרת תהליך טכני, כאשר שבתאי מדריך את רוב בצעדים הנדרשים.

ניתוח רגשות בתמלול:

1. **תחילת השיחה:**
   - **דובר 1 (רוב):** "מה נשמע שבתאי? בוקר טוב."
     - **רגש:** חיובי, נעים.
     - **עוצמה:** קלה.
     - **הסבר:** פתיחה ידידותית ומנומסת, מראה על רצון טוב ותקשורת חיובית.

   - **דובר 2 (שבתאי):** "בוקר רוב."
     - **רגש:** ניטרלי.
     - **עוצמה:** קלה.
     - **הסבר:** תגובה סטנדרטית וברורה, ללא הבעת רגש מיוחדת.

2. **חלק מרכזי של השיחה:**
   - **דובר 1 (רוב):** "התחברת ליתורן של חולחת האישור?"
     - **רגש:** ניטרלי.
     - **עוצמה:** קלה.
     - **הסבר:** שאלה ישירה, ללא הבעת רגש מיוחדת.

   - **דובר 2 (שבתאי):** "לא, אני לא מבין איך את רוצה שאני אתן. זה אין לי שום קרצים של הרכב."
     - **רגש:** תסכול.
     - **עוצמה:** בינונית.
     - **הסבר:** שבתאי מביע בלבול ותסכול מהמצב, חוסר הבנה של התהליך.

   - **דובר 1 (רוב):** "אה, תגיד לי, אין בעיה. אני מצטער לך, מה את צריכה חוץ ממספר רכב?"
     - **רגש:** אמפתיה ונכונות לעזור.
     - **עוצמה:** בינונית.
     - **הסבר:** רוב מנסה להרגיע ולהציע עזרה, מביע הבנה למצב של שבתאי.

3. **סיום השיחה:**
   - **דובר 1 (רוב):** "יופי, תודה שבתאי. תודה רבה."
     - **רגש:** חיובי, סיום נעים.
     - **עוצמה:** קלה.
     - **הסבר:** רוב מסיים את השיחה בטון חיובי ומודה לשבתאי, מראה על שביעות רצון מהפתרון.

   - **דובר 2 (שבתאי):** "אני חייג אליהם עכשיו."
     - **רגש:** החלטיות.
     - **עוצמה:** בינונית.
     - **הסבר:** שבתאי מביע נכונות לפעול ולסיים את העניין, מראה על קבלת המצב והתקדמות.

**שינויים ברגש:**
- השינוי המשמעותי ביותר מתרחש כאשר שבתאי מביע תסכול מהמצב, ולאחר מכן רוב מגיב באמפתיה ונכונות לעזור. השינוי הזה מראה על מעבר מתסכול להבנה ושיתוף פעולה.

**מיפוי רגשות:**
- התסכול של שבתאי מתבטא במשפט: "לא, אני לא מבין איך את רוצה שאני אתן."
- האמפתיה של רוב מתבטאת במשפט: "אה, תגיד לי, אין בעיה. אני מצטער לך, מה את צריכה חוץ ממספר רכב?"
- הסיום החיובי מתבטא במשפטים האחרונים של השיחה, כאשר שני הדוברים מביעים תודה והחלטיות להמשיך.

מילות מפתח וביטויים:
- התחברות
- אישור
- מספר רכב
- מנוע ישראל
- מערכת
- מייל
- וואטסאפ

פרטים מספריים:
- מספר רכב (לא צויין מספר ספציפי בתמלול)

קטלוג נושאים:
1. מידע אישי:
   - מספר רכב: נושא מרכזי בשיחה, יש צורך להעביר את המספר לצורך התחברות למערכת.
2. תהליך התחברות:
   - התחברות למערכת: יש צורך להתחבר למערכת מנוע ישראל ולקבל אישור במייל.
3. תקשורת:
   - שימוש בוואטסאפ להעברת מידע.

רלוונטיות והקשר:
- הנושא המרכזי של השיחה הוא תהליך התחברות למערכת מנוע ישראל באמצעות מספר רכב וקבלת אישור במייל.
- יש דגש על הצורך בהעברת מספר הרכב לצורך השלמת התהליך.
- התקשורת מתבצעת גם באמצעות וואטסאפ לצורך העברת מידע.

### פריטים ניתנים לפעולה:

1. **התחברות למערכת**: שבתאי צריך להתחבר למערכת של מנוע ישראל.
2. **מסירת מספר רכב**: שבתאי צריך למסור את מספר הרכב לרוב.
3. **קבלת אישור במייל**: שבתאי יקבל אישור במייל על התחברות למערכת.
4. **העברת האישור**: שבתאי צריך להעביר את האישור שקיבל במייל לרוב.
5. **שליחת מספר רכב בוואטסאפ**: רוב שלח לשבתאי את מספר הרכב בוואטסאפ, ושבתאי צריך להעביר אותו הלאה.

### המלצות:

1. **וידוא קבלת האישור**: שבתאי צריך לוודא שהוא אכן מקבל את האישור במייל ולבדוק את תקינותו.
2. **שמירת תיעוד**: לשמור את כל התכתובות והאישורים במקום מאובטח ונגיש לעתיד.
3. **בדיקת מערכת**: לאחר התחברות למערכת, לבדוק שהמערכת פועלת כראוי ושאין בעיות נוספות.
4. **תקשורת ברורה**: לוודא שכל ההוראות והמידע מועברים בצורה ברורה ומדויקת בין שבתאי לרוב, כדי למנוע אי הבנות.
5. **מעקב אחר התקדמות**: לקבוע תזכורת לבדוק שהפעולות הנדרשות בוצעו ושאין בעיות נוספות שדורשות טיפול.

בהתבסס על התמלול שסופק, הנה הניתוח שלי:

1. **בדיקה להפרות רגולטוריות:**
   - אין בתמלול הצהרות בלתי הולמות או שאינן עומדות בתקנות באופן ברור. עם זאת, יש לשים לב לשימוש במונחים כמו "מנוע ישראל" ו"התחברות למערכת", שיכולים לרמוז על תהליכים טכניים או רגולטוריים שדורשים בדיקה נוספת כדי לוודא עמידה בתקנות.

2. **עמידה בנהלים:**
   - השיחה מתנהלת בצורה מכבדת ואין שימוש בשפה פוגענית.
   - יש לשים לב לנושא של שמירה על סודיות. בתמלול יש התייחסות להעברת מספר רכב דרך וואטסאפ, מה שיכול להוות בעיה מבחינת שמירה על פרטיות המידע. יש לוודא שהעברת מידע כזה נעשית בהתאם לנהלים המתאימים.

3. **הדגשת חששות:**
   - יש חשש לגבי העברת מידע רגיש (כגון מספר רכב) דרך פלטפורמות שאינן מאובטחות מספיק, כמו וואטסאפ. מומלץ לבדוק אם יש צורך בנקיטת אמצעים נוספים לשמירה על פרטיות המידע.
   - יש לוודא שהפעולות המתוארות בתמלול, כמו "התחברות למנוע ישראל" ו"התקנת מערכות ברכב", נעשות בהתאם לנהלים ולתקנות הרלוונטיים.

בסיכום, אין בתמלול הפרות ברורות של תקנות, אך יש מספר נקודות שדורשות בדיקה נוספת כדי לוודא עמידה מלאה בנהלים ובתקנות.

תחום ההתמקדות: בעיות טכניות

### ניתוח מעמיק:

1. **חוסר בהירות בתהליך**: מהשיחה עולה כי ישנה חוסר בהירות לגבי התהליך של התחברות למערכת "מנוע ישראל". שבתאי אינו בטוח מה המידע הנדרש ממנו ומה עליו לעשות כדי להשלים את התהליך.

2. **תקשורת לא ברורה**: המידע שנמסר לשבתאי לא היה ברור מספיק, והוא נאלץ לשאול שאלות נוספות כדי להבין את הצעדים הנדרשים ממנו. זה מצביע על כך שההנחיות שניתנות ללקוחות אינן מספיק ברורות או מפורטות.

3. **תלות בתקשורת דיגיטלית**: השיחה מצביעה על תלות בתקשורת דיגיטלית (כגון מייל ווואטסאפ) להעברת מידע חשוב, כמו אישור התחברות ומספר רכב. זה יכול להוות בעיה אם יש תקלות טכניות או אם הלקוח אינו מיומן בשימוש בטכנולוגיה זו.

### תובנות ניתנות לפעולה:

1. **שיפור ההנחיות ללקוחות**: יש לפתח מדריך ברור ומפורט שיסביר ללקוחות את התהליך של התחברות למערכת, כולל כל המידע הנדרש מהם. ניתן לשקול גם יצירת סרטון הדרכה קצר שיסביר את התהליך בצורה ויזואלית.

2. **הדרכת נציגי שירות**: יש להדריך את נציגי השירות כיצד להעביר את המידע בצורה ברורה ומדויקת, ולוודא שהלקוח מבין את כל הצעדים הנדרשים ממנו.

3. **גיבוי לתקשורת דיגיטלית**: יש לוודא שישנן דרכים חלופיות להעברת מידע חשוב ללקוחות, כמו שיחה טלפונית או הודעת SMS, למקרה של תקלות במייל או בוואטסאפ.

4. **בדיקת מערכות טכניות**: לבדוק את המערכות הטכניות כדי לוודא שהן פועלות בצורה תקינה ושאין תקלות שמונעות מהלקוחות להתחבר למערכת בקלות.


"""
translated_text = translate_text_google_free(hebrew_text)
print(f"{translated_text}")













# import streamlit as st
# import json
# import os
# import re
# from pathlib import Path

# def load_json_data(json_file_path):
#     """Load JSON data from a file."""
#     with open(json_file_path, "r", encoding="utf-8") as file:
#         return json.load(file)

# def search_in_category(data, category, keyword):
#     """Search for a keyword in a selected category."""
#     if category not in data:
#         return []

#     # Filter the results that contain the keyword (case-insensitive)
#     return [item for item in data[category] if keyword.lower() in str(item).lower()]

# # Helper Functions
# def search_in_file_regex(filename, keyword):
#     """Search for a keyword in a file using regex (case-insensitive, whole word match)."""
#     results = []
#     pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)  # Whole word, case insensitive
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line_number, line in enumerate(file, start=1):
#             if pattern.search(line):
#                 results.append((line_number, line.strip()))  # Return line number and line content
#     return results

# def search_in_category(data, category, keyword):
#     """Search for a keyword in a selected category where all data is strings."""
#     if category not in data:
#         return []

#     category_data = data[category]

#     # Check if the keyword exists in the string (case-insensitive)
#     if keyword.lower() in category_data.lower():
#         return [category_data]  # Return the matching string
#     else:
#         return []  # Return an empty list if no match is found

# def main():
#     st.title("Category Search App")

#     # Directory containing JSON files (replace with your actual folder path)
#     folder_path = "./analytics"  # Replace with the actual folder path

#     # List all JSON files in the folder
#     if not os.path.exists(folder_path):
#         st.error("The folder does not exist! Please ensure the folder exists.")
#         return

#     files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

#     if not files:
#         st.warning("No JSON files found in the folder.")
#         return

#     # Allow user to select a file
#     selected_file = st.selectbox("Select a JSON file", files)

#     # Path to the selected JSON file
#     json_file_path = os.path.join(folder_path, selected_file)

#     # Load JSON data
#     data = load_json_data(json_file_path)

#     # Sidebar: Select category
#     categories = list(data.keys())
#     selected_category = st.sidebar.selectbox("Select a Category", categories)

#     # Search bar
#     keyword = st.text_input("Enter a keyword to search")

#     # Display results
#     if keyword:
#         st.subheader(f"Results in '{selected_category}':")
#         results = search_in_category(data, selected_category, keyword)

#         if results:
#             for result in results:
#                 st.write(result)
#         else:
#             st.warning("No results found.")

# if __name__ == "__main__":
#     main()





# import streamlit as st
# import json
# import os
# import re
# from pathlib import Path

# def load_json_data(json_file_path):
#     """Load JSON data from a file."""
#     with open(json_file_path, "r", encoding="utf-8") as file:
#         return json.load(file)

# def search_in_category(data, category, keyword):
#     """Search for a keyword in a selected category."""
#     if category not in data:
#         return []

#     category_data = data[category]

#     if isinstance(category_data, str):
#         # If it's a string, perform a direct search
#         return [category_data] if keyword.lower() in category_data.lower() else []
#     elif isinstance(category_data, list):
#         # Search in a list of strings or objects
#         return [item for item in category_data if keyword.lower() in str(item).lower()]
#     elif isinstance(category_data, dict):
#         # Search in nested dictionaries
#         return [val for key, val in category_data.items() if keyword.lower() in str(val).lower()]
#     else:
#         return []

# def search_in_file_regex(filename, keyword):
#     """Search for a keyword in a file using regex (case-insensitive, whole word match)."""
#     results = []
#     pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)  # Whole word, case insensitive
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             for line_number, line in enumerate(file, start=1):
#                 if pattern.search(line):
#                     results.append((line_number, line.strip()))  # Return line number and line content
#     except FileNotFoundError:
#         st.error(f"File not found: {filename}")
#     except Exception as e:
#         st.error(f"Error reading file {filename}: {e}")
#     return results

# def search_files_in_category(data, category, keyword):
#     """Search for a keyword in files listed under a selected category."""
#     if category not in data:
#         return []

#     results = []
#     for file_info in data[category]:
#         file_path = Path(file_info['path'])  # Replace 'path' with the actual field name
#         file_results = search_in_file_regex(file_path, keyword)
#         if file_results:
#             results.append({
#                 'file': file_path.name,
#                 'matches': file_results
#             })
#     return results

# def main():
#     st.title("Enhanced JSON Search App")

#     # Directory containing JSON files (replace with your actual folder path)
#     folder_path = "./analytics"  # Replace with the actual folder path

#     # List all JSON files in the folder
#     if not os.path.exists(folder_path):
#         st.error("The folder does not exist! Please ensure the folder exists.")
#         return

#     files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

#     if not files:
#         st.warning("No JSON files found in the folder.")
#         return

#     # Allow user to select a file
#     selected_file = st.selectbox("Select a JSON file", files)

#     # Path to the selected JSON file
#     json_file_path = os.path.join(folder_path, selected_file)

#     # Load JSON data
#     data = load_json_data(json_file_path)

#     # Sidebar: Select category
#     categories = list(data.keys())
#     selected_category = st.sidebar.selectbox("Select a Category", categories)

#     # Search bar
#     keyword = st.text_input("Enter a keyword to search")

#     # Display results
#     if keyword:
#         st.subheader(f"Results in '{selected_category}':")
#         results = search_in_category(data, selected_category, keyword)

#         if results:
#             st.write("### JSON Data Matches")
#             for result in results:
#                 st.write(result)
#         else:
#             st.warning("No results found in JSON data.")

#         # File search if category contains file paths
#         if isinstance(data[selected_category], list) and 'path' in str(data[selected_category]):
#             st.write("### File Search Matches")
#             file_results = search_files_in_category(data, selected_category, keyword)

#             if file_results:
#                 for file_result in file_results:
#                     st.subheader(f"File: {file_result['file']}")
#                     for line_number, content in file_result['matches']:
#                         st.write(f"Line {line_number}: {content}")
#             else:
#                 st.warning("No results found in associated files.")

# if __name__ == "__main__":
#     main()

