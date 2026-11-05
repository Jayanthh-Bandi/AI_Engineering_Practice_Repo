import os


from dotenv import load_dotenv

load_dotenv()

app_name=os.getenv("APP_NAME")
api_key=os.getenv("AI_API_KEY")

print("Application:",app_name)

if api_key:
    print("App name loaded successfully")
else:
    print("API key not loaded")