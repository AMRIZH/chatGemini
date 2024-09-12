# AI Chat Project

## Table of Contents

- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## About

The **AI Chat Project** is an simple ai chat implementing GEMINI API and Gradio libary, so you will need to connected to internet. its easy and simple to install and use this program.

## Requirements

- Python 3.8 or higher
- Gradio
- Gemini API

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/AMRIZH/chatGemini.git
   cd ai-chat-project
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the NLP model:**

- get your own GEMINI API for free [here](https://aistudio.google.com/app/apikey)
- click on "create API key"
- follow the instructions until you get your API
- put your gemini api on main.py

```bash
# SET GOOGLE API KEY
GOOGLE_API_KEY = "YOUR_API_HERE" # change with your own Gemini API key
```

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Access the app:**
   Visit `http://127.0.0.1:7860` in your browser to interact with the AI chat.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project by opening an issue or submitting a pull request.
