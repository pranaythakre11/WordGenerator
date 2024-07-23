Automated Text Generator

Description

"Automated Text Generation for Content Creation. Build a system to generate human-like text content (e.g., articles, stories, scripts) based on specified topics or prompts. Python, NLP libraries, Language Generation models (e.g., GPT-3, BART). Web application or desktop software for inputting prompts and displaying generated text."

## Key Components:
- **Language Generation Models**: Utilizing state-of-the-art models like GPT-3 and BART to ensure high-quality, coherent, and contextually relevant text generation.

- **NLP Libraries**: Incorporating powerful NLP libraries to preprocess input prompts, manage model interactions, and enhance the generated text's quality.

- **User Interface**: Developing a web application or desktop software that provides an intuitive interface for users to input prompts and receive generated text outputs. This interface will facilitate easy interaction with the text generation system.

- **Customization and Flexibility**: Allowing users to specify various parameters and topics to tailor the generated content to their specific needs, ensuring versatility and adaptability for different content creation scenarios.

- **Integration and Deployment**: Implementing the system within a Python environment, utilizing a virtual environment for dependencies and libraries management, and ensuring a seamless deployment process for users.

## Features

- **Text Generation**: Produces relevant and context-aware text based on user input.
- **Web Interface**: Simple and user-friendly web interface for input and output.
- **Customization**: Easy to modify and extend for various text generation applications.
- **Virtual Environment**: Isolated environment to manage dependencies.

## Libraries Used
- **Python**: The core programming language.
- **OpenAI**: For accessing the OpenAI API.
- **Flask**: For creating the web application.
- **dotenv**: For loading environment variables from a .env file.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computing.
- **Requests**: For making HTTP requests.

## Procedure

1.Installation

-> Create and Activate Virtual Environment
Below is the Command
"python -m venv venv"
"source venv/bin/activate"  

2.Install Dependencies
->Install all the required libraries
pip install -r requirements.txt

**Set Up OpenAI API Key
In app.py file ,correctly set up your aopenai api key.
OPENAI_API_KEY=your_openai_api_key

4.Running the Project

->Start the Application
Run "python main.py" on terminal.

->Access the Application
Open your web browser and go to http://localhost:5000