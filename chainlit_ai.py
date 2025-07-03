import chainlit as cl
import os
from dotenv import load_dotenv
from agents import Runner, Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# 🔐 Load API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEYS")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# 🌐 Gemini Model Config
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# Agent instructions (feel free to update these)
instructions = """
You are a professional frontend developer assistant.
You can write code in HTML, CSS, JavaScript, Python, Java, and C++.
Provide well-commented code and clear explanations when answering.
"""

# Initialize the agent
agent = Agent(
    name="Bilal",
    instructions=instructions,
    model=model
)

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(
        content="Welcome to the AI Assistant! How can I help you today?",
        author="AI Assistant"
    ).send()

# Handle user messages
@cl.on_message
async def handle_message(message):
    # Get the user's message
    history = cl.user_session.get("history",[])

    # Append the new message to the history
    history.append({
        "role": "user",
        "content": message.content
    })

    result = await Runner.run(
        agent,
        input=history,
        run_config=config
    )

    history.append(
        {
            "role":"assistant",
            "content":result.final_output
        }
    )
    # Update the session history
    cl.user_session.set("history", history)

    # Send the agent's response
    await cl.Message(
        content=result.final_output
    ).send()
