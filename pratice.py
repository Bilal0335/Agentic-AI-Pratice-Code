from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, RunConfig
from dotenv import load_dotenv
import os

# Step 1: Load API key from .env
load_dotenv()
Open_Router_API_Keys = os.getenv("OPENROUTER_API_KEYS")

if not Open_Router_API_Keys:
    raise ValueError("OPENROUTER_API_KEYS is not set in the environment variables.")

# Step 2: Model setup
MODEL_NAME = "deepseek/deepseek-r1-0528:free"

external_client = AsyncOpenAI(
    api_key=Open_Router_API_Keys,
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model=MODEL_NAME
)

config = RunConfig(
    model_provider=external_client,
    model=model,
    tracing_disabled=True
)

# Step 3: Auto language match instruction
instructions = """
Always respond in the same language that the user used in their question.
If the question is in English, answer in English.
If the question is in Urdu (Roman or native), answer in Urdu.
Keep the tone polite and helpful.
"""

agent = Agent(
    name="Bilal",
    instructions=instructions,
    model=model
)

# Step 4: User input
user_input = input("Apna sawaal likhein (Urdu ya English mein): ")

# Step 5: Run agent
res = Runner.run_sync(
    agent,
    user_input,
    run_config=config
)

# Step 6: Print output
print("\n🤖 Assistant ka jawab:\n")
print(res.final_output)
