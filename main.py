import cred
import google.generativeai as genai


genai.configure(api_key = cred.google_palm_api_key)

#or m in genai.list_models():
#    if 'generateContent' in m.supported_generation_methods:
#        print(m.name)


model = genai.GenerativeModel('gemini-1.0-pro-latest')


prompt = input("Enter your prompt: ")
response = model.generate_content(prompt)
print(response.text)
