from google.adk.agents import Agent

# --------------------------------
# GENERATOR AGENT (AGENT 1)
# --------------------------------
generator_agent = Agent(
    name="generator_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a content generator agent.\n"
        "Generate a clear and concise answer to the user's question.\n"
        "Do your best, but assume it may be improved later."
    )
)

# --------------------------------
# CRITIC AGENT (AGENT 2)
# --------------------------------
critic_agent = Agent(
    name="critic_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a critic agent.\n"
        "Review the generated answer for correctness, clarity, and completeness.\n"
        "Provide constructive feedback and specific suggestions for improvement."
    )
)

# --------------------------------
# REFINED GENERATOR (FINAL STEP)
# --------------------------------
refiner_agent = Agent(
    name="refiner_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a refinement agent.\n"
        "Improve the original answer using the critic's feedback.\n"
        "Produce a refined, high-quality final response."
    )
)

# Root agent
root_agent = generator_agent
