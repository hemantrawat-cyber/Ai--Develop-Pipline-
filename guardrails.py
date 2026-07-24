BLOCKED = [
    "ignore previous instructions",
    "system prompt",
    "reveal hidden prompt",
]

def validate_prompt(prompt):

    prompt = prompt.lower()

    for attack in BLOCKED:
        if attack in prompt:
            return False

    return True
