from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.messages import HumanMessage, SystemMessage
from app.constants import Q_MODEL_NAME
from app.logging import logging
from app.exceptions import LlmAppException
import sys

class QuestionAnalysisModel:
    """
    QuestionAnalysisModel:
    This class is responsible for analyzing user-provided answers using the Llama3.3 (text-only) model.

    Key Components:
    - Initializes ChatOllama with specified model.
    - Defines a prompt template with system instructions and user answers.
    - Formats the prompt dynamically.
    - Calls the Ollama model to generate a response.
    - Implements logging and exception handling.
    """

    def __init__(self):
        """
        Initializes the QuestionAnalysisModel:
        - Loads the LLM model using ChatOllama.
        - Sets up a ChatPromptTemplate with placeholders for dynamic prompts.
        """
        try:
            # Initialize ChatOllama with the model name from constants
            self.llm = ChatOllama(model=Q_MODEL_NAME)
            logging.info(f"Question model ({Q_MODEL_NAME}) initialized successfully")

            # Create a prompt template with placeholders for instructions and user answers
            self.prompt_template = ChatPromptTemplate.from_messages([
                ("system", "{instructions}"),  # System message with general instructions
                ("user", "Name of the user: {user_answers}")  # User message with dynamic answers
            ])

        except Exception as e:
            logging.error(f"Failed to initiate Question Model: {e}")
            raise LlmAppException(e, sys)

    def get_response(self, instructions: str, user_answers: str) -> str:
        """
        Generates a response from the model based on given instructions and user answers.

        Parameters:
        - instructions (str): System-level instructions for the model.
        - user_answers (str): The user's input answers.

        Returns:
        - str: Model-generated response.
        """
        try:
            # Format the prompt with actual instructions and user answers
            formatted_prompt = self.prompt_template.format_messages(
                instructions=instructions,
                user_answers=user_answers
            )

            # Call the LLM model to generate the response
            response = self.llm.invoke(formatted_prompt)
            logging.info("Successfully generated response from Question Model")

            return response.content

        except Exception as e:
            logging.error(f"Error during question model inference: {e}")
            raise LlmAppException(e, sys)
