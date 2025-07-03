from agents import Agent , OpenAIChatCompletionsModel,AsyncOpenAI,Runner,RunConfig
from dotenv import load_dotenv
import os


load_dotenv()
Open_Router_API_Keys=os.getenv("OPENROUTER_API_KEYS")

MODEL_NAME ="deepseek/deepseek-r1-0528:free"


if not Open_Router_API_Keys:
    raise ValueError("Open_Router_API_Keys is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=Open_Router_API_Keys,
    base_url='https://openrouter.ai/api/v1'
)

model=OpenAIChatCompletionsModel(
    openai_client=external_client,
    model=MODEL_NAME
)

config = RunConfig(
    model_provider=external_client,
    model=model,
    tracing_disabled=True
)

# Step 4: Urdu + English instruction
instructions = """
Aap ek mohtaram Urdu assistant hain. Har jawab Urdu mein dein, lekin har technical term (jaise programming language ka naam) ke saath uska English matlab bhi likhein. Aise jawab dein jo dono users ko samajh aayein — jo sirf Urdu jaante hain unhein bhi, aur jo English jaante hain unhein bhi.
"""

agent = Agent(
    name="Bilal",
    instructions=instructions,
    model=model
)

# Step 5: User se input lena
user_input = input("Aap ka sawal likhein (Urdu ya English mein): ")
res = Runner.run_sync(
    agent,
    user_input,
    run_config=config
)

print("\n🤖 Assistant ka jawab:\n")
print(res.final_output)