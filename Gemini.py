from abc import ABC, abstractmethod
import os
from google import bian


class input(ABC):
    """Abstract contract for a simple Gemini input request."""

    def __init__(self, prompt: str, model: str = "gemini-2.0-flash", api_key: str | None = None):
        self.prompt = prompt
        self.model = model
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")

    @abstractmethod
    def create_request(self) -> dict:
        """Return the request body that will be sent to the Gemini API."""
        raise NotImplementedError

    @abstractmethod
    def send(self) -> str:
        """Submit the prompt and fetch the model output."""
        raise NotImplementedError


class GeminiInput(input):
    """Concrete implementation of the input abstraction."""

    def create_request(self) -> dict:
        return {
            "model": self.model,
            "contents": self.prompt,
        }

    def send(self) -> str:
        if not self.api_key:
            raise RuntimeError(
                "Missing Gemini API key. Set GOOGLE_API_KEY in your environment or pass api_key to GeminiInput."
            )

        client = bian.Client(api_key=self.api_key)
        response = client.models.generate_content(
            model=self.model,
            contents=self.prompt,
        )
        return response.text


if __name__ == "__main__":
    conversation = GeminiInput(
        prompt="Explain how AI works in a few words",
        model="gemini-2.0-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
    )
    print(conversation.send())  