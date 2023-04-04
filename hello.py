from flask import Flask,request
import os
import openai
from flask import jsonify

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():

    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/generate_code', methods=['GET'])
def generate_code():
    language = request.args.get('language')
    content = request.args.get('content')
    prompt = f"generate {language} code:\n{content}"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        )
    return completion['choices'][0]['message']['content']

#     # Use the OpenAI Codex API to generate code
#     prompt = f"generate {language} code:\n{content}"
#     response = openai.Completion.create(
#         engine='davinci-codex',
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     # Extract the generated code from the API response
#     code = response.choices[0].text.strip()

#     return jsonify({'code': code})