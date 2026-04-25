# 1. Parent Class (Base Blueprint)
class BaseLLM:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def log_status(self):
        print(f"🤖 Processing with {self.model_name}...")

    def generate(self, prompt: str):
        # This is a placeholder, to be overridden by child classes
        pass

# 2. Child Class for OpenAI
class OpenAIModel(BaseLLM):
    def generate(self, prompt: str):
        self.log_status()  # Using parent's method
        return f"OpenAI Response for '{prompt}': Success"

# 3. Child Class for Gemini
class GeminiModel(BaseLLM):
    def generate(self, prompt: str):
        self.log_status()  # Using parent's method
        return f"Gemini Response for '{prompt}': Success"

# --- Execution (Run the code) ---

# Testing OpenAI
gpt = OpenAIModel("GPT-4")
print(gpt.generate("What is AI?"))

print("-" * 40)

# Testing Gemini
gemini = GeminiModel("Gemini-Pro")
print(gemini.generate("Why use Python?"))