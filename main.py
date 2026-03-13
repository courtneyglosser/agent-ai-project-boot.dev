
import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Could not load Gemini API key")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

def main():

    if api_key == None:
        raise Exception("Scope problems with api_key")
    else:
        client = genai.Client(api_key=api_key)

        # content = args.user_prompt  # Replaced by messages

        messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

        res = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=messages
        )

    if res.usage_metadata == None:
        raise RuntimeError("Error connecting to Gemini API")
    else:
        print (f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print (f"Response tokens: {res.usage_metadata.candidates_token_count}")

        print (f"Response from Gemini API: {res.text}")


if __name__ == "__main__":
    main()
