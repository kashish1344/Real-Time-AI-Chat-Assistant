
# Advanced AI Chatbot using Flask, LLaMA, and Tavily

This project demonstrates an advanced AI chatbot built using **Flask**, **LangChain's LLaMA**, and **Tavily Search API**. It is designed to provide both real-time information from the web and contextual conversational answers through a large language model. The chatbot first uses Tavily to search for real-time data. If no valid result is found, it falls back to the LLaMA model for a response.

## Features

- **Real-Time Web Search**: Powered by the Tavily Search API, allowing the bot to fetch up-to-date information from the web.
- **Conversational AI**: Uses LangChain's Ollama LLaMA 3.1 model for natural language processing and understanding.
- **Flask Integration**: A lightweight web framework to handle chat interactions seamlessly.
- **Balanced AI Responses**: Combines real-time web answers with conversational context, offering enhanced user experience.

## How It Works

1. **Tavily First**: For any query, the chatbot first attempts to retrieve real-time information using Tavily’s Q&A search.
2. **Fallback to LLaMA**: If Tavily doesn’t return a result, the chatbot uses the LLaMA model to generate a response based on the query.

## Project Structure

- `app.py`: Main Flask application file that handles the backend logic.
- `index.html`: Frontend HTML page where users interact with the chatbot.
- `style.css`: CSS file for styling the chat interface.
- `README.md`: This readme file.
- `requirements.txt`: Lists the required Python packages.

## Installation

To run this project locally, follow these steps:

### Prerequisites

- **Python 3.8+** installed on your machine.
- **Tavily API Key**: Sign up on [Tavily](https://tavily.com) and get your API key.

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/kashish1344/Real-Time-AI-Chat-Assistant.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Tavily API Key**:

    Open the `app.py` file and replace the placeholder `your-api-key` with your Tavily API key:
    
    ```python
    os.environ["TAVILY_API_KEY"] = "your-api-key"
    ```

5. **Run the Flask app**:

    ```bash
    python app.py
    ```

6. **Access the chatbot**:

    Open your browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## File Details

### `app.py`

- Initializes the Flask server and sets up the Tavily and LLaMA models.
- Handles incoming POST requests to `/chat` and returns JSON responses with either real-time web answers or fallback responses from LLaMA.

### `index.html`

- The frontend user interface for chatting with the bot. It includes a simple input field for the user to type queries and see responses.

### `style.css`

- Adds visual styling to the chat interface, including a modern design with gradients, hover effects, and more.

## Technologies Used

- **Python**: Core language for the backend.
- **Flask**: A lightweight web framework to serve the chatbot.
- **LangChain**: Uses the Ollama LLaMA model for conversational AI.
- **Tavily Search API**: Enables real-time web search.
- **HTML/CSS**: For building the user interface.

