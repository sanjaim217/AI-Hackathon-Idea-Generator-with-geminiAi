import google.generativeai as genai
from prompts import hackathon_prompt

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

domain = input("Enter domain (AI / Web / FinTech / Health): ")
level = input("Difficulty (Beginner / Intermediate / Advanced): ")
users = input("Target users: ")

prompt = hackathon_prompt(domain, level, users)

response = model.generate_content(prompt)

print("\n🚀 Hackathon Idea Generated:\n")
print(response.text)
