from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
import logging

app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
openai.api_key = "PUt your OPENAI ke"

if not openai.api_key:
    logging.error("OpenAI API key is not set.")

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    logging.info(f"Received data: {data}")
    prompt = data.get('prompt', '')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        logging.info(f"OpenAI response: {response}")
        return jsonify({'response': response['choices'][0]['message']['content'].strip()})
    except openai.error.InvalidRequestError as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': 'Invalid request. Please check your input and try again.'}), 400
    except openai.error.AuthenticationError as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': 'Authentication failed. Please check your API key.'}), 401
    except openai.error.RateLimitError as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': 'Rate limit exceeded. Please try again later.'}), 429
    except openai.error.InsufficientQuotaError as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': 'You have exceeded your current quota. Please check your plan and billing details.'}), 402
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





