import os
from google import genai
from google.genai import types
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def send_to_gemini(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[user_input]
        )
        return response.text
    except Exception as e:
        return str(e)

def generate_fir(crime_scene, objects, people, text, more_context):
    prompt = f"""
    You are an expert crime analyst. Given the crime scene details, detected objects, and people involved, generate an FIR report with possible assumptions and suggested next steps.

    Crime Scene: {crime_scene}
    Objects Found: {', '.join(objects)}
    People Mentioned: {', '.join(people)}
    Incident Description: {text}

    Provide:
    1. A structured **FIR Report**
    2. **Logical Assumptions** based on the details.
    3. **Next Steps for Investigation**


    more context:{more_context}

    note:
    no need to mention anything else just straight report and no need to mention hypothetical
    """

    response_text = send_to_gemini(prompt)
    return response_text
