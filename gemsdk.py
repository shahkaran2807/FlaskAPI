from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from sysprompt import sysprompt


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def hello_world():

  request_data = request.json  # Assuming JSON payload
  text = request_data.get('text')

  genai.configure(api_key='AIzaSyCUPVKqstzD52O6PgEHCCBRhrq4mfhiI6Q')
  model = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction={sysprompt})
  response = model.generate_content(text)

  # print(response.text)
  return jsonify({'response': response.text})

if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=3000) 
    app.run()