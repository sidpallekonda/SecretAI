import google.generativeai as genai

genai.configure(api_key="AIzaSyDFpKUWzok96wA4vqH9G2RCJ4kBE8rYtSc")

models = genai.list_models()
for m in models:
    print(m.name)
