# Gradio & FastAPI LLM Example

## Description
This is a simple FastAPI-based application that utilizes the OpenAI Language Model (LLM) via Langchain. It serves as a demonstration of extracting desired information from input Arabic text using the OpenAI LLM.

## Dependencies
- Install the required dependencies by executing the following command:
    ```
    pip install -r requirements.txt
    ```
- Create a `.env` file in the root directory and populate it with the necessary information as follows:
    ```
    API_KEY = ""
    TEMPERATURE = 0
    MODEL_NAME = ""
    ```

## Running the Application
**Using FastApi**
- Execute the following command to run the application:
    ```
    uvicorn fastapi_app:app --reload 
    ```
**Using gradio**
- Execute the following command to run the application:
    ```
    python3 gradio_app.py
    ```
This command will start the server, allowing you to interact with the FastAPI application.