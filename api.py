# create.py

import json
import os
from pathlib import Path
import convert
import openai

def generate(prompt):
        
    PROMPT = prompt
    DATA_DIR = Path.cwd() / "responses"

    DATA_DIR.mkdir(exist_ok=True)

    openai.api_key = "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"

    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="1024x1024",
        response_format="b64_json",
    )

    file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response, file)

    convert.image(file_name)
    