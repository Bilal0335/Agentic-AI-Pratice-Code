from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
open_router_api_key = os.getenv("OPENROUTER_API_KEYS")

if not open_router_api_key:
    raise ValueError("OPENROUTER_API_KEYS is not set in the environment variables.")

async def main():
        MODEL_NAME="deepseek/deepseek-r1-0528:free"

        external_client = AsyncOpenAI(
            api_key=open_router_api_key,
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


        instructions = """
        Aap aik intelligent assistant hain.

        1. Agar user ka sawaal English mein ho, to jawab bhi sirf English mein dein.
        2. Agar sawaal Roman Urdu ya Urdu mein ho, to jawab sirf Roman Urdu mein dein.
        3. Har jawab simple, short aur aam zaban mein ho.
        4. Kisi formatting, headings, ya bullet points ka istemal na karein.
        """

        agent = Agent(
            name="Bilal",
            instructions=instructions,
            model=model
        )
        user_input = input("Apna sawaal likhein (Urdu ya English mein): ")


        res = await Runner.run(
            agent,
            user_input,
            run_config=config
        )

        # Step 6: Print output
        print("\n🤖 Assistant ka jawab:\n")
        print(res.final_output)

if __name__ == "__main__":
      asyncio.run(main())
      