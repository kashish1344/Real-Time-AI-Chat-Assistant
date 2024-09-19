from flask import Flask, render_template, request, jsonify
from langchain_community.llms.ollama import Ollama
from langchain.prompts import PromptTemplate
from tavily import TavilyClient  # Tavily client import
import os

# Set Tavily API key
os.environ["TAVILY_API_KEY"] = "your-api-key" # Enter your key here

# Initialize Flask app
app = Flask(__name__)

# Initialize the Ollama Llama 3.1 model
chat_model = Ollama(model="llama3.1")
# Initialize the Tavily search client
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Create a web search tool using Tavily
def search_web(query: str) -> str:
    """Search the web for a query using Tavily."""
    response = tavily_client.qna_search(query=query)  # Use Q&A search method
    return response if response else None

# Create a prompt template for LLaMA model
prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""Answer the question using the following context.
    If the answer is not in context, use the tools available to get the answer.
    Question: {question}
    Context: {context}
    Answer:"""
)

# Build the chain using the LLaMA model and prompt
llm_chain = prompt_template | chat_model

# Chatbot endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No input provided"})

    # First, try to get the answer via Tavily
    answer = search_web(user_input)

    if not answer:
        # If Tavily doesn't return a valid result, fall back to LLaMA
        response = llm_chain.invoke({"context": "", "question": user_input})
        answer = response.strip() if response.strip() else "Sorry, I couldn't find an answer to your question."

    return jsonify({"response": answer})

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
